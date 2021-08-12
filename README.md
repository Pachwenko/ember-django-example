# ember-django-example
Example frontend and backend using Ember.js, Python and Django

## Gameplan

- Build out a simple frontend using the official ember tutorial https://guides.emberjs.com/v3.24.0/tutorial/part-1/
- Refactor the frontend to use miragejs
- Build the backend to fit the frontend's miragejs json-api spec using djangorestframework with djangorestframework-jsonapi
  - Obviously test drive it, I think the frontend tutorial covers testing as well
- Refactor the fronted to use the backend's API
- Once things work make a docker-compose to run the frontent, backend, and database with hot reloading
  - Maybe test the performance of hot reloading on Macos as mounting directories supposedly makes things very slow on top of the virtualization overhead... Might be something else we can try
  - Maybe explore full stack testing with something like cypress
- Update docs like this readme, add individual readmes for the frontend and back ( make sure to include non-docker usage stuff )
- Make some kind of blog post (my blog?).
  - A general overview of how the frontend and backend communicate, less about the syntax.
  - Another blog post with code examples of like "JSON-API vs not JSON-API".
  - Maybe the world could use another tooling blog post as well. Using docker I'd guess this deploys easily to something like heroku or digital ocean.
  - And another one about CI. We can make use of free github actions since this is open source, but CD is likely automatically managed with heroku or digital ocean.
  - Another one about Django swagger docs and djangoresetframework API browser?
