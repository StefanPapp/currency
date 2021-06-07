FROM python:3.10.0b1-slim-buster

RUN apt upgrade && apt update

COPY . /opt

RUN pip install /opt/currency_converter_service-0.2-py3-none-any.whl
