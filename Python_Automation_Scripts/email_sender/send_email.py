import smtplib
from email.mime.text import MIMEText

def send_email(subject, message, to_email):
    sender = "YOUR_EMAIL@gmail.com"
    password = "YOUR_APP_PASSWORD"  # Gmail App Password

    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = to_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.send_message(msg)

    print("Email sent successfully!")

# Example
send_email("Automation Test", "Hello, this is an automated email!", "recipient@example.com")
