FROM node:16

WORKDIR /app

COPY package.json package-lock.json tsconfig.json ./
COPY public/ public/
COPY src/ src/

RUN npm install

EXPOSE 3001
CMD ["npm", "start"]