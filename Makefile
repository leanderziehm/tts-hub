pdf2txt:
	uv run -m src.pdf_pipeline.B_pdf_text_extraction /home/user/Documents/p4_exam/datacenter-networkprogramming-slides_reduced2.pdf

cont:
	podman build -t tts-api -f docker/Dockerfile . && podman run -p 8000:8000 tts-api
run:
	uv run uvicorn src.main:app --reload
# 	uv run -m src.main

clean:
	uv run -m src.pdf_pipeline.C_clean_text

tts espeak:
	uv run -m src.pdf_pipeline.D_TTS

	
