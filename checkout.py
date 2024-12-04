# checkout.py
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import Model as m
import login

current_order = None

class CheckoutPage:
    def __init__(self, GUI):
        self.GUI = GUI
        self.root = GUI.root
        
        '''
        # dummy Item List
        self.items = [("Item 1", "Details: milk, coffe beans, black ink, sorrows of the soul", 10.99), 
                      ("Item 2", "Details 2", 5.49), 
                      ("Item 3", "Details 3", 8.99)]
                      '''
        
        self.item_in_order = m.ItemsInOrder(1, 'none')

        # fetch all menu items from databse to put in combobox
        self.menu = m.MenuItem('name', 'desc', 5, 5, 100, 'food', 'img.png')
        self.menu_items = self.menu.getMenuName()
                   
        
        order = m.Order(10000, 'online')

        global current_order
        # create order first
        if login.current_customer is not None and login.current_staff is None:
            onlineorder = m.OnlineOrder(10000, 'none', '1/1/2000', 'none', '5.00', '12:00')
            userID = login.current_customer
            #print(custID)
            onlineorder.createOnlineOrder(userID)
            current_order = onlineorder.onlineID
        else:
            inpersonorder = m.InPersonOrder(10000, 'none', '1/1/2000', 'none', '5.00', '12:00')
            userID = login.current_staff
            #print(staffID)
            inpersonorder.createInPersonOrder(userID)
            current_order = inpersonorder.inPersonID
        
        
        

        # frame
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10, padx=10)
        
        # Listbox for items
        self.listbox = tk.Listbox(self.frame, selectmode="extended", height=10, width=30)
        '''
        for item in self.menu_items:
            self.listbox.insert(tk.END, f"{item[0]} - ${item[2]:.2f}")
            '''
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
        total = self.item_in_order.getTotalCost(current_order)
        self.total_label.config(text=f"Total: ${total:.2f}")

    def view_details(self):
        selected = self.listbox.curselection()
        if not selected or len(selected) > 1:
            messagebox.showerror("Error", "Please select one item to view details.")
            return
        
        index = selected[0]
        item = self.menu_items[index]
        messagebox.showinfo("Item Details", f"Name: {item[0]}\nDetails: {item[1]}\nPrice: ${item[2]:.2f}")

    def remove_items(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "No items selected.")
            return
        
        confirm = messagebox.askyesno("Remove Items", "Are you sure you want to remove the selected items?")
        if confirm:
            for index in selected:  # Remove from the end to avoid index shifting
                self.listbox.delete(index)

            print(selected[0])
            
            selected_item = self.listbox.get(selected)
            print(selected_item)
            

            #for item in self.menu_items:
                #self.listbox.insert(tk.END, f"{item[0]} - ${item[2]:.2f}")

            # get menu item ID from name
            # self.menu.name = selected_item[0]
            #itemID = self.menu.getItemID()

            # remove the item to itemsinorder table
            # item_in_order = m.ItemsInOrder(1, 'none')
            #self.item_in_order.removeItemsFromOrder(itemID, current_order)
            #print(itemID,current_order)

            self.update_total()
            
            '''
            if not self.items:
                quit_confirm = messagebox.askyesno(
                    "No Items Left", "All items have been removed. Do you want to return to the menu?"
                )
                if quit_confirm:
                    self.GUI.showPages(1)  # Go back to menuPage
                else:
                    self.items.append(("Placeholder Item", "Details", 0))  # Add a placeholder to prevent empty list error
                    self.listbox.insert(tk.END, f"{self.items[0][0]} - ${self.items[0][2]:.2f}")
            '''

    def continue_shopping(self):
        # Create a pop-up window
        shopping_window = tk.Toplevel(self.root)
        shopping_window.title("Continue Shopping")
        shopping_window.geometry("400x300")


        # Combobox for items
        tk.Label(shopping_window, text="Select Item:").pack(pady=5)
        item_var = tk.StringVar()
        item_combobox = ttk.Combobox(
        shopping_window, 
        textvariable=item_var, 
        values=[item[0] for item in self.menu_items], 
        state="readonly"
    )
        item_combobox.pack(pady=5)

        # Quantity Spinbox
        tk.Label(shopping_window, text="Select Quantity:").pack(pady=5)
        quantity_var = tk.IntVar(value=1)
        quantity_spinbox = tk.Spinbox(
        shopping_window, 
        from_=1, 
        to=100, 
        textvariable=quantity_var, 
        width=5
    )
        quantity_spinbox.pack(pady=5)

        # Details Text Area
        tk.Label(shopping_window, text="Item Details:").pack(pady=5)
        details_text = tk.Text(shopping_window, height=5, width=40, state="disabled")
        details_text.pack(pady=5)           

        def update_details(*args):
            selected_item = item_var.get()
            for item in self.menu_items:
                if item[0] == selected_item:
                    details_text.config(state="normal")
                    details_text.delete("1.0", tk.END)
                    details_text.insert(tk.END, item[1])
                    details_text.config(state="disabled")
                    break

        # Update details when an item is selected
        item_combobox.bind("<<ComboboxSelected>>", update_details)

        # Customization area 
        tk.Label(shopping_window, text="Customization:").pack(pady=5)
        customization_text = tk.Text(shopping_window, height=5, width=30, state="normal")
        customization_text.pack(pady=5)

        # Add Item Button
        def add_item():
            selected_item = item_var.get()

            # get menu item ID from name
            self.menu.name = selected_item
            itemID = self.menu.getItemID()
            
            quantity = quantity_var.get()
            customization = customization_text.get("1.0", tk.END).strip()

            if not selected_item:
                messagebox.showerror("Error", "Please select an item.")
                return
    
            for item in self.menu_items:
                if item[0] == selected_item:
                    # Add the item back to the listbox
                    self.listbox.insert(tk.END, f"{item[0]} x{quantity} - ${item[2] * quantity:.2f}")
                    
                    
                    # add the item to itemsinorder table
        
                    self.item_in_order.quantity = quantity
                    self.item_in_order.customization = customization
                    self.item_in_order.addItemsToOrder(itemID, current_order)
                    print(self.item_in_order.quantity, self.item_in_order.customization, itemID, current_order)

                    # Update the total price
                    self.update_total()
                    
    
            shopping_window.destroy()
            return

        tk.Button(shopping_window, text="Add Item", command=add_item).pack(pady=10)
        

    def checkout(self):
        if not self.item_in_order:
            messagebox.showerror("Error", "Cannot checkout with no items.")
            return
        messagebox.showinfo("Checkout", "Proceeding to payment...")
        self.GUI.clearPage()
        self.GUI.payForOrder()