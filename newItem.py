import tkinter as tk
from tkinter import messagebox
import Model as m

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
        self.entry_item_name = tk.Entry(self.frame, font=("Arial", 10), width=25)
        self.entry_item_name.pack(pady=5)

        # Item Type
        self.label_item_type = tk.Label(self.frame, text="Item Type:", font=("Arial", 10))
        self.label_item_type.pack(anchor=tk.W, pady=5)
        self.combo_item_type = tk.StringVar()
        self.dropdown_item_type = tk.OptionMenu(self.frame, self.combo_item_type, "Drink", "Food", "Other")
        self.dropdown_item_type.pack(pady=5)

        # Details 
        self.label_ingredients = tk.Label(self.frame, text="Description (Ingredients):", font=("Arial", 10))
        self.label_ingredients.pack(anchor=tk.W, pady=5)
        self.text_ingredients = tk.Text(self.frame, font=("Arial", 10), height=4, width=25)
        self.text_ingredients.pack(pady=5)

        # Price
        self.label_price = tk.Label(self.frame, text="Price ($):", font=("Arial", 10))
        self.label_price.pack(anchor=tk.W, pady=5)
        self.entry_price = tk.Entry(self.frame, font=("Arial", 10), width=25)
        self.entry_price.pack(pady=5)

        # Stock
        self.label_stock = tk.Label(self.frame, text="Stock Quantity:", font=("Arial", 10))
        self.label_stock.pack(anchor=tk.W, pady=5)
        self.entry_stock = tk.Entry(self.frame, font=("Arial", 10), width=25)
        self.entry_stock.pack(pady=5)

        # Calories
        self.label_calories = tk.Label(self.frame, text="Calories:", font=("Arial", 10))
        self.label_calories.pack(anchor=tk.W, pady=5)
        self.entry_calories = tk.Entry(self.frame, font=("Arial", 10), width=25)
        self.entry_calories.pack(pady=5)

        # Image Path
        self.label_image_path = tk.Label(self.frame, text="Image File Path:", font=("Arial", 10))
        self.label_image_path.pack(anchor=tk.W, pady=5)
        self.entry_image_path = tk.Entry(self.frame, font=("Arial", 10), width=40)
        self.entry_image_path.pack(pady=5)

        # Submit Button
        self.button_submit = tk.Button(self.frame, text="Add Item", font=("Arial", 12), bg="#4CAF50", fg="white", command=self.submit_item)
        self.button_submit.pack(pady=10)

    def submit_item(self):
        """Collect and print item data for now (can be connected to backend later)."""
        item_data = [
            self.entry_item_name.get(),
            self.combo_item_type.get(),
            self.text_ingredients.get("1.0", tk.END).strip(),
            self.entry_price.get(),
            self.entry_stock.get(),
            self.entry_calories.get(),
            self.entry_image_path.get(),
        ]
        #return item_data
        
        menuitem = m.MenuItem('name', 'desc', 5, 5, 100, 'food', 'img.png')

        try:
            menuitem.name = item_data[0]
            menuitem.category = item_data[1]
            menuitem.description = item_data[2]
            menuitem.price = item_data[3]
            menuitem.stock = item_data[4]
            menuitem.calories = item_data[5]
            menuitem.image = item_data[6]

            menuitem.createMenuItem()
            print("Item Submitted:", item_data)
            messagebox.showinfo("Success", "Item is successfully added!")
            self.parent.menuPage() # need to test this
        except:
            messagebox.showerror("Error", "Fail to add item")
    

'''
class GUI:
    def __init__(self):
        """Main application window."""
        self.root = tk.Tk()
        self.root.title("Test Create New Item Page")

        self.root.geometry("450x650")
        self.create_item_page = newItem(self)
        self.root.mainloop()


# Run the test
if __name__ == "__main__":
    test_gui = GUI()
    '''
