import tkinter as tk
from tkinter import ttk

class OrderStatusApp:
    def __init__(self, root, orderID):
        self.root = root
        self.root.title("Check Order Status")
        self.root.geometry("500x520")  

        # Header 
        self.header_label = tk.Label(self.root, text="Your Order Status", font=("Arial", 16))
        self.header_label.pack(pady=10)

        # Order ID label 
        self.orderID_label = tk.Label(self.root, text=f"Order ID: {orderID}", font=("Arial", 12))
        self.orderID_label.pack(pady=5)

        # Connected Progress Bar
        self.canvas = tk.Canvas(self.root, width=500, height=120)
        self.canvas.pack(pady=20)

        # circles x-coordinates
        self.circle_radius = 20
        self.step_positions = [100, 200, 300, 400]  
        self.steps = ['Placed Order', 'Cooking!', 'Preparing', 'Ready!']  

        # Circles for corresponding step 
        self.circles = []
        for i, pos in enumerate(self.step_positions):
            circle = self.canvas.create_oval(pos - self.circle_radius, 40, pos + self.circle_radius, 60, outline="black", width=2, fill="gray")
            self.circles.append(circle)
            self.canvas.create_text(pos, 80, text=self.steps[i], font=("Arial", 10))

        # Progress bar (from 0 to 100)
        self.progress_bar = ttk.Progressbar(self.root, orient="horizontal", length=300, mode="determinate", maximum=100)
        self.progress_bar.pack(pady=10)

        # Status Label
        self.status_label = tk.Label(self.root, text="Status: Ordering", font=("Arial", 12))
        self.status_label.pack(pady=5)

        # Buttons 
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20, anchor="center")

        self.create_order_button = tk.Button(button_frame, text="Create New Order", command=self.create_new_order)
        self.create_order_button.grid(row=0, column=0, padx=10)

        self.logout_button = tk.Button(button_frame, text="Logout", command=self.logout)
        self.logout_button.grid(row=0, column=1, padx=10)

        # Back Button 
        self.back_button = tk.Button(self.root, text="← Back", command=self.back_to_main)
        self.back_button.pack(pady=10, anchor="center")

        # Update Button to Simulate Progress (REMOVE LATER)
        self.update_button = tk.Button(self.root, text="Update Progress", command=self.update_progress)
        self.update_button.pack(pady=10, anchor="center")

    def update_progress(self):
        """Simulate updating the progress bar and changing circle colors."""
        current_value = self.progress_bar['value']
        
        # If progress is less than 100, increment by 25 
        if current_value < 100:
            self.progress_bar['value'] += 25
        else:
            self.progress_bar['value'] = 0  # Reset for demo
        
        self.update_status_label()
        self.update_step_circles()

    def update_status_label(self):
        """Update the label to match the progress bar state."""
        progress = self.progress_bar['value']
        
        if progress == 0:
            self.status_label.config(text="Status: Ordering")
        elif progress == 25:
            self.status_label.config(text="Status: Placed Order")
        elif progress == 50:
            self.status_label.config(text="Status: Cooking!")
        elif progress == 75:
            self.status_label.config(text="Status: Preparing")
        elif progress == 100:
            self.status_label.config(text="Status: READY!!")

    def update_step_circles(self):
        """Update the step circles to show progress by changing colors."""
        progress = self.progress_bar['value']

        # For each step, update the circle's colors based on progress
        for i, circle in enumerate(self.circles):
            if progress >= (i + 1) * 25:  # Completed (green)
                self.canvas.itemconfig(circle, fill="green")
            else:  # Not started (gray)
                self.canvas.itemconfig(circle, fill="gray")

    def back_to_main(self):
        """Handle the back button."""
        print("Going back to the main page!")

    def logout(self):
        """Handle the logout button."""
        print("Logging out!")

    def create_new_order(self):
        """Handle creating a new order."""
        print("Creating a new order!")


class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Order Status App")

        # Automatically fetch the orderID (I used static orderID for testing)
        # this would normally be dynamically retrieved 
        self.orderID = 12345  #DELETE

        # Initialize the OrderStatusApp automatically
        self.order_status_app = OrderStatusApp(self.root, self.orderID)

        # Start the Tkinter main loop
        self.root.mainloop()

# Run the test
if __name__ == "__main__":
    test_gui = GUI()







