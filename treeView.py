import tkinter as tk
from tkinter import ttk


class TreeViewApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Orders Overview")
        self.root.geometry("700x500")

        # Header
        self.header_label = tk.Label(self.root, text="Order Management", font=("Arial", 16))
        self.header_label.pack(pady=10)

        # Frame
        self.tree_frame = tk.Frame(self.root)
        self.tree_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        # Scrollbar setup
        self.scrollbar = ttk.Scrollbar(self.tree_frame, orient="vertical")

        # Treeview
        self.tree = ttk.Treeview(
            self.tree_frame,
            columns=("Order ID", "Order Type", "Status", "Payment Date", "Total Cost"),
            show="headings",
            yscrollcommand=self.scrollbar.set
        )
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbar
        self.scrollbar.config(command=self.tree.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Columns
        self.tree.heading("Order ID", text="Order ID")
        self.tree.heading("Order Type", text="Order Type")
        self.tree.heading("Status", text="Status")
        self.tree.heading("Payment Date", text="Payment Date")
        self.tree.heading("Total Cost", text="Total Cost")

        # Column widths
        self.tree.column("Order ID", width=100, anchor="center")
        self.tree.column("Order Type", width=100, anchor="center")
        self.tree.column("Status", width=150, anchor="center")
        self.tree.column("Payment Date", width=150, anchor="center")
        self.tree.column("Total Cost", width=100, anchor="center")

        # Dummy data (DELETE LATER)
        self.sample_data = [
            (12345, "Food", "Placed Order", "2024-12-01", "$25.00"),
            (12346, "Drink", "Cooking!", "2024-12-01", "$5.50"),
            (12347, "Other", "Preparing", "2024-12-02", "$15.75"),
            (12348, "Food", "Ready!", "2024-12-02", "$30.00"),
        ]
        for order in self.sample_data:
            self.tree.insert("", "end", values=order)

        # Buttons Frame
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(pady=10)

        # Update Status Button
        self.update_status_button = tk.Button(self.buttons_frame, text="Update Status", command=self.update_status)
        self.update_status_button.grid(row=0, column=0, padx=10)

        # Back Button
        self.back_button = tk.Button(self.buttons_frame, text="Back", command=self.go_to_main)
        self.back_button.grid(row=0, column=1, padx=10)

        # Refresh Button (DELETE IF NOT NEEDED)
        self.refresh_button = tk.Button(self.root, text="Refresh", command=self.refresh_data)
        self.refresh_button.pack(pady=10)

    def update_status(self):
        """Update the status of the selected order."""
        selected_item = self.tree.selection()
        if not selected_item:
            return  # Do nothing if no order is selected

        current_values = self.tree.item(selected_item, "values")
        order_id, order_type, current_status, payment_date, total_cost = current_values

        # Status progression logic
        status_steps = ["Placed Order", "Cooking!", "Preparing", "Ready!"]
        try:
            next_status = status_steps[(status_steps.index(current_status) + 1) % len(status_steps)]
        except ValueError:
            next_status = "Placed Order"  # Reset if invalid

        # Update Treeview
        self.tree.item(selected_item, values=(order_id, order_type, next_status, payment_date, total_cost))

    def refresh_data(self): # DELETE IF NOT NEEDED
        """Refresh data (placeholder for actual database refresh)."""
        self.tree.delete(*self.tree.get_children())
        for order in self.sample_data:
            self.tree.insert("", "end", values=order)

    def go_to_main(self):
        """Navigate back to the main page."""
        # Placeholder for integration with the main page
        self.root.destroy()
        print("Back to main page! (Integration needed)")


# Run it
if __name__ == "__main__":
    root = tk.Tk()
    app = TreeViewApp(root)
    root.mainloop()
