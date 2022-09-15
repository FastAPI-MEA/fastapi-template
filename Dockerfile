# pull official base image
FROM python:3.9-slim-bullseye

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install necessary packages
RUN apt-get update \
    && apt-get -y install build-essential \
    && apt-get -y install libpq-dev gcc \
    && apt-get -y install netcat

COPY . .
# install pipenv and project dependencies
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile