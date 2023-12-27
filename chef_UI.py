from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image

window = tk.Tk()

window.title("Chef Page")

window.geometry("800x210+500+100")
window.resizable(False, False)



welcomeText = Label(window, text="Welcome, Username", font=("Sans-serif", 18))
welcomeText.grid(padx= 40, sticky="w")

logo = tk.PhotoImage(file="logoSVG.png")

#resize the image to fit the screen better
logo_resize = logo.subsample(2, 2)

smallLogo = Label(window, image=logo_resize)
smallLogo.place(x=90, y=50)

ButtonProfile = tk.Button(window, width=40, text="Profile", font=("Sans-serif", 16))

ButtonOrders = tk.Button(window, text="Orders", width=40, font=("Sans-serif", 16))

# Exit function for the exit button
def Exit ():
    window.quit()

ButtonExit = tk.Button(window, text="Exit", width=40, command=Exit, font=("Sans-serif", 16))

Grid.rowconfigure(window, 0, weight=0)
Grid.columnconfigure(window, 0, weight=2)


ButtonProfile.grid(row=0, column=1, sticky="E")
ButtonOrders.grid(row=2, column=1, sticky="E")
ButtonExit.grid(row=4, column=1, sticky="E")

window.mainloop()
