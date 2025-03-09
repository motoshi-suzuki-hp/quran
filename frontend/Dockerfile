# Stage 1: Build React app
FROM node:16 AS builder
WORKDIR /app
# package.json, package-lock.json をコピーして依存関係をインストール
COPY frontend/package.json frontend/package-lock.json ./
RUN npm install
# ソースコードをコピーしてビルド
COPY frontend/ .
RUN npm run build

# Stage 2: Serve the static files using 'serve'
FROM node:16-alpine
WORKDIR /app
# serve をグローバルにインストール
RUN npm install -g serve
# ビルド済みファイルをコピー
COPY --from=builder /app/build ./build
# Cloud Run は PORT 環境変数（通常3000）を設定するのでそれに合わせる
EXPOSE 3000
# CMD で環境変数 PORT を使うようにする
CMD ["sh", "-c", "serve -s build -l ${PORT:-3000}"]
