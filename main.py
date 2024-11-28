import tkinter as tk

class menuItemButton: #for menu page
    instances = [] #holds every instance of the button just in case we need it!
    def __init__(self, text, page, img):
        menuItemButton.instances.append(self)
        self.f = tk.Frame(width=125, height=125,bg="white")
        self.img = tk.PhotoImage(file=img)
        self.cart = tk.Button(self.frame, text="Add to Cart", width=10,font=("Times New Roman",8))
        self.view = tk.Button(self.frame, text="View Item", width=125,font=("Times New Roman",8), image=self.img)
    def grid(self, r, c):
        self.cart.pack(side="bottom")
        self.view.pack(side="top")
        self.f.grid(row = r, column = c, pady = 50)


class cafeGUI: 
    def __init__(self): #note to self: no widgets should be added here! they should only be added to the functions for pages!
        self.root = tk.Tk()
        self.root.geometry("820x560")
        self.root.title("Cafe Webpage") 

        self.pageIndex = 0
        self.pages = [self.menuPage, self.checkOut, self.loginCreateAccount, self.payForOrder, self.itemPage, self.orderStatus]

        self.root.grid_columnconfigure(0,weight=1)
        self.root.grid_columnconfigure(1,weight=1)
        self.root.grid_columnconfigure(2,weight=1)
        self.root.grid_columnconfigure(3,weight=1)
        self.root.grid_columnconfigure(4,weight=1)
        self.root.grid_columnconfigure(5,weight=1)
        
        # labels for navigation bar
        self.searchLabel = tk.Label(self.root, text="search")
        self.searchBox = tk.Entry(self.root)
        self.buttonDrink = tk.Button(text="Drink", width=5,font=("Times New Roman",14))
        self.buttonFood = tk.Button(text="Food", width=5,font=("Times New Roman",14))
        self.buttonOther = tk.Button(text="Other", width=5,font=("Times New Roman",14))
        
        self.showPages()
        self.root.mainloop()
    
    def naviBar(self):
        self.searchLabel.grid(row = 0, column = 0, pady = 2)
        self.searchBox.grid(row = 0, column = 1, pady = 2, columnspan=2, sticky="ew")

    def menuPage(self):
        self.naviBar()
        self.buttonDrink.grid(row = 5, column = 0, pady = 6, columnspan=2, sticky="ew")
        self.buttonFood.grid(row = 5, column = 2, pady = 6, columnspan=2, sticky="ew")
        self.buttonOther.grid(row = 5, column = 4, pady = 6, columnspan=2, sticky="ew")    

        menuItemButton("hello", "test", "images\images.png").grid(8,0)
        menuItemButton("hello", "test", "images\images.png").grid(8,1)

    def checkOut(self):
        pass
    
    def loginCreateAccount(self): 
        pass

    def payForOrder(self):
        pass

    def itemPage(self): #I haven't decided whether or not to make a page for each item or to do arguments! probably arguements, but TBD! :)
        pass

    def orderStatus(self):
        pass

    def showPages(self): #this is the function that will show everything -> put all visual thingys here!
        self.naviBar()
        self.pages[self.pageIndex]() #if we do arguments for itemPage, use an if statement (if pageIndex != 2)



cafeGUI()