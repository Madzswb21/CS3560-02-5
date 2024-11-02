# System Classes Skeleton

# superclass to provide attributes to subclasses Staff and Customer
class User:
    def __init__(self, name, emailAddress, phoneNumber):
        self.name = name
        self.emailAddress = emailAddress
        self.phoneNumber = phoneNumber

# id_counter is used to keep track of instances from both
# Staff and Customer classes; ID for customer/staff members 
# will be automatically assigned at instantiation

# subclass to create a Staff user, inherits from User superclass
class Staff(User):
    id_counter = 0 # keeping track of Staff IDs
    def __init__(self, name, emailAddress, phoneNumber, role):
        User.__init__(self, name, emailAddress, phoneNumber)
        self.staffID = "0" + str(Staff.id_counter) # concatenates a 0 on a staff ID number to designate it as a staff member
        self.role = role
        Staff.id_counter += 1

    def __str__(self): # displays vital information pertaining to Staff object
        return f"Name: {self.name} \nEmail Address: {self.emailAddress} \nPhone Number: {self.phoneNumber} \nID Number: {self.staffID} \nRole: {self.role}"

# subclass to create a Customer user, inherits from User superclass
class Customer(User):
    id_counter = 0 # keeping track of Customer IDs
    def __init__(self, name, emailAddress, phoneNumber):
        User.__init__(self, name, emailAddress, phoneNumber)
        self.customerID = "1" + str(Staff.id_counter) # concatenates a 1 on a customer ID number to designate it as a customer
        Staff.id_counter += 1

    def __str__(self): # displays vital information pertaining to Customer object
        return f"Name: {self.name} \nEmail Address: {self.emailAddress} \nPhone Number: {self.phoneNumber} \nID Number: {self.customerID} "


class Order: # Thuan-Thien
    def __init__(order, orderID, itemOrderID, additional_comments, paymentDate, totalCost, orderStatus):
        order.orderID = orderID
        order.itemOrderID = itemOrderID
        order.additional_comments = additional_comments
        order.paymentDate = paymentDate
        order.totalCost = totalCost
        order.orderStatus = orderStatus

    def __str__(order):
        return f"OrderID: {order.orderID}, ItemOrderID: {order.itemOrderID}, Additional Comments: {order.additional_comments}, Payment Date: {order.paymentDate}, Total Cost: ${order.totalCost:.2f}, Order Status: {order.orderStatus}"

    def update_status(order, new_status):
        order.orderStatus = new_status

    def add_comments(order, comments):
        order.additional_comments = comments

class Online_Order(Order): # Thuan-Thien
    def __init__(order, orderID, itemOrderID, additional_comments, paymentDate, totalCost, orderStatus, customerID):
        online().__init__(orderID, itemOrderID, additional_comments, paymentDate, totalCost, orderStatus)

        order.customerID = customerID

    def __str__(order):
        return online().__str__() + f", CustomerID: {order.customerID}"
class In_Person_Order(Order): # Thuan-Thien
    def __init__(order, orderID, itemOrderID, additional_comments, paymentDate, totalCost, orderStatus, staffID):
        inPerson().__init__(orderID, itemOrderID, additional_comments, paymentDate, totalCost, orderStatus)

        order.staffID = staffID

    def __str__(self):
        return inPerson().__str__() + f", StaffID: {self.staffID}"

class Menu: # Quynh
    id_counter = 0 # keep track of Menu ID
    def __init__(self, mealType, itemsInMenu):
        self.mealType = mealType
        self.itemsInMenu = itemsInMenu  # list attribute for itemsInMenu
        self.menuID = "3" + str(Menu.id_counter)
        Menu.id_counter += 1

    def __str__(self): # display info of each Menu object
        items_str = "\n - ".join(self.itemsInMenu) # each item is on a new line
        return f"Meal Type: {self.mealType} \nItems In Menu:\n - {self.items_str} "
        

class MenuItem: # Quynh
    id_counter = 0 # keep track of MenuItem ID
    def __init__(self, description, name, price, inStock, calories):
        self.description = description
        self.name = name
        self.price = price
        self.inStock = inStock
        self.calories = calories
        self.menuItemID = "4" + str(MenuItem.id_counter)
        MenuItem.id_counter += 1

    def __str__(self): # display info of each MenuItem object
        stockStatus = "In Stock" if self.inStock else "Out of Stock"  
        return f"Description: {self.description} \nName: {self.name} \nPrice: {self.price} \nStatus: {self.stockStatus} \nCalories: {self.calories} " 

class ItemInOrder: # Quynh 
    id_counter = 0 # ItemInOrder ID
    def __init__(self, menuItemID, customizationToItem):
        ItemInOrder.__init__(self, menuItemID, customizationToItem)
        self.menuItemID = MenuItem.menuItemID # menuItem ID is also an attrbute to link MenuItem and ItemInOrder
        self.ItemInOrderID = "5" + str(ItemInOrder.id_counter)
        ItemInOrder.id_counter += 1
        self.customizationToItem = customizationToItem

    def __str__(self): # display customization info of each ItemInOrder object
        return f"Customization: {self.customizationToItem}"


# System Methods Skeleton

