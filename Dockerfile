FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir /app
WORKDIR /app

RUN pip install --upgrade pip
COPY requirements/dev.txt .
RUN pip install --no-cache-dir --upgrade -r /app/dev.txt

COPY . .