FROM python:3.7-alpine

WORKDIR .

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5021

COPY . .
ENTRYPOINT ["python", "app/producer.py", "echo 127.0.0.1 kafka-broker >> /etc/hosts"]