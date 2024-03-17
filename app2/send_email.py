import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "atwenefour21@gmail.com"
password = "wvdr godl rhot pmkg"

receiver = "atwenefour21@gmail.com"
context = ssl.create_default_context()

message = """ Hi, How are you?
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)

