import smtplib, ssl

def email_conn(message):
    host = "smtp.gmail.com"
    port = 465

    username = "atwenefour21@gmail.com"
    password = "wvdr godl rhot pmkg"

    receiver = "atwenefour21@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)