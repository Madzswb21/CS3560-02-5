import tkinter as tk


class cafeGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("720x560")
        self.root.title("Cafe Webpage") 

        self.root.grid_columnconfigure(5)
        

        # labels for navigation bar
        self.searchLabel = tk.Label(self.root, text="search")
        self.searchBox = tk.Entry(self.root)
        self.naviBar()

        self.buttonDrink = tk.Button(text="Drink", width=5,font=("Times New Roman",14))
        self.buttonFood = tk.Button(text="Food", width=5,font=("Times New Roman",14))
        self.buttonOther = tk.Button(text="Other", width=5,font=("Times New Roman",14))


        self.buttonItem = tk.Button(text="Item", width=10,font=("Times New Roman",14))
        self.buttonItem2 = tk.Button(text="Item", width=10,font=("Times New Roman",14))
        self.buttonItem3 = tk.Button(text="Item", width=10,font=("Times New Roman",14))

        self.buttonaddto1 = tk.Button(text="add", width=10,font=("Times New Roman",10))




        self.button()



        self.root.mainloop()
    
    def naviBar(self):
        self.searchLabel.grid(row = 0, column = 0, rowspan=5, pady = 2)
        self.searchBox.grid(row = 0, column = 1, pady = 2)
    
    def button(self):
        self.buttonDrink.grid(row = 5, column = 0, pady = 6)
        self.buttonFood.grid(row = 5, column = 1, pady = 6)
        self.buttonOther.grid(row = 5, column = 2, pady = 6)
        self.buttonItem.grid(row = 7, column = 0, pady = 50)
        self.buttonItem2.grid(row = 7, column = 1, pady = 50)
        self.buttonItem3.grid(row = 7, column = 2, pady = 50)

        self.buttonaddto1.grid(row = 8, column = 0, pady = 20)









cafeGUI()