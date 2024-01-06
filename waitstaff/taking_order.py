from tkinter import *
from tkinter import messagebox

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

    def show_menu(self):
        menu_window = Toplevel(self.master)
        menu_window.title("Menu")

        menu_items = [
            {"name": "Spaghetti Bolognese", "price": 12.99},
            {"name": "Chicken Alfredo", "price": 14.99},
            {"name": "Margherita Pizza", "price": 10.99},
            {"name": "Caesar Salad", "price": 8.99},
            {"name": "Grilled Salmon", "price": 16.99},
            {"name": "Vegetarian Stir Fry", "price": 11.99},
            {"name": "Cheeseburger", "price": 9.99},
            {"name": "Chicken Sandwich", "price": 8.99},
            {"name": "Shrimp Scampi", "price": 15.99},
            {"name": "Vegetarian Pizza", "price": 11.99},
            {"name": "Mushroom Risotto", "price": 13.99},
            {"name": "BBQ Ribs", "price": 17.99},
        ]

        for item in menu_items:
            button = Button(menu_window, text=f"{item['name']} - ${item['price']:.2f}",
                            command=lambda i=item: self.add_to_order("Menu", i['name'], i['price']), width=30)
            button.pack(pady=5)

        # Add button to add custom menu item
        add_custom_menu_button = Button(menu_window, text="Add Custom Menu Item", command=self.add_custom_menu_item)
        add_custom_menu_button.pack(pady=10)

    def show_desserts(self):
        dessert_window = Toplevel(self.master)
        dessert_window.title("Desserts")

        dessert_items = [
            {"name": "Chocolate Cake", "price": 6.99},
            {"name": "Cheesecake", "price": 8.99},
            {"name": "Tiramisu", "price": 7.99},
            {"name": "Apple Pie", "price": 5.99},
            {"name": "Brownie Sundae", "price": 9.99},
            {"name": "Fruit Tart", "price": 7.99},
            {"name": "Ice Cream Sundae", "price": 6.99},
            {"name": "Pecan Pie", "price": 8.99},
            {"name": "Lemon Sorbet", "price": 5.99},
            {"name": "Red Velvet Cake", "price": 7.99},
            {"name": "Strawberry Shortcake", "price": 6.99},
            {"name": "Creme Brulee", "price": 8.99},
        ]

        for item in dessert_items:
            button = Button(dessert_window, text=f"{item['name']} - ${item['price']:.2f}",
                            command=lambda i=item: self.add_to_order("Desserts", i['name'], i['price']), width=30)
            button.pack(pady=5)

        # Add button to add custom dessert
        add_custom_dessert_button = Button(dessert_window, text="Add Custom Dessert", command=self.add_custom_dessert)
        add_custom_dessert_button.pack(pady=10)

    def show_drinks(self):
        drinks_window = Toplevel(self.master)
        drinks_window.title("Drinks")

        drink_items = [
            {"name": "Coca-Cola", "price": 1.99},
            {"name": "Pepsi", "price": 1.99},
            {"name": "Sprite", "price": 1.99},
            {"name": "Iced Tea", "price": 1.49},
            {"name": "Lemonade", "price": 1.99},
            {"name": "Orange Juice", "price": 2.49},
            {"name": "Coffee", "price": 1.29},
            {"name": "Water", "price": 0.99},
            {"name": "Milk", "price": 1.49},
        ]

        for item in drink_items:
            button = Button(drinks_window, text=f"{item['name']} - ${item['price']:.2f}",
                            command=lambda i=item: self.add_to_order("Drinks", i['name'], i['price']), width=30)
            button.pack(pady=5)

        # Add button to add custom drink
        add_custom_drink_button = Button(drinks_window, text="Add Custom Drink", command=self.add_custom_drink)
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

        add_item_button = Button(custom_menu_window, text="Add Item",
                                 command=lambda: self.add_to_order("Menu", item_name_entry.get(), float(item_price_entry.get())))
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

        add_dessert_button = Button(custom_dessert_window, text="Add Dessert",
                                    command=lambda: self.add_to_order("Desserts", dessert_name_entry.get(), float(dessert_price_entry.get())))
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

        add_drink_button = Button(custom_drink_window, text="Add Drink",
                                  command=lambda: self.add_to_order("Drinks", drink_name_entry.get(), float(drink_price_entry.get())))
        add_drink_button.pack(pady=10)

    def place_order(self):
        # Add functionality for placing the order, e.g., updating a database or sending the order to the kitchen
        messagebox.showinfo("Order Placed", "Your order has been placed successfully!")

if __name__ == "__main__":
    root = Tk()
    app = RestaurantOrder(root)
    root.mainloop()
