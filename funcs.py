import random
import smtplib
from smtplib import *
import datetime as dt


my_mail = "pradyublog@gmail.com"
my_password = "guwafcljmrgtpymu"
# sivajivaailajelabi

#function for generating random otp
def generate_otp():
    otp=""
    for i in range(0,4):
        random_num=str(random.randint(0,9))
        otp+=random_num
    return otp

#function for sending the otp to the users
def send_otp(reciever,msg):

    # creating a smtp obj (establishing the connection)
    connection = SMTP("smtp.gmail.com", 587)
    # securing the connection
    connection.starttls()
    # logging into our mail
    connection.login(user=my_mail, password=my_password)
    # sending the mail
    connection.sendmail(from_addr=my_mail, to_addrs=reciever, msg=f"Subject:Verification of OTP\n\nYour OTP for Pradyu's Blog is {msg} Do not share it with anyone")
    # closing the conection ie obj file
    connection.close()

def send_email(name, email, phone, message,):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_mail,my_password)
        connection.sendmail(my_mail, my_mail, email_message)

def get_time():
    time=dt.datetime.utcnow() + dt.timedelta(hours=5, minutes=30)
    hours=time.hour
    if hours >= 4 and hours <= 11:
        return "Good Morning"
    elif hours >= 12 and hours <= 15:
        return "Good Afternoon"
    elif hours >= 16 and hours <= 19:
        return "Good Evening"
    elif hours >= 20 or hours <= 3:
        return "Good Night"
