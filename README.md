# ember-django-example
Example frontend and backend using Ember.js, Python and Django

## Gameplan

- Build out a simple frontend using the official ember tutorial https://guides.emberjs.com/v3.24.0/tutorial/part-1/
- Refactor the frontend to use miragejs
- Build the backend to fit the frontend's miragejs json-api spec using djangorestframework with djangorestframework-jsonapi
  - Obviously test drive it, I think the frontend tutorial covers testing as well
- Refactor the fronted to use the backend's API
- Once things work locally build a docker-compose to run the frontent, backend, and database with hot reloading
  - Maybe test the performance of hot reloading on Macos as mounting directories is supposedly a huge pain on top of the virtualization overhead... Might be something else we can try
  - Maybe explore full stack testing with something like cypress
