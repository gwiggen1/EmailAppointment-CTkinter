import smtplib
#ssl for security
import ssl
from email.message import EmailMessage
from tkinter import *
import customtkinter as ck
from tkcalendar import Calendar

#Set Color Theme
ck.set_appearance_mode("dark")
ck.set_default_color_theme("green")

#Define Sender
#Must 2 factor authenticate with google and get google app pass
email_sender= 'youremail@gmail.com'
email_pass = 'googleapppassword'

#Define Window
root = ck.CTk()
root.title("Schedule Appointment")
root.geometry('450x450')
root.resizable(height=False,width=False)

#Define Email appointment function
def appt(email_receiver):
    ur_appt.configure(text = "Your Appointment is:" +'\n'+ date.get_date())
    subject = 'Appointment Date:'
    body = fname.get() + " has scheduled an appointment on " + date.get_date()
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)
    context=ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_pass)
        smtp.sendmail(email_sender,email_receiver,em.as_string())
    

#Creates Headings
head = ck.CTkLabel(root, text ="Please Select an Appointment",font=('n',18))
head.place(relx=.7,rely=.1,anchor=CENTER)

#Creates Calendar Object
date = Calendar(root, selectmode = 'day', year=2020,month=5,day=22)
date.place(relx=.7,rely=.4,width=300, height =250,anchor=CENTER)

#Email Entry
elabel = ck.CTkLabel(root, text = "Email:", font=('n',16))
elabel.place(relx=.225,rely=.425,anchor=CENTER)

femail = ck.CTkEntry(root)
femail.place(relx=.225,rely=.5,anchor=CENTER)

#Full Name Entry
nlabel = ck.CTkLabel(root, text="Name:", font=('n',16))
nlabel.place(relx=.225,rely=.225,anchor=CENTER)

fname = ck.CTkEntry(root)
fname.place(relx=.225,rely=.3,anchor=CENTER)

#Creates Button
button = ck.CTkButton(root, text = "Set Appointment", command= lambda: appt(femail.get()))
button.place(relx=.7,rely=.7, anchor=CENTER)

#Applies the appt() in label
ur_appt = ck.CTkLabel(root, text ="" , font=('n',16))
ur_appt.place(relx=.7,rely=.82,anchor=CENTER)

root.mainloop()