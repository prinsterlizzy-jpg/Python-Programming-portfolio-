<!-- PROJECT LOGO -->
<p align="center">
  <img src="<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/1d8d8148-3e5a-4624-bdc1-1a8561b19145" />
" width="120"/>
</p>

<h1 align="center">Python Automation Scripts</h1>

<p align="center">
  A powerful collection of automation scripts written in Python — for emails, file handling, web tasks, bulk messaging, and everyday workflow automation.
</p>

---

## 🚀 Features

✔ Send **HTML emails**  
✔ Send **emails with attachments**  
✔ **Bulk email** sender (multiple recipients)  
✔ File automation (rename, organize, clean folders)  
✔ Web automation with Selenium  
✔ API integration templates  
✔ Task scheduling examples  
✔ Logging & error handling

---

## 🏷️ Badges

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.10+-blue">
  <img src="https://img.shields.io/badge/Automation-Scripts-brightgreen">
  <img src="https://img.shields.io/badge/Status-Active-success">
  <img src="https://img.shields.io/badge/License-MIT-yellow">
</p>

---

## 📂 Project Structure
python-automation-scripts/
│
├── email_sender/
│   ├── html_email.py
│   ├── attachments.py
│   └── bulk_sender.py
│
├── file_automation/
│   ├── rename_files.py
│   ├── organize_folders.py
│   └── delete_temp_files.py
│
├── web_automation/
│   ├── selenium_login.py
│   └── scrape_data.py
│
├── utils/
│   ├── logger.py
│   └── settings.py
│
└── README.md
---

# 📧 Email Automation Examples

### ✅ 1. Send HTML Email

```python
import smtplib
from email.mime.text import MIMEText

sender = "your_email@gmail.com"
password = "your_app_password"
receiver = "recipient@example.com"

html = """
<h2 style='color:#4CAF50;'>Automation Email</h2>
<p>This is an <b>HTML email</b> sent using Python.</p>
"""

msg = MIMEText(html, "html")
msg["Subject"] = "HTML Email Test"
msg["From"] = sender
msg["To"] = receiver

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, msg.as_string())

print("Email sent!")

2. Send Email With Attachment

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

sender = "your_email@gmail.com"
password = "your_app_password"
receiver = "recipient@example.com"

msg = MIMEMultipart()
msg["Subject"] = "Email With Attachment"
msg["From"] = sender
msg["To"] = receiver

# email body
msg.attach(MIMEText("Please find the attached file.", "plain"))

# attach file
file_path = "document.pdf"
attachment = open(file_path, "rb")

part = MIMEBase("application", "octet-stream")
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header("Content-Disposition", f"attachment; filename={file_path}")

msg.attach(part)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, msg.as_string())

print("Attachment sent!")

📨3. Bulk Email Sender (Multiple People)
receivers = ["user1@gmail.com", "user2@yahoo.com", "user3@outlook.com"]

for email in receivers:
    msg["To"] = email
    server.sendmail(sender, email, msg.as_string())

⚙️ Installation
git clone https://github.com/prinsterlizzy-jpg/python-automation-scripts.git
cd python-automation-scripts
pip install -r requirements.txt

🧠 Requirements
smtplib
email
python-dotenv
selenium
requests

🤝 Contributing

Contributions are welcome!
You can submit a pull request or open an issue.

📄 License

This project is licensed under the MIT License.

⭐ Support

If you find this useful, kindly star the repository ⭐ to support the project.


