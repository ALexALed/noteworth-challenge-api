FROM python:3.8.3-slim as python-base

RUN mkdir /noteworth_challenge_api 

COPY /noteworth_challenge_api/noteworth_challenge_api /noteworth_challenge_api/noteworth_challenge_api
COPY /noteworth_challenge_api/poetry.lock /noteworth_challenge_api
COPY /noteworth_challenge_api/pyproject.toml /noteworth_challenge_api
COPY /noteworth_challenge_api/data.json /noteworth_challenge_api

WORKDIR /noteworth_challenge_api

ENV PYTHONPATH=${PYTHONPATH}:${PWD} 

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.0.5 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

ENV FLASK_RUN_HOST=0.0.0.0

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

EXPOSE 5000

CMD ["poetry", "run", "flask", "run"]