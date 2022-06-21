# build
FROM node:15.13-alpine

WORKDIR /app

COPY package.json .

COPY package-lock.json .

COPY . .

RUN npm i

RUN npm run build
