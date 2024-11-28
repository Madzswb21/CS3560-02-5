-- DROP DATABASE IF EXISTS cafeRestaurant; -- use this query if you want to delete old database and make new one with changes applied
CREATE DATABASE cafeRestaurant;
-- make sure to uncomment before pushing :)

-- USE cafeRestaurant; -- use this query if you encounter error where db is created with no tables
-- creates a table to hold information on staff members
CREATE TABLE IF NOT EXISTS Staff (
	staffID int PRIMARY KEY AUTO_INCREMENT,
    f_name VARCHAR(45),
    l_name VARCHAR(45),
    emailAddress VARCHAR(45),
    phoneNumber VARCHAR(45),
    staffRole VARCHAR(45)
);
ALTER TABLE Staff AUTO_INCREMENT = 1000; -- sets the auto-generated IDs to start at 1000

-- creates a table to hold information on customers
CREATE TABLE IF NOT EXISTS Customer (
	custID int PRIMARY KEY AUTO_INCREMENT,
    f_name VARCHAR(45),
    l_name VARCHAR(45),
    emailAddress VARCHAR(45),
    phoneNumber VARCHAR(45),
    physAddress VARCHAR(45)
);
ALTER TABLE Customer AUTO_INCREMENT = 2000; -- sets the auto-generated IDs to start at 2000


-- creates a table to hold a list of all orders and their type
-- is used to auto-generate an order ID, then use to create the actual object depending
-- on if it is an online order or in person order
CREATE TABLE IF NOT EXISTS Orders (
	orderID int PRIMARY KEY,
    orderType VARCHAR(45)
);


-- creates a table to hold information on online orders
-- uses customer ID since customers placeonline orders
CREATE TABLE IF NOT EXISTS OnlineOrder (
	onlineID int PRIMARY KEY,
    custID int,
    orderStatus VARCHAR(45),
    paymentDate VARCHAR(45),
    addComments VARCHAR(100),
    totalCost DECIMAL(65, 2),
    pickupTime VARCHAR(45),
    FOREIGN KEY(custID) REFERENCES Customer(custID)
);


-- creates a table to hold information on in-person orders
-- uses staff ID since staff place in-person orders
CREATE TABLE IF NOT EXISTS InPersonOrder (
	inPersonID int PRIMARY KEY,
    staffID int,
    orderStatus VARCHAR(45),
    paymentDate VARCHAR(45),
    addComments VARCHAR(100),
    totalCost DECIMAL(65, 2),
    tableNum int, 
    FOREIGN KEY(staffID) REFERENCES Staff(staffID)
);


-- creates a table to hold information on all menu items
CREATE TABLE IF NOT EXISTS MenuItem (
	menuItemID int PRIMARY KEY AUTO_INCREMENT,
    itemName VARCHAR(45),
    itemDesc VARCHAR(100),
    itemPrice DECIMAL(65, 2),
    isInStock BOOL,
    calories int
);
-- new changes, run this 1st
ALTER TABLE MenuItem CHANGE isInStock stock int; -- change name to stock and use quantity to show whether an item is available or not
ALTER TABLE MenuItem ADD category ENUM ("food", "drink", "other"); -- category column with 3 choices

-- creates a table that holds items in a specifc order
-- takes in a menu item ID and an existing order ID to create a compound key
-- is the "association class" between an order and the menu items placed into an order
CREATE TABLE IF NOT EXISTS ItemsInOrder (
	menuItemID int,
    orderID int,
    quantity int,
    FOREIGN KEY(menuItemID) REFERENCES MenuItem(menuItemID),
    FOREIGN KEY(orderID) REFERENCES Orders(orderID),
    PRIMARY KEY(menuItemID, orderID)
); 

-- dummy variables for testing purposes; for "customer," "staff" and "menu item"
-- make sure to comment out after running once if needed, don't want duplicates
-- staff members
INSERT INTO Staff (f_name, l_name, emailAddress, phoneNumber, staffRole) VALUES 
	("Jane", "Doe", "janedoe@email.com", "123-456-7890", "Server");
