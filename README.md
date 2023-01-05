# Email-Appointment-CTkinter
## Description
This CTkinter GUI app allows you to send a appointment confirmation email with the date of the appointment selected.
## Requirements
```
pip install Tkinter

pip install CTkinter

pip install TkCalendar
```
Must Enable 2 Factor Authentication With Google Account and Generate an [App Password](https://support.google.com/mail/answer/185833?hl=en-GB)

## Your Setup

You must change this for the email to send:

```
email_sender= 'youremail@gmail.com'  #Enter your email here
email_pass = 'yourapppassword'       #Enter your app password here
```
## Calendar GUI 


![Emailappoint final](https://user-images.githubusercontent.com/121186555/210678583-4ce4eb86-74b8-4319-96ad-96577514de54.PNG)


## Email Received

![Eappointmentfin](https://user-images.githubusercontent.com/121186555/210678657-e62496af-9295-4818-93cd-4ef2b97289f6.PNG)

## Packaging

When trying to package a CTkinter GUI Program as an executable I recommend using auto-py-to-exe (a bit more user friendly than pyinstaller)

To Install auto-py-to-exe:

```
pip install auto-py-to-exe
```

Open auto-py-to-exe:


```
python -m auto_py_to_exe
```


This should open auto-py-to-exe. Once inside you must use One Directory (`--onedir`[^1]) and Add Folders customtkinter, babel, TkCalendar in Additional Files (`--add-data`[^1])

Here is some additional help/explanation from the devs:

[CTK Packaging Help](https://github.com/TomSchimansky/CustomTkinter/wiki/Packaging)

[^1]: If you do not do this your executable will not run. (These are the commands if using pyinstaller)
