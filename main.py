import tkinter as tk
import tkinter.font as tkFont

class cafeGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1920x1080")
        self.root.grid_columnconfigure(5)

        self.pageIndex = 0
        self.pages = [self.menuPage, self.checkOut, self.loginCreateAccount, self.payForOrder, self.itemPage, self.orderStatus]

        # labels for navigation bar
        self.searchLabel = tk.Label(self.root, text="search", font=tkFont.Font(family="Times New Roman", size=12))
        self.searchBox = tk.Entry(self.root, width=50, font=tkFont.Font(family="Times New Roman", size=12))
        self.cart = tk.Button(self.root, text="Cart", font=tkFont.Font(family="Times New Roman", size=12)) 

        # labels for testing purposes
        self.label1 = tk.Label(self.root, text="menuPage", font=tkFont.Font(family="Times New Roman", size=12))
        self.label2 = tk.Label(self.root, text="checkOut", font=tkFont.Font(family="Times New Roman", size=12))
        self.label3 = tk.Label(self.root, text="loginCreateAccount", font=tkFont.Font(family="Times New Roman", size=12))
        self.label4 = tk.Label(self.root, text="payForOrder", font=tkFont.Font(family="Times New Roman", size=12))
        self.label5 = tk.Label(self.root, text="itemPage", font=tkFont.Font(family="Times New Roman", size=12))
        self.label6 = tk.Label(self.root, text="orderStatus", font=tkFont.Font(family="Times New Roman", size=12))

        self.showPages()
        self.root.mainloop()
    
    def naviBar(self):
        self.searchLabel.grid(row = 0, column = 0, rowspan=5, pady = 2)
        self.searchBox.grid(row = 0, column = 1, pady = 2)
        self.cart.grid(row = 0, column = 2, pady = 2)

    def menuPage(self):
        self.label1.grid(row = 1, column = 0, rowspan=5, pady = 2)
    
    def checkOut(self):
        self.label2.grid(row = 1, column = 0, rowspan=5, pady = 2)
    
    def loginCreateAccount(self): 
        self.label3.grid(row = 1, column = 0, rowspan=5, pady = 2)

    def payForOrder(self):
        self.label4.grid(row = 1, column = 0, rowspan=5, pady = 2)

    def itemPage(self): #I haven't decided whether or not to make a page for each item or to do arguments! probably arguements, but TBD! :)
        self.label5.grid(row = 1, column = 0, rowspan=5, pady = 2)

    def orderStatus(self):
        self.label6.grid(row = 1, column = 0, rowspan=5, pady = 2)

    def showPages(self): #this is the function that will show everything -> put all visual thingys here!
        self.naviBar()
        self.pages[self.pageIndex]() #if we do arguments for itemPage, use an if statement (if pageIndex != 2)



cafeGUI()