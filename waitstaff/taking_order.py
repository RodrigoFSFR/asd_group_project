# Rayen

from tkinter import *
from tkinter import messagebox
import os, requests


class RestaurantOrder:
    def __init__(self, master):
        self.master = master
        self.master.title("Restaurant Order")
        self.master.geometry("600x400")

        # Order details variable
        self.order_details = StringVar()
        self.order_details.set("Order Details:\n")

        # Create sections buttons
        menu_button = Button(master, text="Menu", command=self.show_menu)
        menu_button.pack(side=LEFT, padx=10)

        dessert_button = Button(master, text="Desserts", command=self.show_desserts)
        dessert_button.pack(side=LEFT, padx=10)

        drinks_button = Button(master, text="Drinks", command=self.show_drinks)
        drinks_button.pack(side=LEFT, padx=10)

        # Order details label
        self.order_label = Label(master, textvariable=self.order_details, justify=LEFT)
        self.order_label.pack(side=LEFT, padx=10)

        # Order button
        order_button = Button(master, text="Order", command=self.place_order)
        order_button.pack(side=RIGHT, padx=10)

    def add_to_order(self, category, item, price):
        current_details = self.order_details.get()
        current_details += f"\n{category}: {item} - ${price:.2f}"
        self.order_details.set(current_details)

    def get_menu():
        get_menu_URL = os.getenv(
            "get-active-menu", "http://localhost:8080/get-active-menu"
        )
        data = requests.get(get_menu_URL)
        menu = data.json()

        global menu_items
        menu_items = menu["items"]

    get_menu()

    def show_menu(self):
        menu_window = Toplevel(self.master)
        menu_window.title("Menu")

        for item in menu_items:
            if item["itemType"] == "Food":
                button = Button(
                    menu_window,
                    text=f"{item['name']} - {item['price']}",
                    command=lambda i=item: self.add_to_order("Menu", i["name"], i["price"]),
                    width=30,
                )
                button.pack(pady=5)

        # Add button to add custom menu item
        add_custom_menu_button = Button(
            menu_window, text="Add Custom Menu Item", command=self.add_custom_menu_item
        )
        add_custom_menu_button.pack(pady=10)

    def show_desserts(self):
        dessert_window = Toplevel(self.master)
        dessert_window.title("Desserts")

        for item in menu_items:
            if item["itemType"] == "Dessert":
                button = Button(
                    dessert_window,
                    text=f"{item['name']} - {item['price']}",
                    command=lambda i=item: self.add_to_order(
                        "Desserts", i["name"], i["price"]
                    ),
                    width=30,
                )
                button.pack(pady=5)

        # Add button to add custom dessert
        add_custom_dessert_button = Button(
            dessert_window, text="Add Custom Dessert", command=self.add_custom_dessert
        )
        add_custom_dessert_button.pack(pady=10)

    def show_drinks(self):
        drinks_window = Toplevel(self.master)
        drinks_window.title("Drinks")

        for item in menu_items:
            if item["itemType"] == "Drink":
                button = Button(
                    drinks_window,
                    text=f"{item['name']} - {item['price']}",
                    command=lambda i=item: self.add_to_order(
                        "Drinks", i["name"], i["price"]
                    ),
                    width=30,
                )
                button.pack(pady=5)

        # Add button to add custom drink
        add_custom_drink_button = Button(
            drinks_window, text="Add Custom Drink", command=self.add_custom_drink
        )
        add_custom_drink_button.pack(pady=10)

    def add_custom_menu_item(self):
        custom_menu_window = Toplevel(self.master)
        custom_menu_window.title("Add Custom Menu Item")

        Label(custom_menu_window, text="Item Name:").pack(pady=5)
        item_name_entry = Entry(custom_menu_window)
        item_name_entry.pack(pady=5)

        Label(custom_menu_window, text="Item Price:").pack(pady=5)
        item_price_entry = Entry(custom_menu_window)
        item_price_entry.pack(pady=5)

        add_item_button = Button(
            custom_menu_window,
            text="Add Item",
            command=lambda: self.add_to_order(
                "Menu", item_name_entry.get(), float(item_price_entry.get())
            ),
        )
        add_item_button.pack(pady=10)

    def add_custom_dessert(self):
        custom_dessert_window = Toplevel(self.master)
        custom_dessert_window.title("Add Custom Dessert")

        Label(custom_dessert_window, text="Dessert Name:").pack(pady=5)
        dessert_name_entry = Entry(custom_dessert_window)
        dessert_name_entry.pack(pady=5)

        Label(custom_dessert_window, text="Dessert Price:").pack(pady=5)
        dessert_price_entry = Entry(custom_dessert_window)
        dessert_price_entry.pack(pady=5)

        add_dessert_button = Button(
            custom_dessert_window,
            text="Add Dessert",
            command=lambda: self.add_to_order(
                "Desserts", dessert_name_entry.get(), float(dessert_price_entry.get())
            ),
        )
        add_dessert_button.pack(pady=10)

    def add_custom_drink(self):
        custom_drink_window = Toplevel(self.master)
        custom_drink_window.title("Add Custom Drink")

        Label(custom_drink_window, text="Drink Name:").pack(pady=5)
        drink_name_entry = Entry(custom_drink_window)
        drink_name_entry.pack(pady=5)

        Label(custom_drink_window, text="Drink Price:").pack(pady=5)
        drink_price_entry = Entry(custom_drink_window)
        drink_price_entry.pack(pady=5)

        add_drink_button = Button(
            custom_drink_window,
            text="Add Drink",
            command=lambda: self.add_to_order(
                "Drinks", drink_name_entry.get(), float(drink_price_entry.get())
            ),
        )
        add_drink_button.pack(pady=10)

    def place_order(self):
        # Add functionality for placing the order, e.g., updating a database or sending the order to the kitchen
        messagebox.showinfo("Order Placed", "Your order has been placed successfully!")


if __name__ == "__main__":
    root = Tk()
    app = RestaurantOrder(root)
    root.mainloop()
