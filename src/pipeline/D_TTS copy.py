

# from fastapi import FastAPI, HTTPException
# from fastapi.responses import FileResponse
import subprocess
import uuid
from pathlib import Path

# app = FastAPI(title="ESpeak TTS Service")

# OUTPUT_DIR = Path("/tmp/tts_out")
# OUTPUT_DIR.mkdir(exist_ok=True)

# @app.post("/synthesize")
def synthesize(text: str,out_file):
    # try:
        # out_file = OUTPUT_DIR #+ f"{uuid.uuid4()}.wav"
        subprocess.run(
            ["espeak", text, "--stdout"],
            check=True,
            stdout=open(out_file, "wb")
        )
        # return FileResponse(out_file, media_type="audio/wav", filename=out_file.name)
    # except Exception as exc:
        # raise HTTPException(status_code=500, detail=str(exc))


if __name__ == "__main__":
    input_file_path =  "output/1571170655_cleanmanual_clean.txt"
    output_path = "output/1571170655.wav" 
    with open(input_file_path, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()
    synthesize(text,output_path)

