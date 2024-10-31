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
        return f"Name: {self.name} \nID Number: {self.staffID} \nRole: {self.role}"

# subclass to create a Customer user, inherits from User superclass
class Customer(User):
    id_counter = 0 # keeping track of Customer IDs
    def __init__(self, name, emailAddress, phoneNumber):
        User.__init__(self, name, emailAddress, phoneNumber)
        self.customerID = "1" + str(Staff.id_counter) # concatenates a 1 on a customer ID number to designate it as a customer
        Staff.id_counter += 1

    def __str__(self): # displays vital information pertaining to Customer object
        return f"Name: {self.name} \nID Number: {self.customerID} "


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

def createCustomer(): # Cj
    x=0

def createStaff(): # Cj 
    x=0

def createOrder(): # Thuan-Thien
    x=0

def payOrder(): # Thuan-Thien
    x=0

def checkOrderStatus(): # Cj 
    x=0

def updateOrderStatus(): # Cj
    x=0

def createMenuItem(): # Quynh
    x=0

def updateMenuItem(): # Quynh
    x=0

def createMenu(): # Quynh
    x=0

def viewMenu(): # Quynh
    x=0