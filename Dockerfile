FROM python:3.9-alpine3.14

LABEL Maintainer="feri.harsanto@gmail.com"

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT ["/usr/local/bin/python3", "-u", "main.py"]