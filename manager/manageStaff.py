from tkinter import *
import tkinter as tk
from tkinter import messagebox
import requests, os

window = Tk()
window.title("Manage Staff")
window.geometry("270x600+800+100")
window.resizable(True, True)

get_staff_url = os.getenv("get-all-staff", "http://localhost:8080/get-all-staff")
delete_staff_url = os.getenv("delete-staff", "http://localhost:8080/delete-staff")


def deleteStaff(staffMember):
    myRequest = {
        "staffId": staffMember.get("id"),
    }

    try:
        response = requests.delete(delete_staff_url, json=myRequest)
        # Check if the request was successful
        if not (response.ok):
            messagebox.showerror("Failed", "Could not delete staff member")

    except requests.RequestException as e:
        messagebox.showerror("Error:", e)


def getStaffList():
    global staffList

    try:
        response = requests.get(get_staff_url)
        # deleteStaff(response.json()[0]["staffId"])

        # Check if the request was successful
        if not (response.ok):
            # messagebox.showinfo("Success", response.json()[0]["name"])
            messagebox.showerror("Failed", "Could not retrieve staff list")
            return

        staffList = response.json()

    except requests.RequestException as e:
        messagebox.showerror("Error:", e)
    return


getStaffList()


# Function to display the staff list
def displayStaffList():
    # Create a Text widget to display the staff list
    staffListText = Text(window, height=20, width=30)
    staffListText.grid(row=0, column=0, columnspan=2, pady=10)

    # Insert each staff member into the Text widget
    for staffMember in staffList:
        if "position" in staffMember:
            staffListText.insert(
                END, f"{staffMember['name']} ({staffMember['position']})\n"
            )
        else:
            staffListText.insert(END, f"{staffMember['name']}\n")

        # Add a button to delete the staff member
        deleteButton = Button(
            window,
            text="Delete",
            command=lambda staffMember=staffMember: deleteStaff(staffMember),
        )
        deleteButton.grid(row=staffList.index(staffMember) + 1, column=1, padx=5)

        # Add a label for the staff member's name
        nameLabel = Label(window, text=staffMember["name"])
        nameLabel.grid(row=staffList.index(staffMember) + 1, column=0, padx=5)

# Create a button to display the staff list
ButtonDisplayStaffList = tk.Button(
    window,
    text="Display Staff List",
    width=21,
    command=displayStaffList,
    font=("Sans-serif", 16),
)
ButtonDisplayStaffList.grid(row=6, column=0, columnspan=2, pady=10)


# Exit function for the exit button
def Exit():
    window.quit()


ButtonExit = tk.Button(
    window, text="Exit", width=21, command=Exit, font=("Sans-serif", 16)
)

ButtonExit.grid(row=7, column=0, columnspan=2, padx=4)

window.mainloop()
