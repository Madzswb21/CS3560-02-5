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
    x=0

class Online_Order(Order): # Thuan-Thien
    x=0

class In_Person_Order(Order): # Thuan-Thien
    x=0

class Menu: # Quynh
    x=0

class MenuItem: # Quynh
    x=0

class ItemInOrder: # Quynh 
    x=0


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

def createOrder(): # Thuan-Thien
    x=0

def payOrder(): # Thuan-Thien
    x=0

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
           

def createMenuItem(): # Quynh
    x=0

def updateMenuItem(): # Quynh
    x=0

def createMenu(): # Quynh
    x=0

def viewMenu(): # Quynh
    x=0




# can use area for testing :)