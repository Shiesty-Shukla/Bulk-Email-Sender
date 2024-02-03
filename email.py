import smtplib
import threading

def email():
    content = "example email stuff"
    mail = smtplib.SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()
    mail.login("your email", "your password")
    mail.sendmail("your email", "reciever", content)
    mail.close()
    
labels = []

for i in range(10): #able to change number of loops to your prefence
    t1 = threading.Thread(target=email)
    t1.start()
    labels.append(t1)

for thread in labels:
    thread.join()
