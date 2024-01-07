# Guilherme

from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image

w = Tk()

w.title("Login Page")

w.geometry("600x210+600+100")
w.resizable(False, False)

welcomeText = Label(w, text="Welcome", font=("Sans-serif", 18))
welcomeText.grid(padx=101, sticky="w")

# gets the relative image paths
main_dir = os.path.dirname(__file__)
logo_rel = "../images/logoSVG.png"
user_rel = "../images/user.png"
logo_path = os.path.join(main_dir, logo_rel)
user_path = os.path.join (main_dir, user_rel)

logo = tk.PhotoImage(file=logo_path)

# resize the image to fit the screen better
logo_resize = logo.subsample(2, 2)

smallLogo = Label(w, image=logo_resize)
smallLogo.place(x=90, y=50)

# username and password variables
userStr = StringVar()
passStr = StringVar()

# authentication variable
auth = BooleanVar()

auth = False


def loginPressed():
    if auth == False:
        messagebox.showinfo("Alert!", "Login Failed!")
    else:
        messagebox.showinfo("Alert!", "Login Successful!")


# username entry field
userLabel = Label(text="Username:", font=("Sans-serif", 12))
userLabel.grid(row=2, column=1)
userEntry = Entry(bd=2, textvariable=userStr)
userEntry.grid(row=2, column=2)

# password entry field
passLabel = Label(text="Password:", font=("Sans-serif", 12))
passLabel.grid(row=3, column=1)
passEntry = Entry(bd=2, show="*", textvariable=passStr)
passEntry.grid(row=3, column=2)

# login button
loginButton = Button(master=w, text="OK", command=loginPressed, font=("Sans-serif", 16))
loginButton.grid(row=4, column=2, pady=10)

w.mainloop()
