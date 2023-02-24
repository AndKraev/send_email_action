FROM python:3.11-alpine

WORKDIR /app

COPY . .

CMD [ "python", "/cmd/send_gmail.py" ]