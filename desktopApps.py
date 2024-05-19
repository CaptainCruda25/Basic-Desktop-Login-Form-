# Desktop App Project

#from tkinter import *
#from tkinter.ttk import *
#import tkinter as tk
import tkinter
from tkinter import messagebox

root = tkinter.Tk()
root.title("Music School System")
root.geometry("650x550")
root.configure(bg = "#333333")
frame = tkinter.Frame(bg = "#333333")
root.iconphoto(False, tkinter.PhotoImage(file="eletricguitar.png"))


# Python Code

def Login():
    if (uname.get() != "") & (password.get() != ""):
        messagebox.showinfo(title = "Gitatero Music", message = "Login Successfully!")
    else:
        messagebox.showerror(title="Gitarero Music", message = "Account Doesn\'t Exist!")


# Creating Widgets

login = tkinter.Label(frame, text ="Login", font =("Arial Bold", 30), bg = "#333333") # Login Label
unamelabel = tkinter.Label(frame, text="Username:", font =("Arial Bold", 16), width=10, bg='#333333', fg ="#FFFFFF") # Username Label
passlabel = tkinter.Label(frame, text="Password:", font =("Arial Bold", 16),bg = '#333333', fg="#FFFFFF")
uname = tkinter.Entry(frame, text = "Username", font =("Arial Bold", 16),width=26) # Username EntryBox
password = tkinter.Entry(frame, text= "Password", show="*", font =("Arial Bold", 16), width=26) # Password Entry Box
loginbtn = tkinter.Button(frame, text = "Login", font =("Arial Bold", 16), bg ="green",command = Login) # Login Button
registerbtn = tkinter.Button(frame, text = "Register", font = ("Arial Bold", 16), bg = "Blue")


# Placing widgets on the screen

login.grid(row=0, column=0, columnspan=5, sticky= "news", pady=50)
unamelabel.grid(row=2, column=0, padx=50)
passlabel.grid(row=4, column=0,padx=50)
uname.grid(row=2, column=1, pady=10)
password.grid(row=4, column=1, pady=5)
loginbtn.grid(row=5, column=0, columnspan=3, pady=20)
registerbtn.grid(row = 5, column=1, columnspan=3)




frame.pack() # For responsiveness of the desktop app
root.mainloop() # To run the desktop app