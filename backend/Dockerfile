FROM python:3.6 as base

WORKDIR /code
ENV PYTHONUNBUFFERED=1
COPY poetry.lock ./
COPY pyproject.toml ./
RUN pip install poetry
RUN poetry config virtualenvs.create false
EXPOSE 8000

FROM base as production
ENV PYTHON_ENV=production
COPY . /code
RUN poetry install --no-dev
CMD ["poetry", "run", "python", "manage.py", "runserver"]

FROM base as development
ENV PYTHON_ENV=development
RUN poetry install
COPY . /code
CMD ["poetry", "run", "python", "manage.py", "runserver"]