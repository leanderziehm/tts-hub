cont:
	podman build -t tts-api -f docker/Dockerfile . && podman run -p 8000:8000 tts-api
run:
	uv run uvicorn src.main:app --reload
# 	uv run -m src.main

clean:
	uv run -m src.pipeline.C_clean_text

tts espeak:
	uv run -m src.pipeline.D_TTS

	
