FROM python:3.8.6-alpine3.12@sha256:09b31747042d2b4445d222481b326a089207dfe2007df0a3c00d0662d010d73a

RUN apk --no-cache add --virtual build-dependencies build-base libffi-dev openssl-dev

RUN pip3 install poetry
RUN mkdir /app
WORKDIR /app
COPY pyproject.toml /app
COPY poetry.lock /app
RUN POETRY_VIRTUALENVS_IN_PROJECT=true poetry install --no-dev
COPY api.py /app
COPY gunicorn_config.py /app

RUN apk del build-dependencies

EXPOSE 8000

# CMD [ "/app/.venv/bin/python3", "-m", "uvicorn", "--host", "0.0.0.0", "api:app" ]
# Benchmarker with: wrk -t100 -c200 http://127.0.0.1:8000
# 3x Requests/sec:   1367.84 1357.73 1310.01

# CMD [ "/app/.venv/bin/gunicorn", "-k", "uvicorn.workers.UvicornH11Worker", "--bind", "0.0.0.0:8000", "api:app" ]
# Benchmarker with: wrk -t100 -c200 http://127.0.0.1:8000
# 3x Requests/sec:   1728.74 1760.11 1787.55

# Like ANW target solution
CMD ["/app/.venv/bin/gunicorn", "-k", "uvicorn.workers.UvicornH11Worker", "--config", "/app/gunicorn_config.py", "api:app"]
