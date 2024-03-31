import smtplib, ssl
import os

def email_conn(message):
    host = "smtp.gmail.com"
    port = 465

    username = "atwenefour21@gmail.com"
    password = os.getenv("PASSWORD_PORTFOLIO_APP")

    receiver = "atwenefour21@gmail.com"
    context = ssl.create_default_context()

    message = message.encode('utf-8')
    
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)