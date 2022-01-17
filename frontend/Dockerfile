FROM node:14

WORKDIR /code
EXPOSE 4200

ENV CI=true
ENV NODE_ENV=development
COPY . /code
RUN rm -rf node_modules && npm install
CMD ["npm", "run", "star"]