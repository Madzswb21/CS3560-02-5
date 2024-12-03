import tkinter as tk

class newItem:
    def __init__(self, parent):
        """Initialize the Create New Item page."""
        self.frame = tk.Frame(parent.root)
        self.frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Header
        self.header = tk.Label(self.frame, text="Create New Item", font=("Arial", 16, "bold"))
        self.header.pack(pady=10)

        # Item Name
        self.label_item_name = tk.Label(self.frame, text="Item Name:", font=("Arial", 10))
        self.label_item_name.pack(anchor=tk.W, pady=5)
        self.entry_item_name = tk.Entry(self.frame, font=("Arial", 10), width=30)
        self.entry_item_name.pack(pady=5)

        # Item Type
        self.label_item_type = tk.Label(self.frame, text="Item Type:", font=("Arial", 10))
        self.label_item_type.pack(anchor=tk.W, pady=5)
        self.combo_item_type = tk.StringVar()
        self.dropdown_item_type = tk.OptionMenu(self.frame, self.combo_item_type, "Hot Drink", "Iced Drink", "Food")
        self.dropdown_item_type.pack(pady=5)

        # Ingredients
        self.label_ingredients = tk.Label(self.frame, text="Ingredients (Details):", font=("Arial", 10))
        self.label_ingredients.pack(anchor=tk.W, pady=5)
        self.text_ingredients = tk.Text(self.frame, font=("Arial", 10), height=5, width=40)
        self.text_ingredients.pack(pady=5)

        # Submit Button
        self.button_submit = tk.Button(self.frame, text="Add Item", font=("Arial", 12), bg="#4CAF50", fg="white", command=self.submit_item)
        self.button_submit.pack(pady=10)

    def submit_item(self):
        """Placeholder for the Add Item action."""
        print("Submit button clicked!")  # Replace this with functionality later


class GUI:
    def __init__(self):
        """Main application window."""
        self.root = tk.Tk()
        self.root.title("Test Create New Item Page")

        # Set window size
        self.root.geometry("400x450")

        # Initialize the CreateNewItemPage
        self.create_item_page = newItem(self)

        # Start the Tkinter main loop
        self.root.mainloop()


# Run the test
if __name__ == "__main__":
    test_gui = GUI()
