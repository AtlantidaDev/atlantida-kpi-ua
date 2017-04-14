FROM python:2.7

MAINTAINER Oleksandr Pikovets <pikovets.alexandr@gmail.com>

ENV PYTHONUNBUFFERED 1

VOLUME ./src:/src

RUN mkdir /config
ADD /config/requirements.pip /config/

RUN pip install -r /config/requirements.pip

WORKDIR /src
