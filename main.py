import tkinter as tk


class cafeGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1920x1080")
        self.root.grid_columnconfigure(5)
        

        # labels for navigation bar
        self.searchLabel = tk.Label(self.root, text="search")
        self.searchBox = tk.Entry(self.root)
        self.naviBar()


        self.root.mainloop()
    
    def naviBar(self):
        self.searchLabel.grid(row = 0, column = 0, rowspan=5, pady = 2)
        self.searchBox.grid(row = 0, column = 1, pady = 2)


cafeGUI()