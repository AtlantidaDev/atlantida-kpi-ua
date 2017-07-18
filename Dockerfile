FROM python:latest

LABEL maintainer="Oleksandr Pikovets <pikovets.alexandr@gmail.com>"

COPY . /var/www
WORKDIR /var/www

RUN pip install --upgrade pip
RUN pip install -r config/requirements.txt

WORKDIR ./src
