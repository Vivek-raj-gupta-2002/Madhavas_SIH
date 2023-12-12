FROM python:3.10.11
ENV PYTHONUNBUFFERED 1

WORKDIR /code


COPY requriments.txt /code/

RUN pip install --upgrade pip && pip install -r requriments.txt

COPY . /code/