FROM python:3.10.3-alpine

RUN mkdir /app
WORKDIR /app

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN adduser -D fapro

USER fapro

CMD ["python", "src/main.py"]

EXPOSE 8080
