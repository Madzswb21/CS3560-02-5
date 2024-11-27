'''

# what works:
    # createCustomer()
    # createStaff()
    # createOrder()
        # createOnlineOrder() and createInPersonOrder() also work, but
        # only with placeholder "dummy variables"
    # createMenuItem()
    # addItemsToOrder()
    # removeItemsFromOrder()
    
# what needs to work
    # payOrder()
    # checkOrderStatus()
    # updateOrderStatus()
#
    
'''

import mysql.connector # make sure yu have connector set up or else this won't work!
import random # used for orderID generation

# sets up connection to existing database "CafeRestaurant"
    # note for team: you might have to change user and password values
    # depending on how you set up YOUR local server :)
db = mysql.connector.connect(
    host = "localhost",
    user = "root", 
    password = "yomama",
    database = "CafeRestaurant"
)

# acts as the "connection" to the database, used to write queries back to db
cursor = db.cursor(buffered=True)

# functions for altering databse table values, etc.

# creating an instance of the Customer class to put into database
def createCustomer(fName, lName, emailAddress, phoneNumber, physAddress):
    cursor.execute("INSERT INTO Customer (f_name, l_name, emailAddress, phoneNumber, physAddress) VALUES (%s,%s,%s,%s,%s)",
                 (fName, lName, emailAddress, phoneNumber, physAddress))
    db.commit()
    print("The customer has been created!")

# creating an instance of Orders class to put into database, 
# then uses ID created in database to create an online or in-person order
def createOrder(orderType):
    orderID = generateOrderID()
    cursor.execute("INSERT INTO Orders (orderID, orderType) VALUES (%s, %s)", (orderID, orderType))
    db.commit()
    print("The order has been created!")

    if (orderType == "online"):
        createOnlineOrder(orderID)
    else:
        createInPersonOrder(orderID)
    


# create an instance of the Online Order class
def createOnlineOrder(onlineID):
    # need to do "something" here that gets the rest of the needed attributes
    # below are placeholders for testing:
    custID = 2000
    orderStatus = "active"
    paymentDate = "now"
    addComments = "none"
    totalCost = 0.00
    pickupTime = "12:00"
    # end of placeholders

    cursor.execute("INSERT INTO OnlineOrder (onlineID, custID, orderStatus, paymentDate, addComments, totalCost, pickupTime) VALUES (%s,%s,%s,%s,%s,%s,%s)",
        (onlineID, custID, orderStatus, paymentDate, addComments, totalCost, pickupTime))
    db.commit()
    


# create an instance of the In-Person Order class
def createInPersonOrder(inPersonID):
    # need to do "something" here that gets the rest of the needed attributes
    # below are placeholders for testing:
    staffID = 1000
    orderStatus = "active"
    paymentDate = "now"
    addComments = "none"
    totalCost = 0.00
    tableNum = 4
    # end of placeholders

    cursor.execute("INSERT INTO InPersonOrder (inPersonID, staffID, orderStatus, paymentDate, addComments, totalCost, tableNum) VALUES (%s,%s,%s,%s,%s,%s,%s)", 
        (inPersonID, staffID, orderStatus, paymentDate, addComments, totalCost, tableNum))
    db.commit()



# only available to staff members!!
# create an instance of Menu Item class
    # this one may be a bit tricky to implement to GUI, works fine in query
    # but may cause issue with button and image display on GUI
def createMenuItem():
    itemName = input("Name: ")
    itemDesc = input("Description: ")
    try:
        itemPrice = float(input("Price: "))
    except ValueError:
        print("Error.")
    stock = input("Stock: ")
    calories = input("Calories: ")
    category = input("Category: ")      # is it possible to implement radio button for this (food/drink/other)?
    cursor.execute("INSERT INTO MenuItem (itemName, itemDesc, itemPrice, stock, calories, category) VALUES (%s,%s,%s,%s,%s,%s)", 
        (itemName, itemDesc, itemPrice, stock, calories, category))
    db.commit()

# implement this function as a delete button next to the menu item
# only available to staff
def deleteMenuItem(menuItemID):
    cursor.execute("DELETE FROM MenuItem WHERE menuItemID = (%s)", (menuItemID,))
    db.commit()
# all functions to view menu are available to all
def viewMenu():
    cursor.execute("SELECT itemName, itemPrice FROM MenuItem")
    # implement GUI to display all menu items
    for x in cursor:
        print(x)
    db.commit()

# function to view drink only menu
def viewDrinkMenu():
    cursor.execute("SELECT itemName, itemPrice FROM MenuItem WHERE category = 'drink'")
    # implement GUI to display
    for x in cursor:
        print(x)
    db.commit()

# function to view food only menu
def viewFoodMenu():
    cursor.execute("SELECT itemName, itemPrice FROM MenuItem WHERE category = 'food'")
    # implement GUI to display all menu items
    for x in cursor:
        print(x)
    db.commit()

# function to view other category
def viewOtherMenu():
    cursor.execute("SELECT itemName, itemPrice FROM MenuItem WHERE category = 'other'")
    # implement GUI to display all menu items
    for x in cursor:
        print(x)
    db.commit()

