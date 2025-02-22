FROM node:16

WORKDIR /app

COPY frontend/package.json frontend/package-lock.json frontend/tsconfig.json ./
COPY frontend/public/ public/
COPY frontend/src/ src/

RUN npm install

EXPOSE 3001
CMD ["npm", "start"]