import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_bulk_email(sender_email, password, recipients, subject, body):
    # Connect to Gmail SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)

    for recipient in recipients:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        server.sendmail(sender_email, recipient, msg.as_string())
        print(f"Email sent to {recipient}")

    server.quit()
