# Seif

import tkinter as tk
from tkinter import ttk, messagebox
import os, requests


class ChefPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Orders Page")
        self.master.geometry("340x300+760+100")
        self.master.resizable(False, False)

        self.style = ttk.Style()
        self.style.configure("TFrame", padding=10)
        self.style.configure("TLabel", font=("Sans-serif", 16))
        self.style.configure("TButton", padding=5, font=("Sans-serif", 16))

        self.create_widgets()

    def create_widgets(self):
        # Main frame
        self.frm = ttk.Frame(self.master)
        self.frm.grid(
            row=0, column=0, padx=10, pady=10, sticky=(tk.N, tk.S, tk.E, tk.W)
        )

        # Title label
        ttk.Label(self.frm, text="Food Orders", style="TLabel").grid(
            column=0, row=0, columnspan=2, pady=10
        )

        # Listbox to display food orders
        self.orders_listbox = tk.Listbox(self.frm, height=10, selectmode=tk.SINGLE)
        self.orders_listbox.grid(
            column=0, row=1, columnspan=2, pady=10, sticky=(tk.N, tk.S, tk.E, tk.W)
        )

        # Example data for food orders (replace this with your actual data)
        get_all_orders_URL = os.getenv(
            "get-all-orders", "http://localhost:8080/get-all-orders"
        )
        data = requests.get(get_all_orders_URL)
        ordersList = data.json()
        food_orders = []

        for order in ordersList:
            order_id = order["orderId"]
            items = order["items"]

            order_string = f"{order_id}: "

            item_names = [item["name"] for item in items]
            order_string += ", ".join(item_names)
            food_orders.append(order_string)

        for order in food_orders:
            self.orders_listbox.insert(tk.END, order)

        # Button to complete selected order
        ttk.Button(
            self.frm,
            text="Complete Order",
            command=self.complete_order,
            style="TButton",
        ).grid(column=0, row=2, pady=10, sticky=(tk.E, tk.W))

        # Button to quit the application
        ttk.Button(
            self.frm, text="Quit", command=self.master.destroy, style="TButton"
        ).grid(column=1, row=2, pady=10, sticky=(tk.E, tk.W))

        # Set column and row weights
        self.frm.columnconfigure(0, weight=1)
        self.frm.rowconfigure(1, weight=1)

    def complete_order(self):
        selected_item = self.orders_listbox.curselection()

        if selected_item:
            selected_item_text = self.orders_listbox.get(selected_item)
            parts = str(selected_item_text).split(":", 1)
            order_id = int(parts[0])

            try:
                myJson = {"orderId": order_id}
                delete_order_URL = os.getenv(
                    "delete-order", "http://localhost:8080/delete-order"
                )
                requests.delete(delete_order_URL, json=myJson)

                self.orders_listbox.delete(selected_item)

            except requests.RequestException as e:
                messagebox.showerror("Error:", e)


if __name__ == "__main__":
    root = tk.Tk()
    app = ChefPage(root)
    root.mainloop()
