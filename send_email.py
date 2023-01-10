import smtplib, ssl
import os

key = os.getenv('PyEmailKey')
def send_mail(message):
    host = "smtp.gmail.com"
    port = 465
    username = "allalexandersouth@gmail.com"
    password = os.getenv("Python_Email_Key")
    password1 = password
    receiver = "allalexandersouth@gmail.com"
    contexti = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=contexti) as server:
        server.login(username, password1)
        server.sendmail(username, receiver, message)


if __name__ == "__main__":
    print(key)
    print (os.environ)