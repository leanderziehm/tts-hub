FROM python:3.11-slim

# System deps for TTS + audio conversion
RUN apt-get update && apt-get install -y \
    espeak-ng \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python deps first (better layer caching)
COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy only what is needed
COPY ./src/main.py /app/src/main.py

# If you serve frontend from FastAPI (optional)
# COPY src/static /app/src/static

ENV PYTHONUNBUFFERED=1

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]