-- CREATE DATABASE cafeRestaurant;

-- "Menu" can have one or many "MenuItems"
CREATE TABLE MenuItem (
	menuItemID int,
    item_name VARCHAR(45),
    item_desc VARCHAR(100),
    item_price VARCHAR(45),
    isInStock BOOL,
    calories int,
    PRIMARY KEY(menuItemID)
);

-- each ItemInOrder is asscoiated with one MenuItem and one FoodOrder (association class)
CREATE TABLE ItemInOrder (
	menuItemID int,
    orderID int,
    customization VARCHAR(100),
    FOREIGN KEY(menuItemID) REFERENCES MenuItem(menuItemID),
    FOREIGN KEY(orderID) REFERENCES FoodOrder(orderID),
    PRIMARY KEY(menuItemID, orderID)
); 


-- Inheritance: "UserPerson" can be either a "Customer" or "Staff," no instance of "UserPerson" can be made
CREATE TABLE UserPerson (
	userID int,
    f_name VARCHAR(45),
    l_name VARCHAR(45),
    emailAddress VARCHAR(45),
    phoneNumber int,
    PRIMARY KEY(userID)
);

CREATE TABLE Customer (
	userID int,
    paymentInfo VARCHAR(45),
    FOREIGN KEY(userID) REFERENCES UserPerson(userID),
    PRIMARY KEY(userID)
);

CREATE TABLE Staff (
	userID int,
    staff_role VARCHAR(45),
    FOREIGN KEY(userID) REFERENCES UserPerson(userID),
    PRIMARY KEY(userID)
);


-- Inheritance: "FoodOrder" can be either a "OnlineOrder" or "InPersonOrder," no instance of "FoodOrder can be made
CREATE TABLE FoodOrder (
	orderID int,
    userID int,
    orderStatus VARCHAR(45),
    paymentDate VARCHAR(45),
    add_Comments VARCHAR(100),
    totalCost int,
    FOREIGN KEY(userID) REFERENCES UserPerson(userID),
    PRIMARY KEY(orderID)
);

CREATE TABLE OnlineOrder (
	orderID int,
    pickupTime VARCHAR(45),
    FOREIGN KEY(orderID) REFERENCES FoodOrder(orderID),
    PRIMARY KEY(orderID)
);

CREATE TABLE InPersonOrder (
	orderID int,
    customerPhone int, 
    FOREIGN KEY(orderID) REFERENCES FoodOrder(orderID),
    PRIMARY KEY(orderID)
);