# Customer and Staff objects take in str data types for name, email
# take in int data types for phone number
# Staff objects will also take in str data type for role
# both will return str values echoing the details entered to create object

def createCustomer(name, emailAddress, phoneNumber): # Cj
    x = Customer(name, emailAddress, phoneNumber)
    print("New Customer Created!")
    return print(x)

def createStaff(name, emailAddress, phoneNumber, role): # Cj 
    x = Staff(name, emailAddress, phoneNumber, role)
    print("New Staff Member Created!")
    return print(x)

def createOrder(order_type, customer): #Thuan-Thien
    if order_type == "online":
        return Online_Order(
            customer.get('orderID'),
            customer.get('itemOrderID'),
            customer.get('additional_comments'),
            customer.get('paymentDate'),
            customer.get('totalCost'),
            customer.get('orderStatus'),
            customer.get('customerID')
        )
    elif order_type == "in_person":
        return In_Person_Order(
            customer.get('orderID'),
            customer.get('itemOrderID'),
            customer.get('additional_comments'),
            customer.get('paymentDate'),
            customer.get('totalCost'),
            customer.get('orderStatus'),
            customer.get('staffID')
        )
    else:
        raise ValueError("Invalid order type specified. Use 'online' or 'in_person'.")

def payOrder(customerBankingInfo, Order): #Thuan-Thien
    # Simulating payment process using customer banking info
    if not customerBankingInfo:
        raise ValueError("Invalid banking information provided.")

    # Assuming payment is successful, return receipt
    return f"Receipt: OrderID: {order.orderID}, Total Cost: ${order.totalCost:.2f}"

# will take in an orderID number and a list of active orders (assume list has been created)
# will return the status of the desired order (str)
def checkOrderStatus(activeOrders, targetOrderID): # Cj 
    for order in activeOrders:
        number = getattr(order, "orderID")
        if number == targetOrderID:
            print("The order of the status is: " + order.status)
        else:
            print("The order does not exist. Sorry!")
        
# will take in a staffID (for verification that the user can update status of order)
# orderID, list of StaffIDs, and list of active orders, will change the staus of the 
# order based on Staff input
def updateOrderStatus(staffMembers, activeOrders, staffID, orderID): # Cj
    for order in activeOrders:
        number = getattr(order, "orderID")
        if number == orderID:
            for staff in staffMembers:
                id = getattr(staff, "staffID")
                if id == staffID:
                    newOrderStatus = input("Please enter the new status of the order: ")
                    order.orderStatus = newOrderStatus
                else:
                    print("The staff ID does not exist. Sorry!")
        else:
            print("The order does not exist. Sorry!")
           
# creates a MenuItem object
# inStock is a boolean attribute (there is stock or no stock)
def createMenuItem(): # Quynh
    description = input("Enter the item description: ")
    name = input("Enter the item name: ")
    
    # get price
    while True:
        try:
            price = float(input("Enter the item price: $"))
            break
        except ValueError:
            print("Invalid input. Please enter a number for the price. ")

    # get inStock status
    while True:
        inStock = input("Is the item in stock? (yes/no): ").strip().lower()
        if inStock in ['yes', 'y']:
            inStock = True
            break
        elif inStock in ['no', 'n']:
            inStock = False
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'. ")

    calories = input("Enter the item calories: ")

    # instantiate an object
    x = MenuItem(description, name, price, inStock, calories)
    return x

# this method takes in the MenuItem object that staff wants to change
# assume menu_item = createMenuItem()
# might need if-else to allow staff to choose which attribute to edit?
def updateMenuItem(menu_item): # Quynh
    # get new description
    new_description = input("Enter new description: ")
    if new_description:
        menu_item.description = new_description

    # get new name
    new_name = input("Enter new name: ")
    if new_name:
        menu_item.name = new_name

    # get new price
    while True:
        new_price = float(input("Enter new price: $"))
        if new_price:
            try:
                menu_item.price = new_price
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        else:
            break

    # get new status
    while True:
        new_status = input("Is the item in stock? (yes/no): ").strip().lower()
        if new_status in ['yes', 'y']:
            menu_item.inStock = True
            break
        elif new_status in ['no', 'n']:
            menu_item.inStock = False
            break
        elif new_status == "":
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'. ")

    # get new calories
    new_calories = input("Enter new calories: ")
    if new_calories:
        menu_item.calories = new_calories

    # display updated menu item details
    print(menu_item)
    

# all menu items are categorized by meal type
# each object of Menu will have one mealType value and multiple itemsInMenu values
def createMenu(): # Quynh
    mealType = input("Enter the meal type: ")

    # input items as a comma-separated list
    items_input = input("Enter each menu item separated by commas: ") 
    itemsInMenu = [item.strip() for item in items_input.split(",") if item.strip()]

    # instantiate an object
    x = Menu(mealType, itemsInMenu)
    return x

# this method takes in all objects of Menu and display all of them at once
# assume menuLists = list(Menu objects)
def viewMenu(menuLists): # Quynh

    # if no Menu object has been created
    if not menuLists:
        print("No menu to display.")
        return
    # loop to display all Menu objects
    for menuList in menuLists:
        print(menuList)




# can use area for testing :)
