FROM python:3.9-alpine

COPY . /app
WORKDIR /app

EXPOSE 5000

RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "app.py" ]