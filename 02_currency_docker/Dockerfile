FROM python:3.10.0b1-slim-buster

RUN apt upgrade && apt update

COPY . /opt

RUN pip install /opt/currency_converter-0.1-py3-none-any.whl
