FROM python:3.8

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN apt-get -y update && apt-get -y install netcat \

WORKDIR /app
COPY requirements.txt .

RUN pip install --upgrade pip & pip install -r requirements.txt

COPY . .


