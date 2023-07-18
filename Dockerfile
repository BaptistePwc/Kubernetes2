FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

ADD requirements.txt main.py ./

RUN apt update && apt install python3-pip libmysqlclient-dev mysql-client -y && pip install -r requirements.txt

EXPOSE 8000

ENV MYSQL_HOST mysql-container

ENV MYSQL_ROOT_PASSWORD datascientest1234

CMD uvicorn main:server --host 0.0.0.0