# function to view a menu item 
# show name, desc, price, and calories
def viewMenuItem(menuItemID):
    cursor.execute("SELECT itemName, itemDesc, itemPrice, calories FROM MenuItem WHERE menuItemID = (%s)", (menuItemID,))
    print(cursor.fetchall())
    db.commit()

# takes in an order's ID and a menu item's ID to add an item
# from the menu to a specific order
def addItemsToOrder(orderID, menuItemID, quantity):
    cursor.execute("INSERT INTO ItemsInOrder (orderID, menuItemID, quantity) VALUES (%s,%s,%s)",
                   (orderID, menuItemID, quantity))
    db.commit()

    orderType = getOrderType(orderID)
    totalCost = getTotalCost(orderID)
    itemCost = getItemPrice(menuItemID)
    itemCost = itemCost * quantity
    
    totalCost = totalCost + itemCost

    # updates respective total cost in order
    if(orderType == "online"):
        cursor.execute("UPDATE OnlineOrder SET totalCost = (%s) WHERE onlineID = (%s)",
                       (totalCost, orderID))
    else:
        cursor.execute("UPDATE InPersonOrder SET totalCost = (%s) WHERE inPersonID = (%s)",
                       (totalCost, orderID))
    db.commit()

 

# takes same parameters as "addItemsToOrder" but removes an itemInOrder
def removeItemsFromOrder(orderID, menuItemID):
    orderType = getOrderType(orderID)
    totalCost = getTotalCost(orderID)
    itemCost = getItemPrice(menuItemID)
    quantity = getQuantity(orderID, menuItemID)
    removeCost = itemCost * quantity

    totalCost = totalCost - removeCost

    # will change the totalCost in the respective order
    if(orderType == "online"):
        cursor.execute("UPDATE OnlineOrder SET totalCost = (%s) WHERE onlineID = (%s)",
                       (totalCost, orderID))
    else:
        cursor.execute("UPDATE InPersonOrder SET totalCost = (%s) WHERE inPersonID = (%s)",
                       (totalCost, orderID))
    db.commit()

    # removes item that user wanted to remove
    cursor.execute("DELETE FROM ItemsInOrder WHERE orderID = (%s) and menuItemID = (%s)",
                   (orderID, menuItemID))
    db.commit()

    # end removeItemsToOrder




# update the value of the order's "orderStatus" and "paymentDate"
def payOrder(orderID, personID):
    x=0

# takes an order ID and returns its current status (ready for pickup, cooking, etc.)
def checkOrderStatus(orderID):
    x=0

# only available to staff members!!
# takes a staff member's ID, and allows them to update the staus of an order
# once it is finished cooking, if it gets cancelled/postponed, etc.
def updateOrderStatus(staffID, orderID):
    x=0


# internal functions used by larger functions (makes code cleaner)

def getOrderType(orderID):
    cursor.execute("SELECT orderType FROM Orders WHERE orderID = (%s)", (orderID,))
    orderType = cursor.fetchone()
    orderType = orderType[0]
    return orderType

def getTotalCost(orderID):
    orderType = getOrderType(orderID)
    if(orderType == "online"):
        cursor.execute("SELECT totalCost FROM OnlineOrder WHERE onlineID = (%s)", (orderID,))
    else:
        cursor.execute("SELECT totalCost FROM InPersonOrder WHERE inPersonID = (%s)", (orderID,))
    
    totalCost = cursor.fetchone()
    totalCost = totalCost[0]
    return totalCost

def getItemPrice(menuItemID):
    cursor.execute("SELECT itemPrice FROM MenuItem WHERE menuItemID = (%s)", (menuItemID,))
    itemPrice = cursor.fetchone()
    itemPrice = itemPrice[0]
    return itemPrice

def getQuantity(orderID, menuItemID):
    cursor.execute("SELECT quantity FROM ItemsInOrder WHERE orderID = (%s) and menuItemID = (%s)", 
                   (orderID, menuItemID))
    quantity = cursor.fetchone()
    quantity = quantity[0]
    return quantity


def generateOrderID():
    orderID = random.randint(1, 100000)
    cursor.execute("SELECT orderID FROM Orders")
    orderCheck = cursor.fetchone()

    if orderCheck is not None:
        cursor.execute("SELECT orderID FROM Orders")
        orderList = cursor.fetchall()
        for order in orderList:
            if(order == orderID):
                generateOrderID()
            else:
                return orderID
    else:
        return orderID



# practice
'''
createOrder("online")
createOrder("online")
createOrder("inperson")
createOrder("inperson")
'''
'''
addItemsToOrder(30602, 1, 2)
addItemsToOrder(50014, 5, 1)
addItemsToOrder(59530, 10, 1)
addItemsToOrder(85655, 15, 2)
'''
'''
removeItemsFromOrder(30602, 1)
removeItemsFromOrder(50014, 5)
removeItemsFromOrder(59530, 10)
removeItemsFromOrder(85655, 15)
'''