FROM python:3.11-alpine

COPY . .

CMD [ "python", "send_gmail.py" ]