from email_automation.html_email import send_html_email

send_html_email(
    "Welcome!",
    "<h2>Hello!</h2><p>This is an automated email.</p>",
    "recipient@gmail.com"
)
