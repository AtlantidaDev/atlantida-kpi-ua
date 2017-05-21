FROM ubuntu:16.04

MAINTAINER Oleksandr Pikovets

ENV PORT=3000

COPY . /var/www
WORKDIR /var/www

RUN apt-get upgrade && apt-get update && apt-get install -y \
    python \
    python-pip

RUN pip install --upgrade pip
RUN pip install -r requirements.pip

EXPOSE $PORT

ENTRYPOINT ["python", "mannage.py", "runserver", "$PORT"]