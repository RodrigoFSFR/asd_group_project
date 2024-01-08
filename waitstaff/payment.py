# Seif

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os, requests


class PaymentPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Payment Page")
        self.master.geometry("400x400")

        self.style = ttk.Style()
        self.style.configure("TFrame", padding=10)
        self.style.configure("TLabel", font=("Sans-serif", 18))
        self.style.configure("TButton", padding=5, font=("Sans-serif", 16))

        self.ordered_items = []
        self.total = 0.0
        self.discount = 0.0

        self.create_widgets()

    def create_widgets(self):
        # Main frame
        self.frm = ttk.Frame(self.master)
        self.frm.grid(
            row=0, column=0, padx=10, pady=10, sticky=(tk.N, tk.S, tk.E, tk.W)
        )

        # Ordered Items label and listbox
        ttk.Label(self.frm, text="Ordered Items:", style="TLabel").grid(
            column=0, row=0, columnspan=2, pady=10
        )
        self.order_listbox = tk.Listbox(self.frm, height=5)
        self.order_listbox.grid(
            column=0, row=1, columnspan=2, pady=5, sticky=(tk.N, tk.S, tk.E, tk.W)
        )

        # Staff Promo Code label and entry
        ttk.Label(self.frm, text="Staff Promo Code:", style="TLabel").grid(
            column=0, row=2, pady=5, sticky=tk.E
        )
        self.promo_code_entry = ttk.Entry(self.frm)
        self.promo_code_entry.grid(column=1, row=2, pady=5, sticky=tk.W)
        
        # Order ID label, entry and button
        ttk.Label(self.frm, text="Order ID:", style="TLabel").grid(
            column=0, row=4, pady=5, sticky=tk.E
        )
        self.order_id_entry = ttk.Entry(self.frm)
        self.order_id_entry.grid(column=1, row=4, pady=3, sticky=tk.W)
        ttk.Button(
            self.frm, text="Get Order", command=self.get_order, style="TButton"
        ).grid(column=1, row=5)

        # Pay by Cash button
        ttk.Button(
            self.frm, text="Pay by Cash", command=self.pay_by_cash, style="TButton"
        ).grid(column=0, row=3, pady=10)

        # Pay by Card button
        ttk.Button(
            self.frm, text="Pay by Card", command=self.pay_by_card, style="TButton"
        ).grid(column=1, row=3, pady=10)

        # Set column and row weights
        self.frm.columnconfigure(0, weight=1)
        self.frm.columnconfigure(1, weight=1)
        self.frm.rowconfigure(3, weight=1)

    def add_to_order(self, item):
        self.ordered_items.append(item)
        self.order_listbox.insert(tk.END, item)

    def pay_by_cash(self):
        promo_code = self.promo_code_entry.get()
        if promo_code.lower() == os.getenv("promo-code", "staff123"):
            self.discount = 0.8 * self.total
            self.process_payment("Cash (Staff)", self.discount)
        else:
            self.process_payment("Cash", self.total)

    def pay_by_card(self):
        promo_code = self.promo_code_entry.get()
        if promo_code.lower() == os.getenv("promo-code", "staff123"):
            self.discount = 0.8 * self.total
            self.process_payment("Card (Staff)", self.discount)
        else:
            self.process_payment("Card", self.total)

    def get_order(self):
        orderId = int(self.order_id_entry.get())
        try:
            get_order_URL = os.getenv("get-order", "http://localhost:8080/get-order")
            body = {"orderId": orderId}
            data = requests.get(get_order_URL, json=body)
            order = data.json()["items"]
            for item in order:
                self.add_to_order(item["name"] + " | " + item["price"])
                price_str = item["price"].rstrip("£")
                price = float(price_str)
                self.total += price

        except requests.RequestException as e:
            messagebox.showerror("Error:", e)

    def process_payment(self, payment_method, total):
        # Payment processing logic here

        # Display a success message with the ordered items and payment method
        ordered_items_str = "\n".join(self.ordered_items)
        total_2 = "{:.2f}".format(total)
        messagebox.showinfo(
            "Payment Successful",
            f"Payment processed successfully!\nOrdered Items:"
            + f"\n{ordered_items_str}"
            + f"\nPayment Method: {payment_method}"
            + f"\nTotal: {total_2}£",
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = PaymentPage(root)
    root.mainloop()
