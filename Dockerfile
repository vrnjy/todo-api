FROM python:3.11.2-alpine3.17

ADD . /todo-api
WORKDIR /todo-api
RUN pip install -r requirements.txt