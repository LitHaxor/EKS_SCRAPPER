FROM python:3.7-slim

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt --no-cache-dir




