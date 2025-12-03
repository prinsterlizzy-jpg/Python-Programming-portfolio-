receivers = ["user1@gmail.com", "user2@yahoo.com", "user3@outlook.com"]

for email in receivers:
    msg["To"] = email
    server.sendmail(sender, email, msg.as_string())
