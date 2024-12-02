import tkinter as tk
import Model as m
from PIL import Image, ImageTk
#import controller as c

'''
this class inherits MenuItem from the project skeleton, it just does formatting tkinter things!

Parameters:
    GUI: allows me to perform commands to switch pages (ex command=lambda:self.GUI.itemPage(self))
    img: thumbnail on menu page
    bigImg: big picture on menuItem Page
'''
class menuItemButton (m.MenuItem):  
    instances = [] #holds every instance of the button just in case we need it!
    def __init__(self, GUI, name, description, price, stock, calories, category, img, image):
        m.MenuItem.__init__(self, name, description, price, stock, calories, category, image)
        menuItemButton.instances.append(self)
        self.GUI = GUI
        self.frame = tk.Frame(width=125, height=125,bg="white")
        self.img = tk.PhotoImage(file=img)
        self.image = tk.PhotoImage(file=image)
        self.cart = tk.Button(self.frame, text="Add to Cart", width=10,font=("Times New Roman",8), command=lambda:self.addToCart())
        self.view = tk.Button(self.frame, text="View Item", width=125,font=("Times New Roman",8), image=self.img, command=lambda:self.GUI.itemPage(self))


    def grid(self, r, c):
        self.cart.pack(side="bottom")
        self.view.pack(side="top")
        self.frame.grid(row = r, column = c, pady = 50)
    
    def addToCart(self): # i dont think we need this, but i'll keep it just in case idk
        print("hello")

    #def set_controller(self, c.MenuItemController):
        #self.controller = c.MenuItemController

'''
here is the method I used to make sure we can switch between pages!

def showPages(self, i) - makes sure I can show a certain page at a certain index of the self.pages list

def clearPage(self) - clears all the widgets in a page - run this at the beginning of each function to clear the website!


side note: I created widgets in the __init__ but only put them into a grid in the functions for each page!
'''

class cafeGUI: 
    def __init__(self): #note to self: no widgets should be "run" here! they should only be added to the functions for pages!
        self.root = tk.Tk()
        self.root.geometry("820x560")
        self.root.title("Cafe Webpage") 
        
        self.pageIndex = 0
        self.pages = [self.menuPage, self.checkOut, self.loginCreateAccount, self.payForOrder, self.itemPage, self.orderStatus]
        self.currentItemPage = ""

        #setting 6 columns for this!
        self.root.grid_columnconfigure(0,weight=1)
        self.root.grid_columnconfigure(1,weight=1)
        self.root.grid_columnconfigure(2,weight=1)
        self.root.grid_columnconfigure(3,weight=1)
        self.root.grid_columnconfigure(4,weight=1)
        self.root.grid_columnconfigure(5,weight=1)
        
        # widgets for navigation bar (goes on every page except payForOrder i think??)
        self.searchLabel = tk.Label(self.root, text="search")
        self.searchBox = tk.Entry(self.root)

        # widgets for menuPage
        self.buttonDrink = tk.Button(self.root,text="Drink", width=5,font=("Times New Roman",14))
        self.buttonFood = tk.Button(self.root,text="Food", width=5,font=("Times New Roman",14))
        self.buttonOther = tk.Button(self.root,text="Other", width=5,font=("Times New Roman",14))
        #self.pancakeItem = menuItemButton(self, "pancakes", "description", 2.99, 5, 200, "other", "images\images.png", "images\drink (1).png")
        
        self.item = []
        menu_items = m.MenuItem.getMenuItems(self)
        for menu_item in menu_items:
            name = menu_item[0]
            description = menu_item[1]
            price = menu_item[2]
            stock = menu_item[3]
            calories = menu_item[4]
            category = menu_item[5]
            image = menu_item[6]
            self.item.append(menuItemButton(self, name, description, price, stock, calories, category, "images\images.png", image))



        # widgets for itemPage
        self.itemImg = ""
        self.costLabel = ""
        self.editsLabel = tk.Label(self.root, text="Additional Information:", width=20,font=("Times New Roman",14))
        self.textBox = tk.Text(self.root, height=10, width=20)
        self.itemToCart = tk.Button(self.root, text="Add to Cart", width=10,font=("Times New Roman",8))

        #labels for all food items
        
        self.showPages(0)

    def clearPage(self):
        for i in self.root.winfo_children():
            i.grid_forget()
    
    def naviBar(self):
        self.searchLabel.grid(row = 0, column = 0, pady = 2)
        self.searchBox.grid(row = 0, column = 1, pady = 2, columnspan=2, sticky="ew")

    def menuPage(self):
        self.clearPage()
        self.naviBar()
        self.buttonDrink.grid(row = 5, column = 0, pady = 6, columnspan=2, sticky="ew")
        self.buttonFood.grid(row = 5, column = 2, pady = 6, columnspan=2, sticky="ew")
        self.buttonOther.grid(row = 5, column = 4, pady = 6, columnspan=2, sticky="ew")    

        #self.pancakeItem.grid(8,0)

        self.item[0].grid(8,0)
        self.item[1].grid(8,1)
        self.item[2].grid(8,2)
        self.item[3].grid(8,3)
        self.item[4].grid(8,4)
        self.item[5].grid(9,0)
        self.item[6].grid(9,1)
        

    def checkOut(self):
        self.clearPage()
    
    def loginCreateAccount(self): 
        self.clearPage()

    def payForOrder(self):
        self.clearPage()

    def itemPage(self, item):
        self.clearPage()
        self.naviBar()
        self.itemImg = tk.Label(self.root, image=item.image)
        self.costLabel = tk.Label(self.root, text="Cost: $"+str(item.price), width=20,font=("Times New Roman",14))

        self.itemImg.grid(row=1,column=0, rowspan=4, pady = 10, columnspan=2)
        self.costLabel.grid(row=1, column=3, pady = 10)

        self.editsLabel.grid(row=2,column=3)
        self.textBox.grid(row=3,column=3)

        self.itemToCart.grid(row=4,column=3)

    def orderStatus(self):
        self.clearPage() 

    def showPages(self, i): #this is the function that will show everything -> put all visual thingys here!
        self.pageIndex = i #part of me doesn't think we need this anymore? but i'm too afraid to erase it lmaoooo
        if self.pageIndex != 4: 
            self.pages[self.pageIndex]() 
        else:
            self.pages[self.pageIndex](self.currentItemPage) 



cafeGUI().root.mainloop()