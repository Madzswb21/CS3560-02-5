

# test file to combine project skeleton and sqlconnector

import mysql.connector # make sure yu have connector set up or else this won't work!
import random # used for orderID generation
import hashlib 

# sets up connection to existing database "CafeRestaurant"
    # note for team: you might have to change user and password values
    # depending on how you set up YOUR local server :)
db = mysql.connector.connect(
    host = "localhost",
    user = "root", 
    password = "stella96",
    database = "caferestaurant"
)

# acts as the "connection" to the database, used to write queries back to db
cursor = db.cursor(buffered=True)

# define class Customer
class Customer:
    def __init__(self, username, password, fName, lName, emailAddress, phoneNumber, physAddress):
        self.username = username
        self.password = password
        self.fName = fName
        self.lName = lName
        self.emailAddress = emailAddress
        self.phoneNumber = phoneNumber
        self.physAddress = physAddress

    '''
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, value):
        self.__password = hashlib.sha256(value.encode()).hexdigest()
        '''

    # create a customer account
    def createCustomer(self):
        cursor.execute("INSERT INTO Customer (username, pass, f_name, l_name, emailAddress, phoneNumber, physAddress) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                 (self.username, self.password, self.fName, self.lName, self.emailAddress, self.phoneNumber, self.physAddress))
        db.commit()
        print("The customer has been created!")

    # function to check log in
    def login(self):
        '''
        cursor.execute("SELECT custID FROM Customer WHERE username = %s AND pass = %s", (self.username, self.password))
        custID = cursor.fetchone()
        custID = custID[0]
        if custID:
            return custID
        else:
            print("Login error!")  
            '''

        try:
            #Execute the SQL query
            cursor.execute("SELECT custID FROM Customer WHERE username = %s AND pass = %s", (self.username, self.password))
            result = cursor.fetchone()

            #Check if the result is not None
            if result:
                custID = result[0]
                print("Login successful!")
                return custID  # Return the customer ID upon successful login
            else:
                print("Invalid username or password.")
                return None
        except Exception as e:
            print(f"An error occurred during login: {e}")
            return None 
  

class Staff:
    def __init__(self, username, password, fName, lName, emailAddress, phoneNumber, staffRole):
        self.username = username
        self.password = password
        self.fName = fName
        self.lName = lName
        self.emailAddress = emailAddress
        self.phoneNumber = phoneNumber
        self.staffRole = staffRole

    '''
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, value):
        self.__password = hashlib.sha256(value.encode()).hexdigest()
        '''

    # create a staff account
    def createStaff(self):
        cursor.execute("INSERT INTO Staff (username, pass, f_name, l_name, emailAddress, phoneNumber, staffRole) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                 (self.username, self.password, self.fName, self.lName, self.emailAddress, self.phoneNumber, self.staffRole))
        db.commit()
        print("The staff has been created!")

    # function to check log in
    def login(self):
        try:
            #Execute the SQL query
            cursor.execute("SELECT staffID FROM Staff WHERE username = %s AND pass = %s", (self.username, self.password))
            result = cursor.fetchone()

            #Check if the result is not None
            if result:
                staffID = result[0]
                print("Login successful!")
                return staffID  # Return the customer ID upon successful login
            else:
                print("Invalid username or password.")
                return None
        except Exception as e:
            print(f"An error occurred during login: {e}")
            return None
        
        cursor.execute("SELECT staffID FROM Staff WHERE username = %s AND pass = %s", (self.username, self.password))
        staffID = cursor.fetchone()
        staffID = staffID[0]
        if staffID:
            return staffID
        else:
            print("Login error!") 



# define class MenuItem
class MenuItem:
    def __init__(self, name, description, price, stock, calories, category, image):
        self.description = description
        self.name = name
        self.price = price
        self.stock = stock
        self.calories = calories
        self.category = category
        self.image = image

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        """
        validate the price
        :param value:
        :return:
        """
        try:
            self.__price = float(value)
        except ValueError:
            print(f'Invalid price')

    # only available to staff members!!
    # create an instance of Menu Item class
        # this one may be a bit tricky to implement to GUI, works fine in query
        # but may cause issue with button and image display on GUI
    def createMenuItem(self):

        # add to database
        cursor.execute("INSERT INTO MenuItem (itemName, itemDesc, itemPrice, stock, calories, category, image) VALUES (%s,%s,%s,%s,%s,%s, %s)", 
            (self.name, self.description, self.price, self.stock, self.calories, self.category, self.image))
        db.commit()

    # implement this function as a delete button next to the menu item
    # only available to staff
    def deleteMenuItem(self, itemName):
        try:
            # get stock number
            cursor.execute("SELECT stock FROM MenuItem WHERE itemName = (%s)", (itemName,))
            stock = cursor.fetchone()
            stock = stock[0]

            # only delete an item if stock is 0
            if stock == 0:
                cursor.execute("DELETE FROM MenuItem WHERE itemName = (%s)", (itemName,))
                db.commit()
                return True
            else:
                raise Exception(f'This item is still available, cannot be deleted.')
        except Exception as e:
            print(e)
            return False
    

    # function to update menu item
    # only available to staff
    def updateMenuItem(self,itemID):

        cursor.execute("UPDATE MenuItem SET itemName = (%s), itemDesc = (%s), itemPrice = (%s), stock = (%s), calories = (%s), category = (%s) WHERE menuItemID = (%s)", 
            (self.name, self.description, self.price, self.stock, self.calories, self.category, itemID)) 
        db.commit()

    # all functions to view menu are available to all
    def getMenu(self):
        cursor.execute("SELECT itemName, itemPrice FROM MenuItem")
        # implement GUI to display all menu items
        menu = cursor.fetchall()
        #for x, y in menu:   # use this for gui to populate the main menu page with grid 
            #print(x, "and", y)
        db.commit()
        return menu

    # function to view drink only menu
    def getDrinkMenu(self):
        cursor.execute("SELECT itemName, itemDesc, itemPrice, stock, calories, category, image FROM MenuItem WHERE category = 'drink'")
        # implement GUI to display
        drink_items = cursor.fetchall()
        #for x, y in drink_items:
            #print(x, "and", y)
        db.commit()
        return drink_items

    # function to view food only menu
    def getFoodMenu(self):
        cursor.execute("SELECT itemName, itemDesc, itemPrice, stock, calories, category, image FROM MenuItem WHERE category = 'food'")
        # implement GUI to display all menu items
        food_items = cursor.fetchall()
        #for x, y in food_items:
            #print(x, "and", y)
        db.commit()
        return food_items

    # function to view other category
    def getOtherMenu(self):
        cursor.execute("SELECT itemName, itemDesc, itemPrice, stock, calories, category, image FROM MenuItem WHERE category = 'other'")
        # implement GUI to display all menu items
        other_items = cursor.fetchall()
        #for x , y in other_items:
            #print(x, "and", y)
        db.commit()
        return other_items

    # function to view a menu item 
    # show name, desc, price, and calories
    def getMenuItems(self):
        cursor.execute("SELECT itemName, itemDesc, itemPrice, stock, calories, category, image FROM MenuItem")
        menu_items = cursor.fetchall()
        #for menu_item in menu_items:
            #print(menu_item[0], "and", menu_item[1])
        db.commit()
        return menu_items
    
    # function to fetch all menu names
    def getMenuName(self):
        cursor.execute("SELECT itemName, itemDesc, itemPrice from MenuItem")
        menu_name = cursor.fetchall()
        db.commit()
        return menu_name
    
    # function to fetch menuItemID by name
    def getItemID(self):
        cursor.execute("SELECT menuItemID from MenuItem WHERE itemName = %s", (self.name,))
        itemID = cursor.fetchone()
        itemID = itemID[0]
        db.commit()
        return itemID

# define Order class
class Order:
    def __init__(self, orderID, orderType):
        self.orderID = orderID
        self.orderType = orderType
    
    # generate orderID
    def generateOrderID(self):
        orderID = random.randint(1, 100000)
        cursor.execute("SELECT orderID FROM Orders")
        orderCheck = cursor.fetchone()

        if orderCheck is not None:
            cursor.execute("SELECT orderID FROM Orders")
            orderList = cursor.fetchall()
            for order in orderList:
                if(order == orderID):
                    self.generateOrderID()
                else:
                    return orderID
        else:
            return orderID
    
    
    # creating an instance of Orders class to put into database, 
    # then uses ID created in database to create an online or in-person order
    def createOrder(self):
        self.orderID = self.generateOrderID()
        cursor.execute("INSERT INTO Orders (orderID, orderType) VALUES (%s, %s)", (self.orderID, self.orderType))
        db.commit()
        print("The order has been created!")
        
        return self.orderID
    
    def payOrder(self): # this function needs orderID input (store current orderID in self.orderID)
        # Check if the order exists and get order details
        orderType = self.getOrderType()

        if orderType == "online":
            cursor.execute("SELECT * FROM OnlineOrder WHERE onlineID = (%s)", (self.orderID,))
        else:
            cursor.execute("SELECT * FROM InPersonOrder WHERE inPersonID = (%s)", (self.orderID,))

        order = cursor.fetchone()
        if not order:
            print("Order not found.")
            return

        #Update the order status to 'paid'
        if orderType == "online":
            cursor.execute("UPDATE OnlineOrder SET orderStatus = 'paid', paymentDate = NOW() WHERE onlineID = (%s)", (self.orderID,))
        else:
            cursor.execute("UPDATE InPersonOrder SET orderStatus = 'paid', paymentDate = NOW() WHERE inPersonID = (%s)", (self.orderID,))
        db.commit()

        #Update the stock of each menu item in the order
        cursor.execute("SELECT menuItemID, quantity FROM ItemsInOrder WHERE orderID = (%s)", (self.orderID,))
        items = cursor.fetchall()

        for item in items:
            menuItemID, quantity = item
            cursor.execute("SELECT stock FROM MenuItem WHERE menuItemID = (%s)", (menuItemID,))
            stock = cursor.fetchone()[0]

            if stock >= quantity:
                new_stock = stock - quantity
                cursor.execute("UPDATE MenuItem SET stock = (%s) WHERE menuItemID = (%s)", (new_stock, menuItemID))
            else:
                print(f"Not enough stock for item ID {menuItemID}. Cannot complete order.")
                return
            
        # delete all items in order


        db.commit()
        print("Order has been paid and stock updated.") 

    def updateOrderStatus(self, staffID, newStatus):  #needs orderID, staffID, newStatus (text entry) input
        #Check if the staff member exists
        cursor.execute("SELECT * FROM Staff WHERE staffID = (%s)", (staffID,))
        staff = cursor.fetchone()
        if not staff:
            print("Staff member not found. Access denied.")
            return

        #Get the current status of the order
        orderType = self.getOrderType()
        if orderType == "online":
            cursor.execute("SELECT orderStatus FROM OnlineOrder WHERE onlineID = (%s)", (self.orderID,))
        else:
            cursor.execute("SELECT orderStatus FROM InPersonOrder WHERE inPersonID = (%s)", (self.orderID,))

        orderStatus = cursor.fetchone()
        if not orderStatus:
            print("Order not found.")
            return

        #Prompt staff to enter the new status for the order
        #newStatus = input("Enter the new status for the order (e.g., 'cooking', 'ready for pickup', 'completed', 'cancelled'): ")

        #Update the order status
        if orderType == "online":
            cursor.execute("UPDATE OnlineOrder SET orderStatus = (%s) WHERE onlineID = (%s)", (newStatus, self.orderID))
        else:
            cursor.execute("UPDATE InPersonOrder SET orderStatus = (%s) WHERE inPersonID = (%s)", (newStatus, self.orderID))

        # if order gets picked up, staff updates completed, pickupTime is also updated
        if self.orderStatus == 'completed':
            cursor.execute("UPDATE OnlineOrder SET pickupTime = NOW()")
        db.commit()

        print(f"Order status has been updated to: {self.orderStatus}")

    def checkOrderStatus(self): # needs orderID input
        #Check if the order exists and get its status
        orderType = self.getOrderType()

        if orderType == "online":
            cursor.execute("SELECT orderStatus FROM OnlineOrder WHERE onlineID = (%s)", (self.orderID,))
        else:
            cursor.execute("SELECT orderStatus FROM InPersonOrder WHERE inPersonID = (%s)", (self.orderID,))

        orderStatus = cursor.fetchone()
        if not orderStatus:
            print("Order not found.")
            return

        print(f"The current status of the order is: {orderStatus[0]}")
        return orderStatus[0]

    def getOrderType(self):
        cursor.execute("SELECT orderType FROM Orders WHERE orderID = (%s)", (self.orderID,))
        orderType = cursor.fetchone()
        orderType = orderType[0]
        db.commit()
        return orderType
    


# define OnlineOrder class
class OnlineOrder(Order):
    def __init__(self, onlineID, orderStatus, paymentDate, addComments, totalCost, pickupTime):
        self.onlineID = onlineID
        self.orderStatus = orderStatus
        self.paymentDate = paymentDate
        self.addComments = addComments
        self.totalCost = totalCost
        self.pickupTime = pickupTime

    # create an instance of order if no order is active
    # 1st instance of order has no payment date, no comments, 0 cost, no pickupTime
    def createOnlineOrder(self, custID):  # needs customerID input
        self.orderType = 'online'
        self.onlineID = self.createOrder()
        self.orderStatus = 'active'
        self.totalCost = 0.00
        cursor.execute("INSERT INTO OnlineOrder (onlineID, custID, orderStatus, totalCost) VALUES (%s,%s,%s,%s)",
        (self.onlineID, custID, self.orderStatus, self.totalCost))
        db.commit()


# define InPersonOrder class
class InPersonOrder(Order):
    def __init__(self, inPersonID, orderStatus, paymentDate, addComments, totalCost, tableNum):
        self.inPersonID = inPersonID
        self.orderStatus = orderStatus
        self.paymentDate = paymentDate
        self.addComments = addComments
        self.totalCost = totalCost
        self.tableNum = tableNum

    # create an instance of order if no order is active
    # 1st instance of order has no payment date, no comments, no cost, no pickupTime
    def createInPersonOrder(self, staffID): # nees staffID input
        self.orderType = 'in person'
        self.inPersonID = self.createOrder()
        self.orderStatus = 'active'
        self.totalCost = 0.00
        cursor.execute("INSERT INTO InPersonOrder (inPersonID, staffID, orderStatus, totalCost) VALUES (%s,%s,%s,%s)",
        (self.inPersonID, staffID, self.orderStatus, self.totalCost))
        db.commit()

    '''
    def removeInPersonOrder(self):
        cursor.execute("DELETE FROM InPersonOrder WHERE inPersonID = %s", (self.inPersonID,))
        cursor.execute("DELETE FROM Orders WHERE orderID = %s", (self.inPersonID,))

        db.commit()
        '''
    

# define ItemInOrder class
class ItemsInOrder:
    def __init__(self, quantity, customization):    
        self.quantity = quantity
        self.customization = customization

    # create a popup-like window to input selection
    # use combobox to make dropdown menu for item name
    # show items in the order in treeview
    def addItemsToOrder(self, menuItemID, orderID): # needs menuItemID (fetched using itemName), orderID, quantity, customization input
        cursor.execute("INSERT INTO ItemsInOrder (orderID, menuItemID, quantity, customization) VALUES (%s,%s,%s,%s)",
                   (orderID, menuItemID, self.quantity, self.customization))
        db.commit()

        orderType = self.getOrderType(orderID)
        totalCost = self.getTotalCost(orderID)
        itemCost = self.getItemPrice(menuItemID)
        itemCost = itemCost * self.quantity
        
        totalCost = totalCost + itemCost

        # updates respective total cost in order
        if(orderType == "online"):
            cursor.execute("UPDATE OnlineOrder SET totalCost = (%s) WHERE onlineID = (%s)",
                        (totalCost, orderID))
        else:
            cursor.execute("UPDATE InPersonOrder SET totalCost = (%s) WHERE inPersonID = (%s)",
                        (totalCost, orderID))
            
        db.commit()
    
    def removeItemsFromOrder(self, menuItemID, orderID): # needs menuItemID (fetched using itemName), orderID

        orderType = self.getOrderType(orderID)
        totalCost = self.getTotalCost(orderID)
        itemCost = self.getItemPrice(menuItemID)
        quantity = self.getQuantity(menuItemID, orderID)
        removeCost = itemCost * quantity

        totalCost = totalCost - removeCost

        # remove item from database
        cursor.execute("DELETE FROM ItemsInOrder WHERE menuItemID = %s AND orderID = %s",
                   (menuItemID, orderID))
        
        db.commit()

        # will change the totalCost in the respective order
        if(orderType == "online"):
            cursor.execute("UPDATE OnlineOrder SET totalCost = (%s) WHERE onlineID = (%s)",
                        (totalCost, orderID))
        else:
            cursor.execute("UPDATE InPersonOrder SET totalCost = (%s) WHERE inPersonID = (%s)",
                        (totalCost, orderID))
        db.commit()

    # internal functions used by larger functions (makes code cleaner)

    def getOrderType(self, orderID):
        cursor.execute("SELECT orderType FROM Orders WHERE orderID = (%s)", (orderID,))
        orderType = cursor.fetchone()
        orderType = orderType[0]
        db.commit()
        return orderType

    def getTotalCost(self, orderID):
        orderType = self.getOrderType(orderID)
        if(orderType == "online"):
            cursor.execute("SELECT totalCost FROM OnlineOrder WHERE onlineID = (%s)", (orderID,))
        else:
            cursor.execute("SELECT totalCost FROM InPersonOrder WHERE inPersonID = (%s)", (orderID,))
        
        totalCost = cursor.fetchone()
        totalCost = totalCost[0]
        db.commit()
        return totalCost

    def getItemPrice(self, menuItemID):
        cursor.execute("SELECT itemPrice FROM MenuItem WHERE menuItemID = (%s)", (menuItemID,))
        itemPrice = cursor.fetchone()
        itemPrice = itemPrice[0]
        return itemPrice

    def getQuantity(self, menuItemID, orderID):
        cursor.execute("SELECT quantity FROM ItemsInOrder WHERE orderID = (%s) and menuItemID = (%s)", 
                    (orderID, menuItemID))
        quantity = cursor.fetchone()
        quantity = quantity[0]
        return quantity




menuitem = MenuItem('name', 'desc', 5, 5, 100, 'food', 'img.png')
#menuitem.createMenuItem()

#menuitem.getMenuItems()
customer = Customer('qlam', '123456', 'Quynh', 'Lam', 'qlam@cpp.edu', '111-222-3333', '1000 Main St.')

#custID = customer.login()
#print(custID)
#customer.createCustomer()

staff = Staff('qlam', '123456', 'Quynh', 'Lam', 'qlam@cpp.edu', '111-222-3333', 'server')
#staff.createStaff()
#staffID = staff.login()

order = Order(10000, 'online')

onlineorder = OnlineOrder (10000, 'none', '1/1/2000', 'none', '5.00', '12:00')

#onlineorder.createOnlineOrder(custID)

#onlineorder.removeOnlineOrder(61890)

inpersonorder = InPersonOrder(10000, 'none', '1/1/2000', 'none', 5.00, 12)
#inpersonorder.createInPersonOrder(staffID)
#inpersonorder.removeInPersonOrder(32627)    


iteminorder = ItemsInOrder(1, 'none')
#iteminorder.addItemsToOrder(4, 89815)
#iteminorder.removeItemsFromOrder(4, 61890)
#iteminorder.addItemsToOrder(4, 32627)
#iteminorder.removeItemsFromOrder(4, 32627)


#order.orderID = 89815
#order.checkOrderStatus()
#order.payOrder()
#order.updateOrderStatus(1002)