# A Django API for the Ember.js Super Rentals Application

Super rentals is the official Ember.js tutorial application. It is a simple read only application. With the Django Admin you can perform all CRUD operations at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)


## Prerequisites

You will need the following things properly installed on your computer (unless using Docker).

- [Git](https://git-scm.com/)
- [Python](https://www.python.org/)
- [Poetry](https://python-poetry.org/)
- [Mariadb](https://mariadb.org/) or any other MySQL compatible database. You'll need to create a database with the right user with permission for said database (see the [settings.py file](backend/settings.py) for DATABASE configuration settings)

## Installation

- `git clone <repository-url>` this repository
- `cd backend`
- `poetry install`

## Running / Development

- `poetry shell` - this must be ran before everything as it sets up your shell with the project's python environment
- If it's your first time running the app or you need to run a database migration you need to do `python manage.py migrate`
- `python manage.py runserver` - the database will need to be running
- Visit your app at [http://127.0.0.1:8000](http://127.0.0.1:8000).
  - If you want some data to play with you can load the fixture with:
  - `python manage.py loaddata initial-data.json`
- Visit the Django Admin at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin).
  - You will also need to create a superuser, you can do so with:
  - `DJANGO_SUPERUSER_PASSWORD=admin DJANGO_SUPERUSER_USERNAME=admin DJANGO_SUPERUSER_EMAIL=admin@example.com python manage.py createsuperuser --noinput`
    - This was already ran if you used the 'initial-data.json' fixture
- Visit the browseable API at [http://127.0.0.1:8000/api/rentals](http://127.0.0.1:8000/api/rentals).
- Visit the API Documentation at [http://127.0.0.1:8000/swagger-ui/](http://127.0.0.1:8000/swagger-ui/)
- If using docker: `docker-compose up backend`
  - This should set up everything including an administrator account with initial data.

### Running Tests

- `pytest`

### Linting

- `flake8 .`

### Deploying

Deployed using [zappa](https://github.com/zappa/Zappa) to [AWS Lambda](https://aws.amazon.com/lambda/)

Basically:
`zappa init`
`zappa deploy`
`zappa manage migrate`

You'll need a MYSQL database to connect to. Ideally this lambda + the database are in a VPC and the database is inaccessible from the outside (while the lambda has it's own security group to make it accessible from the internet). Here's an example zappa_settings:

```json
{
    "dev": {
      "django_settings": "backend.settings",
      "profile_name": null,
      "project_name": "backend",
      "runtime": "python3.8",
      "s3_bucket": "zappa-ember-django-example",
      "keep_warm": false,
      "aws_environment_variables": {
        "RDS_DB_HOST": "your-mysql-hostname",
        "RDS_DB_NAME": "zappa_ember_django_example",
        "RDS_DB_USER": "zappa_ember_django_example",
        "RDS_DB_PASSWORD": "your-mysql-password",
        "RDS_DB_PORT": "3306",
        "DJANGO_SECRET_KEY": "your-django-secret-key"
      },
      "vpc_config": {
        "SubnetIds": [ "your-subnet-id" ],
        "SecurityGroupIds": [ "your-securitygroup" ]
      }
    }
}
```

Additonally:
- You should modify the settings file to set the `CORS_ALLOWED_ORIGINS` and `ALLOWED_HOSTS`. Presently anything is allowed which isn't very secure.
- We are using [PyMySQL](https://github.com/PyMySQL/PyMySQL) as zappa doesn't provide an updated MySQL system package in the lambda environment. Hopefully zappa provides updated packages in the future.

## Further Reading / Useful Links

- [Django](https://docs.djangoproject.com/en/3.2/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Django Rest Framework JSONAPI](https://github.com/django-json-api/django-rest-framework-json-api)
- [Zappa](https://github.com/zappa/Zappa)
