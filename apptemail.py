import smtplib
#ssl for security
import ssl
from email.message import EmailMessage
from tkinter import *
import customtkinter as ck
from tkcalendar import Calendar
import datetime

#Set Todays date
today = datetime.date.today()

#Set Color Theme
ck.set_appearance_mode("dark")
ck.set_default_color_theme("green")

#Define Sender
#Must 2 factor authenticate with google and get google app pass
email_sender= 'youremail@gmail.com'
email_pass = 'yourapppassword'

#Define Window
root = ck.CTk()
root.title("Schedule Appointment")
root.geometry('525x525')
root.resizable(height=False,width=False)

#Define Email appointment function
def appt(email_receiver):
    ur_appt.configure(text = "Your Appointment is:" +'\n'+ date.get_date() + '\n' + "@" +appt_time)
    subject = 'Appointment Date:'
    body = fname.get() + " has scheduled an appointment on " + date.get_date() + " at " + appt_time
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

#Creates Calendar Object with today's date selected
date = Calendar(root, selectmode = 'day', year=today.year,month=today.month,day=today.day)
date.place(relx=.7,rely=.4,width=300, height =250,anchor=CENTER)

#Create Time Label and Selector
timlabel = ck.CTkLabel(root, text = "Time:", font=('n',16))
timlabel.place(relx=.225,rely=.515,anchor=CENTER)

timespinhr = Spinbox(root,from_=1, to=12)
timespinhr.place(relx=.135,rely=.560,width = 50,anchor=CENTER)
timespinmin = Spinbox(root,from_=00, to=60,format="%02.0f")
timespinmin.place(relx=.210,rely=.560,width =50, anchor=CENTER)

#Dropdown Box
drop_box = ck.CTkOptionMenu(root, values=["AM","PM"])
drop_box.place(relx=.310,rely=.560,width =75,height = 20, anchor=CENTER)

#Email Entry
elabel = ck.CTkLabel(root, text = "Email:", font=('n',16))
elabel.place(relx=.225,rely=.375,anchor=CENTER)

femail = ck.CTkEntry(root)
femail.place(relx=.225,rely=.450,anchor=CENTER)

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

#Appointment time
appt_time = timespinhr.get() + ":" + timespinmin.get() + drop_box.get()

root.mainloop()
