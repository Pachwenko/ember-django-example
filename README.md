# ember-django-example
Example frontend and backend using Ember.js, Python and Django

## Gameplan

- [x] Build a simple frontend using the official ember [tutorial](https://guides.emberjs.com/release/tutorial/part-1/)
- [x] Refactor the frontend to use miragejs
- [] Add github action to run the frontend tests (make sure linting is part of the tests)
- [] Build the backend to fit the frontend's miragejs json-api spec using djangorestframework with djangorestframework-jsonapi
  - Test drive this
- [] Refactor the fronted to use the backend's API
- [] Make a docker-compose to run the frontent, backend, and database with hot reloading
  - Maybe test the performance of hot reloading on Macos as mounting directories supposedly makes things very slow on top of the virtualization overhead... Might be something else we can try
  - Maybe explore full stack testing with something like cypress
- [] Update docs like this readme, add individual readmes for the frontend and back ( make sure to include non-docker usage stuff )