import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from tkinter import messagebox
import Model as m
import login as l



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
        self.delete = tk.Button(self.frame, text="Delete Item", width=10,font=("Times New Roman",8), command=lambda:self.GUI.deleteMenuItemButton(self))
        self.view = tk.Button(self.frame, text="View Item", width=125,font=("Times New Roman",8), image=self.img, command=lambda:self.GUI.itemPage(self))
        self.update = tk.Button(self.frame, text="Update Item", width=10, font=("Times New Roman", 8),
                                command=lambda: self.GUI.updateMenuItemButton(self))

    def grid(self, r, c):
        self.cart.pack(side="bottom")
        self.update.pack(side="bottom")
        self.view.pack(side="top")
        self.delete.pack(side="bottom")
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

class cafeGUI(): 
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
        self.buttonLogin = tk.Button(self.root,text="Login", width=2,font=("Times New Roman",14), command=self.loginCreateAccount)
        self.buttonMenu = tk.Button(self.root,text="Main", width=5,font=("Times New Roman",14), command=self.menuPage)
        self.buttonDrink = tk.Button(self.root,text="Drink", width=5,font=("Times New Roman",14), command=self.drinkMenuPage)
        self.buttonFood = tk.Button(self.root,text="Food", width=5,font=("Times New Roman",14), command=self.foodMenuPage)
        self.buttonOther = tk.Button(self.root,text="Other", width=5,font=("Times New Roman",14), command=self.otherMenuPage)
        #self.pancakeItem = menuItemButton(self, "pancakes", "description", 2.99, 5, 200, "other", "images\images.png", "images\drink (1).png")
        
        # all menu item fetched and stored in menuItemButton
        self.items = []
        menu_items = m.MenuItem.getMenuItems(m.MenuItem)
        for name, description, price, stock, calories, category, image in menu_items:
            self.items.append(menuItemButton(self, name, description, price, stock, calories, category, "images\images.png", image))

        # labels for testing purposes
        self.label1 = tk.Label(self.root, text="menuPage", font=tkFont.Font(family="Times New Roman", size=12))
        self.label2 = tk.Label(self.root, text="checkOut", font=tkFont.Font(family="Times New Roman", size=12))
        self.label3 = tk.Label(self.root, text="loginCreateAccount", font=tkFont.Font(family="Times New Roman", size=12))
        self.label4 = tk.Label(self.root, text="payForOrder", font=tkFont.Font(family="Times New Roman", size=12))
        self.label5 = tk.Label(self.root, text="itemPage", font=tkFont.Font(family="Times New Roman", size=12))
        self.label6 = tk.Label(self.root, text="orderStatus", font=tkFont.Font(family="Times New Roman", size=12))

        # widgets for itemPage
        self.itemImg = ""
        self.costLabel = ""
        self.editsLabel = tk.Label(self.root, text="Additional Information:", width=20,font=("Times New Roman",14))
        self.textBox = tk.Text(self.root, height=10, width=20)
        self.itemToCart = tk.Button(self.root, text="Add to Cart", width=10,font=("Times New Roman",8))
        
        self.showPages(0)

    def clearPage(self):
        for i in self.root.winfo_children():
            i.grid_forget()
    
    def naviBar(self):
        self.searchLabel.grid(row = 0, column = 0, pady = 2)
        self.searchBox.grid(row = 0, column = 1, pady = 2, columnspan=2, sticky="ew")

    def menuPage(self):
        self.label1.grid(row = 1, column = 0, rowspan=5, pady = 2)
        self.clearPage()
        self.naviBar()
        self.buttonLogin.grid(row=3, column = 8, pady = 6)
        self.buttonDrink.grid(row = 5, column = 0, pady = 6, columnspan=2, sticky="ew")
        self.buttonFood.grid(row = 5, column = 2, pady = 6, columnspan=2, sticky="ew")
        self.buttonOther.grid(row = 5, column = 4, pady = 6, columnspan=2, sticky="ew")
        #self.buttonAdd.grid(row = )    

        #self.pancakeItem.grid(8,0)
        
        # grids of all menu items
        row_num = 8
        col_num = 0
        for item in self.items:
            item.grid(row_num, col_num)
            col_num += 1
            if col_num == 6:
                col_num = 0
                row_num += 1

        # only available to staff
            # add menu item button
            # update menu item button
            # remove menu item button


        
    '''
    def removeMenuItemButton(self):
        # fetch menuitemID from selecting the item
        m.MenuItem.deleteMenuItem(self, itemID)
    def updateMenuItemButton(self):
        x=0
    '''
    
    def checkOut(self):
        self.clearPage()
        self.label2.grid(row = 1, column = 0, rowspan=5, pady = 2)
    
    def loginCreateAccount(self): 
        self.clearPage()
        self.loginaccount = l.LoginPage(self)

    def payForOrder(self):
        self.clearPage()
        self.label4.grid(row = 1, column = 0, rowspan=5, pady = 2)

    def itemPage(self, item):
        self.clearPage()
        self.label5.grid(row = 1, column = 0, rowspan=5, pady = 2)
        self.naviBar()
        self.buttonMenu.grid(row = 5, column = 0, pady = 6, columnspan=2, sticky="ew")
        self.buttonDrink.grid(row = 5, column = 2, pady = 6, columnspan=2, sticky="ew")
        self.buttonFood.grid(row = 5, column = 4, pady = 6, columnspan=2, sticky="ew")
        self.buttonOther.grid(row = 5, column = 6, pady = 6, columnspan=2, sticky="ew")

        self.itemImg = tk.Label(self.root, image=item.image)
        self.costLabel = tk.Label(self.root, text="Cost: $"+str(item.price), width=20,font=("Times New Roman",14))

        self.itemImg.grid(row=10,column=0, rowspan=4, pady = 10, columnspan=2)
        self.costLabel.grid(row=10, column=3, pady = 10)

        self.editsLabel.grid(row=11,column=3)
        self.textBox.grid(row=12,column=3)

        self.itemToCart.grid(row=13,column=3)

    def orderStatus(self):
        self.clearPage() 

    def showPages(self, i): #this is the function that will show everything -> put all visual thingys here!
        self.pageIndex = i #part of me doesn't think we need this anymore? but i'm too afraid to erase it lmaoooo
        if self.pageIndex != 4: 
            self.pages[self.pageIndex]() 
        else:
            self.pages[self.pageIndex](self.currentItemPage) 

    def drinkMenuPage(self):
        self.clearPage()
        self.naviBar()
        self.buttonMenu.grid(row = 5, column = 0, pady = 6, columnspan=2, sticky="ew")
        self.buttonFood.grid(row = 5, column = 2, pady = 6, columnspan=2, sticky="ew")
        self.buttonOther.grid(row = 5, column = 4, pady = 6, columnspan=2, sticky="ew")
        # fetch drink items and store them menuItemButton
        drinks = []
        drink_items = m.MenuItem.getDrinkMenu(self)
        for name, description, price, stock, calories, category, image in drink_items:
            drinks.append(menuItemButton(self, name, description, price, stock, calories, category, "images\images.png", image))

        # grids of all drink items 
        row_num = 8
        col_num = 0
        for drink in drinks:
            drink.grid(row_num, col_num)
            col_num += 1
            if col_num == 6:
                col_num = 0
                row_num += 1

    def foodMenuPage(self):
        self.clearPage()
        self.naviBar()
        self.buttonMenu.grid(row = 5, column = 0, pady = 6, columnspan=2, sticky="ew")
        self.buttonDrink.grid(row = 5, column = 2, pady = 6, columnspan=2, sticky="ew")
        self.buttonOther.grid(row = 5, column = 4, pady = 6, columnspan=2, sticky="ew")

        # fetch food items and store them menuItemButton
        foods = []
        food_items = m.MenuItem.getFoodMenu(self)
        for name, description, price, stock, calories, category, image in food_items:
            foods.append(menuItemButton(self, name, description, price, stock, calories, category, "images\images.png", image))

        # grids of all food items 
        row_num = 8
        col_num = 0
        for food in foods:
            food.grid(row_num, col_num)
            col_num += 1
            if col_num == 6:
                col_num = 0
                row_num += 1

    def otherMenuPage(self):
        self.clearPage()
        self.naviBar()
        self.buttonMenu.grid(row = 5, column = 0, pady = 6, columnspan=2, sticky="ew")
        self.buttonFood.grid(row = 5, column = 2, pady = 6, columnspan=2, sticky="ew")
        self.buttonDrink.grid(row = 5, column = 4, pady = 6, columnspan=2, sticky="ew")

        # fetch other items and store them menuItemButton
        otherItems = []
        other_items = m.MenuItem.getOtherMenu(self)
        for name, description, price, stock, calories, category, image in other_items:
            otherItems.append(menuItemButton(self, name, description, price, stock, calories, category, "images\images.png", image))

        # grids of all other items 
        row_num = 8
        col_num = 0
        for other in otherItems:
            other.grid(row_num, col_num)
            col_num += 1
            if col_num == 6:
                col_num = 0
                row_num += 1
    
    def addMenuItemButton(self):
        x=0

    
    def updateMenuItemButton(self, item):
        self.clearPage()
        self.naviBar()

        # Display entry fields for updating item
        tk.Label(self.root, text="Update Menu Item", font=("Times New Roman", 16)).grid(row=2, column=1, columnspan=2, pady=10)

        fields = ["Name", "Description", "Price", "Stock", "Calories", "Category"]
        current_values = [item.name, item.description, item.price, item.stock, item.calories, item.category]
        entries = {}

        
        for i, field in enumerate(fields):
            tk.Label(self.root, text=f"{field}:", font=("Times New Roman", 12)).grid(row=i + 5, column=0, padx=10, pady=10)
            entry = tk.Entry(self.root, width=50, font=("Times New Roman", 12))
            entry.insert(0, current_values[i])
            entry.grid(row=i + 5, column=1, padx=20, pady=10)
            entries[field.lower()] = entry
    
        def submitUpdate():
            updated_values = {key: entries[key].get() for key in entries}
            try:
                item.name = updated_values["name"]
                item.description = updated_values["description"]
                item.price = float(updated_values["price"])
                item.stock = int(updated_values["stock"])
                item.calories = int(updated_values["calories"])
                item.category = updated_values["category"]

                itemID = m.MenuItem.getItemID(item.name)
                item.updateMenuItem(itemID)  # Update in backend
                self.menuPage()  # Refresh menu page
                tk.messagebox.showinfo("Update Successful", f"'{item.name}' has been updated successfully!")
            except Exception as e:
                tk.messagebox.showerror("Error", f"Failed to update item: {e}")
        
        tk.Button(self.root, text="Submit", font=("Times New Roman", 12), command=submitUpdate).grid(row=len(fields) + 5, column=1, pady=10)
        tk.Button(self.root, text="Cancel", font=("Times New Roman", 12), command=self.menuPage).grid(row=len(fields) + 6, column=1, pady=10)


    def deleteMenuItemButton(self, item):
        #show message to confirm the decision
        response = tk.messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete '{item.name}'?")
        if response:
        
            if m.MenuItem.deleteMenuItem(self, item.name):
                tk.messagebox.showinfo("Success", f"The item '{item.name}' has been successfully deleted.")
            else:
                tk.messagebox.showerror("Error", f"The item '{item.name} is still in stock, it cannot be deleted.")
    

        # all menu item fetched and stored in menuItemButton
        self.items = []
        menu_items = m.MenuItem.getMenuItems(m.MenuItem)
        for name, description, price, stock, calories, category, image in menu_items:
            self.items.append(menuItemButton(self, name, description, price, stock, calories, category, "images\images.png", image))
        self.menuPage()


    def orderList(self):
        order_list = ttk.Treeview(self)

        order_list['column'] = ("Order ID", "Order Type", "Status", "Payment Date", "Total Cost")


cafeGUI().root.mainloop()