FROM python:3.11-alpine

WORKDIR /app

COPY . .

CMD [ "python", "/app/send_gmail.py" ]