FROM python:3.11-alpine

WORKDIR /app

COPY . .

CMD [ "python", "./send_gmail.py" ]