# syntax=docker/dockerfile:1
FROM python:3.11-slim-buster

WORKDIR /app
COPY . /app

RUN pip3 install -r requirements.txt

EXPOSE 5000
ENV FLASK_APP=app.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
