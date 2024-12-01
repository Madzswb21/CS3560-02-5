import tkinter as tk


class cafeGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("720x560")
        self.root.title("Cafe Webpage") 

        self.root.grid_columnconfigure(5)
        

        # labels for navigation bar
        self.searchLabel = tk.Label(self.root, text="Username:")
        self.searchBox = tk.Entry(self.root)
        self.naviBar()

     #   self.buttonDrink = tk.Button(text="Drink", width=5,font=("Times New Roman",14))
      #  self.buttonFood = tk.Button(text="Food", width=5,font=("Times New Roman",14))





       # self.button()



        self.root.mainloop()
    
    def naviBar(self):
        self.searchLabel.grid(row = 8, column = 9)
       # self.searchBox.grid(row = 9, column = 9, rowspan=5, pady = 2)
    
    #def button(self):
       # self.buttonDrink.grid(row = 10, column = 10, pady = 6)
        #self.buttonFood.grid(row = 10, column = 10, pady = 6)
        








cafeGUI()