INSERT INTO Staff (f_name, l_name, emailAddress, phoneNumber, staffRole) VALUES 
	("John", "Doe", "johndoe@email.com", "111-222-3434", "Cashier");

-- customers
INSERT INTO Customer(f_name, l_name, emailAddress, phoneNumber, physAddress) VALUES
	("Caoilainn", "Johnsson", "cj@email.com", "222-222-2222", "222 Some St.");
INSERT INTO Customer(f_name, l_name, emailAddress, phoneNumber, physAddress) VALUES 
	("Joe", "Mama", "jm@email.com", "555-555-5555", "555 Some St.");

-- menu items
INSERT INTO MenuItem (itemName, itemDesc, itemPrice, isInStock, calories) VALUES 
	("Turkey BLT", "Turkey sandwich on sourdough with bacon, lettuce and tomato with garlic aoili", 12.99, True, 447);
INSERT INTO MenuItem (itemName, itemDesc, itemPrice, isInStock, calories) VALUES 
	("Egg Salad Sandwich", "Egg salad on rye bread", 11.99, True, 350);
INSERT INTO MenuItem (itemName, itemDesc, itemPrice, isInStock, calories) VALUES 
	("Caeser Salad", "Romaine lettuce with house-made Caeser dressing, topped with grilled chicken", 14.00, True, 550);
INSERT INTO MenuItem (itemName, itemDesc, itemPrice, isInStock, calories) VALUES 
	("French Onion Soup", "House-made french onion soup, served in a bread bowl", 14.50, True, 600);
INSERT INTO MenuItem (itemName, itemDesc, itemPrice, isInStock, calories) VALUES 
	("Chicken Noodle Soup", "House-made chicken noodle soup with carrots and celery", 13.50, True, 500);

INSERT INTO MenuItem (itemName, itemDesc, itemPrice, isInStock, calories) VALUES 
	("Vanilla Latte", "Vanilla latte with fresh ground espresso", 5.50, True, 250);
INSERT INTO MenuItem (itemName, itemDesc, itemPrice, isInStock, calories) VALUES 
	("Matcha Latte", "Ceremonial-grade matcha with milk", 6.50, True, 225);
INSERT INTO MenuItem (itemName, itemDesc, itemPrice, isInStock, calories) VALUES 
	("Coffee", "Freshly brewed coffee with 100% Arabica beans", 2.00, True, 10);
INSERT INTO MenuItem (itemName, itemDesc, itemPrice, isInStock, calories) VALUES 
	("Green tea", "Steeped green tea leaves", 2.00, True, 10);
INSERT INTO MenuItem (itemName, itemDesc, itemPrice, isInStock, calories) VALUES 
	("Mocha Latte", "Chcolate and espresso combined with milk", 5.50, True, 280);

INSERT INTO MenuItem (itemName, itemDesc, itemPrice, isInStock, calories) VALUES 
	("Croissant", "Flaky, buttery pastery", 2.00, True, 150);
INSERT INTO MenuItem (itemName, itemDesc, itemPrice, isInStock, calories) VALUES 
	("Side of Fries", "Crinkle-cut fries made fresh-to-order", 3.50, True, 250);
INSERT INTO MenuItem (itemName, itemDesc, itemPrice, isInStock, calories) VALUES 
	("Side Salad", "House Salad with balsamic dressing", 4.00, True, 150);
INSERT INTO MenuItem (itemName, itemDesc, itemPrice, isInStock, calories) VALUES 
	("Bleuberry Muffin", "Freshly baked blueberry muffin", 2.50, True, 300);
INSERT INTO MenuItem (itemName, itemDesc, itemPrice, isInStock, calories) VALUES 
	("Brownie", "Freshly baked fudge brownie dusted with powdered sugar", 2.99, True, 300);

-- populate stock and category column, run this 2nd
UPDATE MenuItem SET stock = 5 WHERE menuItemID > 0;
UPDATE MenuItem SET category = "food" WHERE menuItemID < 6;
UPDATE MenuItem SET category = "drink" WHERE menuItemID BETWEEN 6 AND 10;
UPDATE MenuItem SET category = "other" WHERE menuItemID BETWEEN 11 AND 15;


