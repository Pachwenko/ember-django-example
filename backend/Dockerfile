FROM python:3.9

WORKDIR /code
ENV PYTHONUNBUFFERED=1
COPY poetry.lock ./
COPY pyproject.toml ./
RUN pip install poetry
RUN poetry config virtualenvs.create false
EXPOSE 8000

ENV PYTHON_ENV=development
RUN poetry install
COPY . /code
CMD ["poetry", "run", "python", "manage.py", "runserver"]