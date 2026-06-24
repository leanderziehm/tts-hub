from fastapi import FastAPI, BackgroundTasks, HTTPException
from fastapi.responses import FileResponse
from sse_starlette.sse import EventSourceResponse
import asyncio
import json
import os
import subprocess
import tempfile
import uuid
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # lock down later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

jobs = {}
subscribers = {}


def publish(job_id: str, event: str, data: dict):
    queues = subscribers.get(job_id, [])

    payload = {
        "event": event,
        "data": json.dumps(data),
    }

    for queue in queues:
        queue.put_nowait(payload)


async def run_tts(job_id: str, text: str, voice: str):
    workdir = tempfile.mkdtemp(prefix=f"{job_id}_")

    try:
        wav_file = os.path.join(workdir, "speech.wav")
        mp3_file = os.path.join(workdir, "speech.mp3")

        jobs[job_id]["status"] = "synthesizing"

        await asyncio.to_thread(
            subprocess.run,
            [
                "espeak-ng",
                "-v",
                voice,
                "-w",
                wav_file,
                text,
            ],
            check=True,
        )

        publish(
            job_id,
            "tts.completed",
            {
                "job_id": job_id,
            },
        )

        jobs[job_id]["status"] = "converting"

        await asyncio.to_thread(
            subprocess.run,
            [
                "ffmpeg",
                "-y",
                "-i",
                wav_file,
                "-codec:a",
                "libmp3lame",
                mp3_file,
            ],
            check=True,
            capture_output=True,
        )

        publish(
            job_id,
            "mp3.completed",
            {
                "job_id": job_id,
            },
        )

        jobs[job_id]["status"] = "ready"
        jobs[job_id]["mp3"] = mp3_file

        publish(
            job_id,
            "file.ready",
            {
                "job_id": job_id,
                "download_url": f"/v1/jobs/{job_id}/download",
            },
        )

    except Exception as e:
        jobs[job_id]["status"] = "failed"

        publish(
            job_id,
            "job.failed",
            {
                "job_id": job_id,
                "error": str(e),
            },
        )


@app.post("/v1/speech")
async def create_speech(
    payload: dict,
    background_tasks: BackgroundTasks,
):
    job_id = str(uuid.uuid4())

    jobs[job_id] = {
        "status": "queued",
    }

    background_tasks.add_task(
        run_tts,
        job_id,
        payload["text"],
        payload.get("voice", "en-us"),
    )

    return {
        "job_id": job_id,
        "status": "queued",
        "events_url": f"/v1/jobs/{job_id}/events",
    }


@app.get("/v1/jobs/{job_id}/events")
async def events(job_id: str):
    if job_id not in jobs:
        raise HTTPException(404)

    queue = asyncio.Queue()

    subscribers.setdefault(job_id, []).append(queue)

    async def event_generator():
        try:
            while True:
                msg = await queue.get()

                yield {
                    "event": msg["event"],
                    "data": msg["data"],
                }

        finally:
            subscribers[job_id].remove(queue)

    return EventSourceResponse(event_generator())


@app.get("/v1/jobs/{job_id}/download")
async def download(job_id: str):
    job = jobs.get(job_id)

    if not job:
        raise HTTPException(404)

    if job["status"] != "ready":
        raise HTTPException(409)

    return FileResponse(
        path=job["mp3"],
        media_type="audio/mpeg",
        filename=f"{job_id}.mp3",
    )