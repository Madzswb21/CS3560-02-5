import tkinter as tk
from tkinter import messagebox
import re
import Model as m
import checkout as ch


class PayForOrderPage:
    def __init__(self, parent):
        """Initialize the Pay for Order page."""
        self.frame = tk.Frame(parent.root)
        self.frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Header
        self.header = tk.Label(self.frame, text="Pay for Order", font=("Arial", 14, "bold"))
        self.header.pack(pady=10)

        # Cardholder Name
        self.label_card_name = tk.Label(self.frame, text="Cardholder Name:", font=("Arial", 10))
        self.label_card_name.pack(anchor=tk.W, pady=(10, 5))
        self.entry_card_name = tk.Entry(self.frame, width=30, font=("Arial", 10))
        self.entry_card_name.pack(pady=5)

        # Card Number
        self.label_card_number = tk.Label(self.frame, text="Card Number (16 digits):", font=("Arial", 10))
        self.label_card_number.pack(anchor=tk.W, pady=(10, 5))
        self.entry_card_number = tk.Entry(self.frame, width=30, font=("Arial", 10))
        self.entry_card_number.pack(pady=5)

        # Expiration Date
        self.label_exp_date = tk.Label(self.frame, text="Expiration Date (MM/YY):", font=("Arial", 10))
        self.label_exp_date.pack(anchor=tk.W, pady=(10, 5))
        self.entry_exp_date = tk.Entry(self.frame, width=10, font=("Arial", 10))
        self.entry_exp_date.pack(pady=5)


        # Payment Options
        self.label_payment = tk.Label(self.frame, text="Payment Method:", font=("Arial", 10))
        self.label_payment.pack(anchor=tk.W, pady=(10, 5))
        self.payment_method = tk.StringVar(value="card")
        self.radio_card = tk.Radiobutton(self.frame, text="Credit/Debit Card", variable=self.payment_method, value="card", font=("Arial", 8))
        self.radio_cash = tk.Radiobutton(self.frame, text="Cash", variable=self.payment_method, value="cash", font=("Arial", 8))
        self.radio_card.pack(anchor=tk.W, pady=2)
        self.radio_cash.pack(anchor=tk.W, pady=2)
        
        # Submit Button
        self.button_submit = tk.Button(self.frame, text="Submit Payment", font=("Arial", 10), bg="#4CAF50", fg="white", command=self.validate_form)
        self.button_submit.pack(pady=20)

        '''
        # Pickup or Delivery
        self.label_delivery = tk.Label(self.frame, text="Select Pickup or Delivery:", font=("Arial", 10))
        self.label_delivery.pack(anchor=tk.W, pady=(10, 5))
        self.button_pickup = tk.Button(self.frame, text="Pickup", font=("Arial", 10), bg="#4CAF50", fg="white", command=self.pickup_action)
        self.button_delivery = tk.Button(self.frame, text="Delivery", font=("Arial", 10), bg="#2196F3", fg="white", command=self.delivery_action)
        self.button_pickup.pack(side=tk.LEFT, expand=True, pady=20, padx=10)
        self.button_delivery.pack(side=tk.RIGHT, expand=True, pady=20, padx=10)
        '''
        
        

    def validate_form(self):
        """Validate the form inputs."""
        card_name = self.entry_card_name.get().strip()
        card_number = self.entry_card_number.get().strip()
        exp_date = self.entry_exp_date.get().strip()

        # Validate cardholder name
        if not card_name:
            messagebox.showerror("Validation Error", "Cardholder Name cannot be empty.")
            return

        # Validate card number
        if not re.fullmatch(r"\d{16}", card_number):
            messagebox.showerror("Validation Error", "Card Number must be exactly 16 digits.")
            return

        # Validate expiration date
        if not re.fullmatch(r"(0[1-9]|1[0-2])/\d{2}", exp_date):
            messagebox.showerror("Validation Error", "Expiration Date must be in MM/YY format.")
            return

        # If all validations pass
        messagebox.showinfo("Success", "Payment details submitted successfully!")


        order = m.Order(10000, 'online')
        order.orderID = ch.current_order
        result = order.payOrder()
        
        messagebox.showinfo("Success", result)
        self.parent.menuPage()
        

        




