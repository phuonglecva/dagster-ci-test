FROM python:3.10
WORKDIR /opt/dagster/app

RUN apt-get update && \
    apt-get install -y git && \
    apt-get install -y default-jre 
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .