FROM node:14

WORKDIR /code
COPY package.json ./
COPY package-lock.json ./
EXPOSE 4200

# update system
RUN apt update && apt upgrade -y

# Install google-chrome for ember tests
RUN \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt install ./google-chrome-stable_current_amd64.deb -y

ENV CI=true
ENV NODE_ENV=development
RUN npm install
COPY . /code
CMD ["npm", "run", "build"]