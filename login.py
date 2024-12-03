# login/ Create Account Page
import tkinter as tk
from tkinter import messagebox
import Model as m

class LoginPage:
    def __init__(self, GUI):
        self.GUI = GUI
        self.root = GUI.root  
        
        # Widgets for login
        self.username_label = tk.Label(self.root, text="Username")
        self.username_entry = tk.Entry(self.root)
        self.password_label = tk.Label(self.root, text="Password")
        self.password_entry = tk.Entry(self.root, show="*")  # Hide password
        
        # Buttons for login
        self.login_button = tk.Button(self.root, text="Login", command=self.login, width=20)  

        # Placing widgets 
        self.username_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.username_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        self.password_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        self.login_button.grid(row=2, column=0, columnspan=2, pady=10, padx=(45, 0))  #small right padding to align login button

        # centering without stretching too much
        self.root.grid_columnconfigure(0, weight=1)  
        self.root.grid_columnconfigure(1, weight=3)  
        self.root.grid_columnconfigure(2, weight=1)  

        
        self.root.grid_rowconfigure(0, weight=1)  
        self.root.grid_rowconfigure(1, weight=1)  
        self.root.grid_rowconfigure(2, weight=1)  

    def login(self):
        # Login logic here
        username = self.username_entry.get()
        password = self.password_entry.get()

        m.Customer.username = username
        m.Customer.password = password
        
        # For now, just a basic check (replace this with actual authentication logic)
        if m.Customer.login:
            messagebox.showinfo("Login", "Login Successful!")
            self.GUI.showPages(1)  # Navigate to the next page (e.g., menuPage)
        else:
            messagebox.showerror("Error", "Invalid username or password")
