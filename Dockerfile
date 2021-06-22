FROM python:3.8-alpine

WORKDIR /bot
COPY ./bot/ $WORKDIR/
COPY pyproject.toml poetry.lock $WORKDIR/
# Install poetry:
RUN pip install poetry
RUN poetry install --no-root --no-dev


CMD ["python3", "main.py"]
