FROM python:3.11-slim

ENV PIP_NO_CACHE_DIR=0
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update -y && apt-get install -y gcc portaudio19-dev python3-dev build-essential libpq-dev pkg-config ffmpeg && apt-get clean

COPY ./requirements.txt /app/
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]
