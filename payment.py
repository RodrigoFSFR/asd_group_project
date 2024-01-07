import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class PaymentPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Payment Page")
        self.master.geometry("400x300")
        
        self.style = ttk.Style()
        self.style.configure("TFrame", padding=10)
        self.style.configure("TLabel", font=("Helvetica", 12))
        self.style.configure("TButton", padding=5, font=("Helvetica", 12))

        self.create_widgets()

    def create_widgets(self):
        # Main frame
        self.frm = ttk.Frame(self.master)
        self.frm.grid(row=0, column=0, padx=10, pady=10, sticky=(tk.N, tk.S, tk.E, tk.W))

        # Title label
        ttk.Label(self.frm, text="Enter Card Details", style="TLabel").grid(column=0, row=0, columnspan=2, pady=10)

        # Cardholder's Name label and entry
        ttk.Label(self.frm, text="Cardholder's Name:", style="TLabel").grid(column=0, row=1, pady=5, sticky=tk.E)
        self.cardholder_name_entry = ttk.Entry(self.frm)
        self.cardholder_name_entry.grid(column=1, row=1, pady=5, sticky=tk.W)

        # Card Number label and entry
        ttk.Label(self.frm, text="Card Number:", style="TLabel").grid(column=0, row=2, pady=5, sticky=tk.E)
        self.card_number_entry = ttk.Entry(self.frm, show="*")
        self.card_number_entry.grid(column=1, row=2, pady=5, sticky=tk.W)

        # Expiration Date label and entry
        ttk.Label(self.frm, text="Expiration Date (MM/YY):", style="TLabel").grid(column=0, row=3, pady=5, sticky=tk.E)
        self.expiration_date_entry = ttk.Entry(self.frm)
        self.expiration_date_entry.grid(column=1, row=3, pady=5, sticky=tk.W)

        # Process Payment button
        ttk.Button(self.frm, text="Process Payment", command=self.process_payment, style="TButton").grid(column=0, row=4, columnspan=2, pady=10)

        # Set column and row weights
        self.frm.columnconfigure(0, weight=1)
        self.frm.rowconfigure(4, weight=1)

    def process_payment(self):
        cardholder_name = self.cardholder_name_entry.get()
        card_number = self.card_number_entry.get()
        expiration_date = self.expiration_date_entry.get()

        # Basic validation (you should implement more robust validation)
        if not cardholder_name or not card_number or not expiration_date:
            messagebox.showerror("Error", "Please enter all card details.")
            return

        messagebox.showinfo("Payment Successful", "Payment processed successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PaymentPage(root)
    root.mainloop()
