# BookStoreGUI

This is a simple GUI-based book management system. It allows users to add, edit, and delete books, as well as search for books in the system. There are two accounts availible: user and admin.

When the program is launched, it will display a login screen where users can enter their username and password. The system will then check the entered details and redirect the user to either the user or admin interface.

If the user enters the correct login credentials for the admin account, they will be redirected to the admin interface. Here, they can manage books, orders, and users. When managing books, the admin can add, edit, or delete a book. Similarly, when managing users, the admin can add, edit, or delete a user.

If the user enters the correct login credentials for a non-admin account, they will be redirected to the user interface. Here, they can browse and search for books in the system. They can also view book details and edit their profile.

To add a new book to the system, click the "Add Book" button in the user interface. A new window will open where the user can enter the book details such as book name, author, price, and number of copies. The user can also upload an image of the book cover.

# Library Management System Manual

## Login

To access the program, users will need to log in using their username and password. If they do not have an account, they will need to create one. Admin accounts will need to be created manually by modifying the users.xlsx file in the program’s directory.

## Admin Functions

When logged in as an admin, users will have access to the following functions:


- Manage Books: Allows admins to view, add, update, and delete books from the inventory.

- Manage Users: Allows admins to view, add, update, and delete users from the system.

- Manage Orders: Allows admins to view and delete orders placed by users.

## User Functions

When logged in as a regular user, users will have access to the following functions:

- View Books: Allows users to view the available books in the inventory.

- Place Order: Allows users to place an order for a book. Users will need to provide their name, the book’s ID, and the number of copies they want to order.


* Adding a Book

> To add a new book to the inventory, an admin will need to click on the “Manage Books” button and then click on the “Add Book” button. They will then need to provide the book’s title, author, price, image (in PNG format), and the number of copies available. Once the book has been added, it will be available for users to view and order.

* Updating a Book

> To update a book’s information, an admin will need to click on the “Manage Books” button and then select the book they want to update. They can then update the book’s information and save the changes.

* Deleting a Book

> To delete a book from the inventory, an admin will need to click on the “Manage Books” button and then select the book they want to delete. They can then click on the “Delete” button to remove the book from the inventory.

## Admin Functions

* Adding a User

> To add a new user to the system, an admin will need to click on the “Manage Users” button and then click on the “Add User” button. They will then need to provide the user’s name, password, and whether or not they are an admin. Once the user has been added, they will be able to log in and use the program.

* Updating a User

> To update a user’s information, an admin will need to click on the “Manage Users” button and then select the user they want to update. They can then update the user’s information and save the changes.

* Deleting a User

> To delete a user from the system, an admin will need to click on the “Manage Users” button and then select the user they want to delete. They can then click on the “Delete” button to remove the user from the system.

* Placing an Order

> To place an order, a regular user will need to click on the “View Books” button and select the book they want to order. They can then enter their name and the number of copies they want to order. Once they have confirmed their order, it will be added to the system and the inventory will be updated.

* Viewing Orders

> To view orders, an admin will need to click on the “Manage Orders” button. They will then be able to view a list of all the orders that have been placed, as well
