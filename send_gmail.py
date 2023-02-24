import os
import smtplib


def send_email(
        user: str, pwd: str, recipient: [str | list[str]], subject: str, body: str
) -> None:
    print(f"user: {user}")
    print(f"pwd: {pwd}")

    from_ = user
    to = recipient if isinstance(recipient, list) else [recipient]
    subject = subject
    text = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (from_, ", ".join(to), subject, text)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(user, pwd)
    server.sendmail(from_, to, message)
    server.close()
    print('Email has been successfully sent.')


if __name__ == "__main__":
    send_email(
        user=os.getenv("USERNAME"),
        pwd=os.getenv("PASSWORD"),
        recipient=os.getenv("RECIPIENT"),
        subject=os.getenv("SUBJECT"),
        body=os.getenv("BODY")
    )
