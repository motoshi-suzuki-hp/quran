FROM python:3.9

# 必要なシステム依存関係をインストール
RUN apt-get update && apt-get install -y libsndfile1 ffmpeg espeak-ng \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# アプリケーションの依存関係をインストール
WORKDIR /app

COPY media/audio/ /app/media/audio/

COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ /app/

EXPOSE 5001
CMD ["python", "main.py"]
