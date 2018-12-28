FROM python:3.7.2-alpine


MAINTAINER Yaroslav <hello@unimarijo.com>

ADD . data/
WORKDIR data
ENV PYTHONPATH "$PYTHONPATH:$(pwd)"

RUN apk add --update build-base
RUN pip install -r requirements/requirements.txt

ENTRYPOINT python run.py
