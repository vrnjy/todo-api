FROM python:3.11.2-alpine3.17

WORKDIR /todo-api

COPY ./requirements.txt /todo-api/

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /todo-api/

CMD ["python", "app.py"]