# data_rep
Repository containing project for Data Representation module

MYSQL
Hostname: localhost
Port: 3306
Username: root
password: root

Create Table 1
create table shopstock (code INT PRIMARY KEY, Product VARCHAR(20), amount INT, price INT);

Create Table 2
create table timetable (Employee VARCHAR(50), Monday VARCHAR(15), Tuesday VARCHAR(15), Wednesday VARCHAR(15), Thursday VARCHAR(15), Friday VARCHAR(15), Saturday VARCHAR(15), Sunday VARCHAR(15), PRIMARY KEY(Employee));

This project is a web application project. It is based on a database for a clothes shop, The Wardrobe, which contains 2 tables. The database is called shopstock. One table contains information relating to the shops stock, called shopstock and the other contains staff hours, called timetable.

The welcome page opens first and links to a login page; the login information is:
Username: admin
Password: password

This takes you to the stock page which shows the shopstock table and from here you can perform CRUD operations on the table. There is also a button to take you to the timetable page which shows the table called timetable. 