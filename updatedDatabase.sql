DROP DATABASE IF EXISTS cafeRestaurant; -- use this query if you want to delete old database 
										   -- and make new one with changes applied
CREATE DATABASE cafeRestaurant;
-- make sure to uncomment before pushing :)

USE cafeRestaurant; -- use this query if you encounter error where db is created with no tables
-- creates a table to hold information on staff members
CREATE TABLE IF NOT EXISTS Staff (
	staffID int PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(20),
    pass VARCHAR(255),   -- space to hash the password
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
    username VARCHAR(20),
    pass VARCHAR(255),   -- space to hash the password
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
ALTER TABLE MenuItem ADD image VARCHAR(45);

-- creates a table that holds items in a specifc order
-- takes in a menu item ID and an existing order ID to create a compound key
-- is the "association class" between an order and the menu items placed into an order
CREATE TABLE IF NOT EXISTS ItemsInOrder (
	menuItemID int,
    orderID int,
    quantity int,
    customization VARCHAR(45), 
    FOREIGN KEY(menuItemID) REFERENCES MenuItem(menuItemID),
    FOREIGN KEY(orderID) REFERENCES Orders(orderID),
    PRIMARY KEY(menuItemID, orderID)
); 

-- dummy variables for testing purposes; for "customer," "staff" and "menu item"
-- make sure to comment out after running once if needed, don't want duplicates
-- staff members
INSERT INTO Staff (username, pass, f_name, l_name, emailAddress, phoneNumber, staffRole) VALUES 
	("staff", "1234", "Jane", "Doe", "janedoe@email.com", "123-456-7890", "Server");
INSERT INTO Staff (username, pass, f_name, l_name, emailAddress, phoneNumber, staffRole) VALUES 
	("employee", "0000", "John", "Doe", "johndoe@email.com", "111-222-3434", "Cashier");

-- customers
INSERT INTO Customer(username, pass, f_name, l_name, emailAddress, phoneNumber, physAddress) VALUES
	("cjohnsson", "55555", "Caoilainn", "Johnsson", "cj@email.com", "222-222-2222", "222 Some St.");
INSERT INTO Customer(username, pass, f_name, l_name, emailAddress, phoneNumber, physAddress) VALUES 
	("jmama", "22222", "Joe", "Mama", "jm@email.com", "555-555-5555", "555 Some St.");

-- menu items
INSERT INTO MenuItem (itemName, itemDesc, itemPrice, stock, calories, category) VALUES 
	("Turkey BLT", "Turkey sandwich on sourdough with bacon, lettuce and tomato with garlic aoili", 12.99, 10, 447, "food");
INSERT INTO MenuItem (itemName, itemDesc, itemPrice, stock, calories, category) VALUES 
	("Egg Salad Sandwich", "Egg salad on rye bread", 11.99, 10, 350, "food");
INSERT INTO MenuItem (itemName, itemDesc, itemPrice, stock, calories, category) VALUES 
	("Caeser Salad", "Romaine lettuce with house-made Caeser dressing, topped with grilled chicken", 14.00, 10, 550, "food");
INSERT INTO MenuItem (itemName, itemDesc, itemPrice, stock, calories, category) VALUES 
	("French Onion Soup", "House-made french onion soup, served in a bread bowl", 14.50, 10, 600, "food");
INSERT INTO MenuItem (itemName, itemDesc, itemPrice, stock, calories, category) VALUES 
	("Chicken Noodle Soup", "House-made chicken noodle soup with carrots and celery", 13.50, 10, 500, "food");

INSERT INTO MenuItem (itemName, itemDesc, itemPrice, stock, calories, category) VALUES 
	("Vanilla Latte", "Vanilla latte with fresh ground espresso", 5.50, 10, 250, "drink");
INSERT INTO MenuItem (itemName, itemDesc, itemPrice, stock, calories, category) VALUES 
	("Matcha Latte", "Ceremonial-grade matcha with milk", 6.50, 10, 225, "drink");
INSERT INTO MenuItem (itemName, itemDesc, itemPrice, stock, calories, category) VALUES 
	("Coffee", "Freshly brewed coffee with 100% Arabica beans", 2.00, 10, 10, "drink");
INSERT INTO MenuItem (itemName, itemDesc, itemPrice, stock, calories, category) VALUES 
	("Green tea", "Steeped green tea leaves", 2.00, 10, 10, "drink");
INSERT INTO MenuItem (itemName, itemDesc, itemPrice, stock, calories, category) VALUES 
	("Mocha Latte", "Chcolate and espresso combined with milk", 5.50, 10, 280, "drink");

INSERT INTO MenuItem (itemName, itemDesc, itemPrice, stock, calories, category) VALUES 
	("Croissant", "Flaky, buttery pastery", 2.00, 10, 150, "other");
INSERT INTO MenuItem (itemName, itemDesc, itemPrice, stock, calories, category) VALUES 
	("Side of Fries", "Crinkle-cut fries made fresh-to-order", 3.50, 10, 250, "other");
INSERT INTO MenuItem (itemName, itemDesc, itemPrice, stock, calories, category) VALUES 
	("Side Salad", "House Salad with balsamic dressing", 4.00, 10, 150, "other");
INSERT INTO MenuItem (itemName, itemDesc, itemPrice, stock, calories, category) VALUES 
	("Bleuberry Muffin", "Freshly baked blueberry muffin", 2.50, 10, 300, "other");
INSERT INTO MenuItem (itemName, itemDesc, itemPrice, stock, calories, category) VALUES 
	("Brownie", "Freshly baked fudge brownie dusted with powdered sugar", 2.99, 10, 300, "other");


-- test img 
UPDATE MenuItem SET image = "img/turkey.png" WHERE menuItemID = 1;
UPDATE MenuItem SET image = "img/eggsandwich.png" WHERE menuItemID = 2;
UPDATE MenuItem SET image = "img/vanillalatte.png" WHERE menuItemID = 6;
UPDATE MenuItem SET image = "img/matchalatte.png" WHERE menuItemID = 7;
UPDATE MenuItem SET image = "img/croissant.png" WHERE menuItemID = 11;
UPDATE MenuItem SET image = "img/fries.png" WHERE menuItemID = 12;







