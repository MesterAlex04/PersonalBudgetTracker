from tkinter import *
from tkinter.ttk import *
import re


registerWindow=Tk()
warningWindow = Tk()
warningWindow.geometry("200x200")
wrng = Label(warningWindow,text="Password must contain at least 8 letters, one number, one special character, one uppercase letter, one lowercase letter. Spaces are not allowed")
warningWindow.title("Warning!")
usrName = StringVar()
passw = StringVar()
eMail = StringVar()
phnNr = StringVar()

def confirm():
    username = usrName.get()
    password = passw.get()
    email = eMail.get
    phoneNumber = phnNr.get()
    if(len(password)<8 or 
       not re.search(r'[A-Z]', password) or
       not re.search(r'[a-z]',password) or
       not re.search(r'\d', password) or
       not re.search(r'!@#$%^&', password) or
       ' ' in password):
        warningWindow.deiconify()
    else:
        warningWindow.withdraw()
    usrName.set("")
    passw.set("")
    eMail.set("")
    phnNr.set("")
    


def center_window(window):
    window.update_idletasks()
    width =window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x=(screen_width-width)//2
    y=(screen_height-height)//2
    window.geometry(f"{width}x{height}+{x}+{y}")

def open_new_window():
    newWindow = Toplevel(registerWindow)
    newWindow.title("New window")
    newWindow.geometry("250x1500")
    



username = Entry(registerWindow)
password = Entry(registerWindow,textvariable = passw,show="*")
email = Entry(registerWindow)
phoneNumber = Entry(registerWindow)
confirmation = Button(registerWindow,command=confirm)
cancel = Button(registerWindow)




registerWindow.geometry("800x600")
registerWindow.title("Register Window")
center_window(registerWindow)
center_window(warningWindow)
registerWindow.mainloop()

warningWindow.withdraw()