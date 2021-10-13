# ember-django-example
Example frontend and backend using Ember.js, Python and Django

This is supposed to be a simple application to demonstrate a full stack web application using Ember.js with Python + Django. It is based upon the [official ember tutorial](https://guides.emberjs.com/release/tutorial/part-1/).

The frontent connects to the backend using [Ember Data's JSONAPI adapter](https://guides.emberjs.com/release/models/customizing-adapters/).

For more info see the README for the [frontend](frontend/README.md) or [backend](backend/README).



## Feature branches

This project has a few branches you can check out:

- [main](https://github.com/Pachwenko/ember-django-example/tree/main) This is supposed to be a minimal application that's easy to tinker with and understand.
- [cypress](https://github.com/Pachwenko/ember-django-example/tree/cypress) Has high level integration tests. Cypress is a much more enjoyable test runner/write than Ember's default of testem.


## Running locally

To run the full stack at once the easiest way is with [Docker](https://docs.docker.com/get-started/). With docker installed you can run (in the this folder) `docker-compose up`. This will automatically reload upon any changes. If you just want to run the backend for example you can do `docker-compose up backend`.

Otherwise you will need to run the frontend and backend simultaneously. Presently the backend uses sqlite so you do not need to run the database.