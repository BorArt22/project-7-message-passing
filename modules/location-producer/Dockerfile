FROM python:3.7-alpine

WORKDIR .

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5021

COPY . .
ENTRYPOINT ["python", "app/main.py"]