from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image

window = tk.Tk()

window.title("Manager Page")

window.geometry("800x210+500+100")
window.resizable(False, False)


welcomeText = Label(window, text="Welcome, Username", font=("Sans-serif", 18))
welcomeText.grid(padx=40, sticky="w")

logo = tk.PhotoImage(file=".\images\logoSVG.png")

# resize the image to fit the screen better
logo_resize = logo.subsample(2, 2)

smallLogo = Label(window, image=logo_resize)
smallLogo.place(x=90, y=50)


def profileWindow():
    profileWindow = Toplevel(window)
    profileWindow.title("Profile Page")

    profileWindow.geometry("410x500+700+100")
    profileWindow.resizable(False, False)

    profileWindow.columnconfigure(0, weight=1)
    profileWindow.rowconfigure(0, weight=0)

    userLogo = tk.PhotoImage(file=".\images\user.png")
    label = Label(profileWindow, image=userLogo)
    label.img = userLogo
    label.grid(row=1, column=0)

    jobText = Label(profileWindow, text="Job Title", font=("Sans-serif", 18))
    jobText.grid(row=2, column=0, sticky="n")

    usernameText = Label(profileWindow, text="Username", font=("Sans-serif", 18))
    usernameText.grid(row=3, column=0, sticky="n")

    idText = Label(profileWindow, text="ID Number: ID", font=("Sans-serif", 18))
    idText.grid(row=4, column=0, sticky="n")

    def Back():
        profileWindow.destroy()

    ButtonExit = tk.Button(
        profileWindow, text="Back", width=10, command=Back, font=("Sans-serif", 16)
    )
    ButtonExit.grid(row=5, column=0, sticky="n")


ButtonProfile = tk.Button(
    window, width=40, command=profileWindow, text="Profile", font=("Sans-serif", 16)
)


def openManageStaff():
    window.destroy()
    import asd_group_project.manager.manageStaff as manageStaff


ButtonManageStaff = tk.Button(
    window,
    width=40,
    text="Manage Staff",
    command=openManageStaff,
    font=("Sans-serif", 16),
)
ButtonOrders = tk.Button(window, text="Orders", width=40, font=("Sans-serif", 16))


def openReservation():
    window.destroy()
    import asd_group_project.receptionist.reservation as reservation


ButtonReservations = tk.Button(
    window,
    text="Reservations",
    width=40,
    font=("Sans-serif", 16),
    command=openReservation,
)


# Exit function for the exit button
def Exit():
    window.quit()


ButtonExit = tk.Button(
    window, text="Exit", width=40, command=Exit, font=("Sans-serif", 16)
)


ButtonProfile.grid(row=0, column=1, sticky="E")
ButtonManageStaff.grid(row=1, column=1, sticky="E")
ButtonOrders.grid(row=2, column=1, sticky="E")
ButtonReservations.grid(row=3, column=1, sticky="E")
ButtonExit.grid(row=4, column=1, sticky="E")

window.mainloop()