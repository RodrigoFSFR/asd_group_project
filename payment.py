import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class PaymentPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Payment Page")
        self.master.geometry("400x400")
        
        self.style = ttk.Style()
        self.style.configure("TFrame", padding=10)
        self.style.configure("TLabel", font=("Helvetica", 12))
        self.style.configure("TButton", padding=5, font=("Helvetica", 12))

        self.ordered_items = []

        self.create_widgets()

    def create_widgets(self):
        # Main frame
        self.frm = ttk.Frame(self.master)
        self.frm.grid(row=0, column=0, padx=10, pady=10, sticky=(tk.N, tk.S, tk.E, tk.W))

        # Ordered Items label and listbox
        ttk.Label(self.frm, text="Ordered Items:", style="TLabel").grid(column=0, row=0, columnspan=2, pady=10)
        self.order_listbox = tk.Listbox(self.frm, height=5)
        self.order_listbox.grid(column=0, row=1, columnspan=2, pady=5, sticky=(tk.N, tk.S, tk.E, tk.W))

        # Staff Promo Code label and entry
        ttk.Label(self.frm, text="Staff Promo Code:", style="TLabel").grid(column=0, row=2, pady=5, sticky=tk.E)
        self.promo_code_entry = ttk.Entry(self.frm)
        self.promo_code_entry.grid(column=1, row=2, pady=5, sticky=tk.W)

        # Pay by Cash button
        ttk.Button(self.frm, text="Pay by Cash", command=self.pay_by_cash, style="TButton").grid(column=0, row=3, pady=10)

        # Pay by Card button
        ttk.Button(self.frm, text="Pay by Card", command=self.pay_by_card, style="TButton").grid(column=1, row=3, pady=10)

        # Set column and row weights
        self.frm.columnconfigure(0, weight=1)
        self.frm.columnconfigure(1, weight=1)
        self.frm.rowconfigure(3, weight=1)

    def add_to_order(self, item):
        self.ordered_items.append(item)
        self.order_listbox.insert(tk.END, item)

    def pay_by_cash(self):
        self.process_payment("Cash")

    def pay_by_card(self):
        promo_code = self.promo_code_entry.get()
        if promo_code.lower() == "staff123":  # Replace with your actual staff promo code
            self.process_payment("Card (Staff)")
        else:
            self.process_payment("Card")

    def process_payment(self, payment_method):
        # Payment processing logic here

        # Display a success message with the ordered items and payment method
        ordered_items_str = "\n".join(self.ordered_items)
        messagebox.showinfo("Payment Successful", f"Payment processed successfully!\nOrdered Items:\n{ordered_items_str}\nPayment Method: {payment_method}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PaymentPage(root)
    app.add_to_order("Pizza")
    app.add_to_order("Burger")
    root.mainloop()
