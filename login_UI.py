from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

w = Tk()
w.geometry("200x100")

# username and password variables
userStr = StringVar()
passStr = StringVar()

# authentication variable
auth = BooleanVar()

auth = False

def loginPressed():
    if auth == False: 
      messagebox.showinfo("Alert!","Login Failed!")
    else:
      messagebox.showinfo("Alert!","Login Successful!")


# username entry field
userLabel = Label(text="Username")
userLabel.grid(row=0, column=0)
userEntry = Entry(bd=2, textvariable=userStr)
userEntry.grid(row=0, column=1)

# password entry field
passLabel = Label(text="Password")
passLabel.grid(row=1, column=0)
passEntry = Entry(bd=2, show="*", textvariable=passStr)
passEntry.grid(row=1, column=1)

# login button
loginButton = Button(master=w, text="OK",command=loginPressed)
loginButton.grid(row=2, column=1, pady=10)

w.mainloop()
