# syntax=docker/dockerfile:1
FROM python:3.9.7
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip3 install --upgrade pip
COPY . .
RUN pip3 install -r requirements.txt