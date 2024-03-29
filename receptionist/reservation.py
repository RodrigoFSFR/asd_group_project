# Rayen

from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
import tkinter as tk
from datetime import datetime
import requests, os

# In-memory reservation list
reservations = []


# Function to validate the time entry
def validate_time_entry():
    available_times = [
        "10:00",
        "11:00",
        "12:00",
        "13:00",
        "14:00",
        "15:00",
        "16:00",
        "17:00",
        "18:00",
        "19:00",
        "20:00",
        "21:00",
        "22:00",
    ]
    chosen_time = time_var.get()
    if chosen_time not in available_times:
        messagebox.showinfo("Invalid Time", "Please choose a valid time.")
        return False
    return True


def validate_people_entry():
    try:
        people = int(people_var.get())
        if 1 <= people <= 20:
            return True
        else:
            messagebox.showinfo(
                "Invalid Entry", "Number of people must be between 1 and 20."
            )
            return False
    except ValueError:
        messagebox.showinfo(
            "Invalid Entry", "Please enter a valid number for the number of people."
        )
        return False


def validate_date_entry():
    selected_date = date_entry.get_date()
    today = datetime.now().date()
    if selected_date < today:
        messagebox.showinfo(
            "Invalid Date", "Please choose a date today or in the future."
        )
        return False
    return True


def validate_phone_entry():
    phone = phone_entry.get()
    if not phone.isdigit():
        messagebox.showinfo(
            "Invalid Phone Number", "Please enter digits only for the phone number."
        )
        return False
    return True


def make_reservation(name, date, time, people, seating, phone):
    # Check if the chosen date and time slot is available in the in-memory list
    myRequest = {
        "name": name,
        "date": date,
        "time": time,
        "people": people,
        "phone": phone,
        "table": seating,
    }

    # Make the POST request to the API endpoint
    api_url = os.getenv("add-reservation", "http://localhost:8080/add-reservation")
    try:
        response = requests.post(api_url, json=myRequest)

        # Check if the request was successful
        if response.ok:
            messagebox.showinfo(
                "Reservation Successful", "Your reservation has been confirmed!"
            )
        else:
            messagebox.showinfo(
                "Reservation Failed",
                "This slot is already taken. Please choose another.",
            )
            return

    except requests.RequestException as e:
        messagebox.showerror("Error:", e)


def reserve_button_clicked():
    chosen_name = name_entry.get()
    chosen_date = date_entry.get_date().strftime("%Y-%m-%d")
    chosen_time = time_var.get()
    chosen_people = people_var.get()
    chosen_seating = seating_var.get()
    chosen_phone = phone_entry.get()

    # Check if any field is empty
    if not all(
        [
            chosen_name,
            chosen_date,
            chosen_time,
            chosen_people,
            chosen_seating,
            chosen_phone,
        ]
    ):
        messagebox.showinfo("Empty Fields", "Please fill in all fields.")
        return

    # Check if the selected date is valid
    if not validate_date_entry():
        return

    # Check if the time, people, phone number entries are valid
    if validate_time_entry() and validate_people_entry() and validate_phone_entry():
        make_reservation(
            chosen_name,
            chosen_date,
            chosen_time,
            int(chosen_people),
            int(chosen_seating),
            chosen_phone,
        )


# Create reservation window
reservation_window = Tk()
reservation_window.title("Make a Reservation")
reservation_window.geometry("270x400+800+100")
reservation_window.resizable(False, False)

# Add name entry, date picker, time entry, people entry, seating choice, and phone number entry
name_label = Label(reservation_window, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=10)
name_entry = Entry(reservation_window)
name_entry.grid(row=0, column=1, padx=10, pady=10)

phone_label = Label(reservation_window, text="Phone Number:")
phone_label.grid(row=1, column=0, padx=10, pady=10)
phone_entry = Entry(reservation_window)
phone_entry.grid(row=1, column=1, padx=10, pady=10)

date_label = Label(reservation_window, text="Select Date:")
date_label.grid(row=2, column=0, padx=10, pady=10)
date_entry = DateEntry(
    reservation_window,
    width=12,
    background="darkblue",
    foreground="white",
    borderwidth=2,
)
date_entry.grid(row=2, column=1, padx=10, pady=10)

time_label = Label(reservation_window, text="Select Time:")
time_label.grid(row=3, column=0, padx=10, pady=10)

# List of available times
available_times = [
    "10:00",
    "11:00",
    "12:00",
    "13:00",
    "14:00",
    "15:00",
    "16:00",
    "17:00",
    "18:00",
    "19:00",
    "20:00",
    "21:00",
    "22:00",
]
time_var = StringVar()
time_menu = OptionMenu(reservation_window, time_var, *available_times)
time_menu.grid(row=3, column=1, padx=10, pady=10)

people_label = Label(reservation_window, text="Number of People:")
people_label.grid(row=4, column=0, padx=10, pady=10)

# List of available number of people
people_list = list(range(1, 21))
people_var = StringVar()
people_menu = OptionMenu(reservation_window, people_var, *people_list)
people_menu.grid(row=4, column=1, padx=10, pady=10)

seating_label = Label(reservation_window, text="Table Number:")
seating_label.grid(row=5, column=0, padx=10, pady=10)
seating_var = IntVar()
seating_choices = list(range(1, 11))
seating_menu = OptionMenu(reservation_window, seating_var, *seating_choices)
seating_menu.grid(row=5, column=1, padx=10, pady=10)

reserve_button = Button(
    reservation_window, text="Reserve", command=reserve_button_clicked
)
reserve_button.grid(row=6, column=0, columnspan=2, pady=10)


# Returns to the main
def Exit():
    reservation_window.destroy()


ButtonExit = tk.Button(
    reservation_window, text="Exit", width=20, command=Exit, font=("Sans-serif", 16)
)
ButtonExit.grid(row=7, column=0, columnspan=2, pady=10)

reservation_window.mainloop()
