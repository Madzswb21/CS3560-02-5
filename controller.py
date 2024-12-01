# controller

# define a controller class for each class in the system


# define controller for MenuItem
class MenuItemController:
    def __init__(self, MenuItem):
        self.MenuItem = MenuItem

    def createMenuItem(self, name, description, price, stock, calories, category):
        try:
            # create a menu item
            self.MenuItem.name = name
            self.MenuItem.description = description
            self.MenuItem.price = price
            self.MenuItem.stock = stock
            self.MenuItem.calories = calories
            self.MenuItem.category = category
            self.MenuItem.createMenuItem()

            # show add success message

        except ValueError as error:
            # show error message
            print(error)

    def updateMenuItem(self, newName, newDesc, newPrice, newStock, newCalories, newCategory, itemID):
        try:
            # update a menu item
            self.MenuItem.name = newName
            self.MenuItem.description = newDesc
            self.MenuItem.price = newPrice
            self.MenuItem.stock = newStock
            self.MenuItem.calories = newCalories
            self.MenuItem.category = newCategory
            self.MenuItem.updateMenuItem(itemID)

            # show update success message
        except ValueError as error:
            # show error message
            print(error)

    def deleteMenuItem(self, itemID):
        self.MenuItem.deleteMenuItem(itemID)
        # show delete success message 

    # getters from model
    def getMenu(self):
        menu = self.MenuItem.getMenu()
        return menu

    def getFoodMenu(self):
        food = self.MenuItem.getFoodMenu()
        return food

    def getDrinkMenu(self):
        drink = self.MenuItem.getDrinkMenu()
        return drink

    def getOtherMenu(self):
        other = self.MenuItem.getOtherMenu()
        return other

    def getMenuItem(self, itemID):
        item = self.MenuItem.getMenuItem(itemID)
        return item 


        

    
    
