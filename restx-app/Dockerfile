FROM python:3.9-alpine

EXPOSE 5000

COPY . /src

WORKDIR /src

RUN ["pip", "install", "-r", "requirements.txt"]

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]