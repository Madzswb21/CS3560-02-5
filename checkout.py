# checkout.py
# checkout.py
import tkinter as tk
from tkinter import messagebox

class CheckoutPage:
    def __init__(self, GUI):
        self.GUI = GUI
        self.root = GUI.root
        
        # dummy Item List
        self.items = [("Item 1", "Details: milk, coffe beans, black ink, sorrows of the soul", 10.99), 
                      ("Item 2", "Details 2", 5.49), 
                      ("Item 3", "Details 3", 8.99)]
        
        # frame
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10, padx=10)
        
        # Listbox for items
        self.listbox = tk.Listbox(self.frame, selectmode="extended", height=10, width=30)
        for item in self.items:
            self.listbox.insert(tk.END, f"{item[0]} - ${item[2]:.2f}")
        self.listbox.grid(row=0, column=0, rowspan=4, padx=10, pady=5)
        
        # Buttons
        self.details_button = tk.Button(self.frame, text="View Details", command=self.view_details)
        self.details_button.grid(row=4, column=0, padx=5, sticky="w")
        
        self.remove_button = tk.Button(self.frame, text="Remove Selected", command=self.remove_items)
        self.remove_button.grid(row=4, column=0, padx=5, sticky="e")
        
        
        self.continue_button = tk.Button(self.frame, text="Continue Shopping", command=self.continue_shopping)
        self.continue_button.grid(row=5, column=0, pady=10)

        # Total and Checkout
        total_checkout_frame = tk.Frame(self.frame)
        total_checkout_frame.grid(row=6, column=0, pady=10)
        
        self.total_label = tk.Label(total_checkout_frame, text="Total: $0.00")
        self.total_label.pack(side="left", padx=5)
        
        self.checkout_button = tk.Button(total_checkout_frame, text="Checkout", command=self.checkout)
        self.checkout_button.pack(side="left", padx=5)
        
        self.update_total()

    def update_total(self):
        total = sum(item[2] for item in self.items)
        self.total_label.config(text=f"Total: ${total:.2f}")

    def view_details(self):
        selected = self.listbox.curselection()
        if not selected or len(selected) > 1:
            messagebox.showerror("Error", "Please select one item to view details.")
            return
        
        index = selected[0]
        item = self.items[index]
        messagebox.showinfo("Item Details", f"Name: {item[0]}\nDetails: {item[1]}\nPrice: ${item[2]:.2f}")

    def remove_items(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "No items selected.")
            return
        
        confirm = messagebox.askyesno("Remove Items", "Are you sure you want to remove the selected items?")
        if confirm:
            for index in reversed(selected):  # Remove from the end to avoid index shifting
                del self.items[index]
            
            self.listbox.delete(0, tk.END)
            for item in self.items:
                self.listbox.insert(tk.END, f"{item[0]} - ${item[2]:.2f}")
            self.update_total()
            
            if not self.items:
                quit_confirm = messagebox.askyesno(
                    "No Items Left", "All items have been removed. Do you want to return to the menu?"
                )
                if quit_confirm:
                    self.GUI.showPages(1)  # Go back to menuPage
                else:
                    self.items.append(("Placeholder Item", "Details", 0))  # Add a placeholder to prevent empty list error
                    self.listbox.insert(tk.END, f"{self.items[0][0]} - ${self.items[0][2]:.2f}")

    def continue_shopping(self):
        self.GUI.showPages(1)  # Go back to menuPage

    def checkout(self):
        if not self.items:
            messagebox.showerror("Error", "Cannot checkout with no items.")
            return
        messagebox.showinfo("Checkout", "Proceeding to payment...")