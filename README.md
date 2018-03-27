# Item Catalog Project
## Udacity Full-Stack Web Developer Nanodegree
Version 1.0

Abdi Ibrahim
March 27, 2017

Purpose
-----------------------------------------
To develop an application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.

To learn how to develop a RESTful web application using the Python framework Flask along with implementing third-party OAuth authentication. To learn when to properly use the various HTTP methods available and how these methods relate to CRUD (create, read, update and delete) operations.

Contents
-----------------------------------------
- static
    - blank_user.jpg
    - styles.css
    - top-banner.jpg
- templates
    - categories.html
    - deleteCategory.html
    - deletelistitem.html
    - editCategory.html
    - editListItem.html
    - header.html
    - list.html
    - login.html
    - main.html
    - newCategory.html
    - newlistitem.html
    - publiccategories.html
    - publiclist.html
- client_secrets.json
- database_setup.py
- populate.py
- project.py
- README.md

Built With
-----------------------------------------
- Python 3
- Vagrant VM

Getting Started
-----------------------------------------
Pre-requisites:
- Python 3
- Git Bash
- Vagrant (Linux-based Virtual Machine)
- Text Editor (Atom, Sublime, etc.)
- SQLAlchemy
- Google Account
- Web browser (Chrome, Firefox, etc.)

How to Run
-----------------------------------------
- Install Vagrant VM by following the instructions on the Udacity Project Page.
- In the Git Bash shell, change directories to that you are in the file
  containing the Vagrant VM.
- Load Vagrant VM using 'vagrant up' and 'vagrant shh' commands.
- Run the following commands to load the database and populate it.
    - `python database_setup.py`
    - `python populate.py`
- Run the Python program using the command
    - `python project.py`
- Open web browser and go to http://localhost:5000/

Authors
-----------------------------------------
Abdi Ibrahim

Acknowledgements
-----------------------------------------
- Udacity
- Udacity Style Guide
- PEP8 Style Guide
- SQLAlchemy
- Python Standard Library
