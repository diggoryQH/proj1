use book_store;
CREATE TABLE customer (
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100),
email VARCHAR(100),
password VARCHAR(255)
);


CREATE TABLE book (
id INT AUTO_INCREMENT PRIMARY KEY,
title VARCHAR(255),
author VARCHAR(255),
price FLOAT,
stock INT
);


CREATE TABLE cart (
id INT AUTO_INCREMENT PRIMARY KEY,
customer_id INT,
created_at DATETIME,
FOREIGN KEY (customer_id) REFERENCES customer(id)
);


CREATE TABLE cart_item (
id INT AUTO_INCREMENT PRIMARY KEY,
cart_id INT,
book_id INT,
quantity INT,
FOREIGN KEY (cart_id) REFERENCES cart(id),
FOREIGN KEY (book_id) REFERENCES book(id)
);