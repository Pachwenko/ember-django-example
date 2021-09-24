FROM node:10 as base

WORKDIR /code
COPY package.json ./
COPY package-lock.json ./
EXPOSE 4200

FROM base as production
ENV NODE_ENV=production
RUN npm ci
COPY . /code
CMD ["npm", "run", "build"]

FROM base as development
ENV NODE_ENV=development
RUN npm install
COPY . /code
CMD ["npm", "run", "build"]