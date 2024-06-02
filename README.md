# Leave Tracker
Live Demo :https://rup-leave-tracker.herokuapp.com/

Description
- This app allows employee to request leave and track their leave detail based on the leave approval.
- If leave is approved then calculate remaining leave, Calculates number of leave taken per month.

# Procedure to run locally:
- Create a directory and pull the source code to the directory
- Create and activate a virtual environment
- Point the directory towards path where manage.py file exists
- Install the dependencies using pip install -r requirements.txt
- Run python manage.py migrate
- Run python manage.py createsuper to create superuser
- Run python manage.py load_master_data to load groups into database
- Then request http://127.0.0.1:8000 in browser. On sucessful run Welcome page appears.
- Request http://127.0.0.1:8000/admin/ in the url to login as superuser.
- After sucessful login add Leave such as Sick leave, Casual leave with number of days from the admin panen.
- Then you can create employees, Make sure to add group "employee" to the user added.
- Then an employee can login and request leave, track leaves througn the app.

Note: .env file has to be added in project directory for secret key

Branch leave-production is for deployment in Heroku.





# Backend Internship syllabus

## Internship  overview
	- Python, Django, DRF, Git, Project, Exercise

## Python Installation
   **Windows**
 - [https://www.python.org/downloads/windows/]()
 - [https://www.digitalocean.com/community/tutorials/install-python-windows-10]()

**Linux**
 - [https://www.geeksforgeeks.org/how-to-install-python-on-linux/]()
  
  **Mac**:
        -[https://www.python.org/downloads/macos/]()
        -[https://www.dataquest.io/blog/installing-python-on-mac/]()

## IDE Installation
**Visual Studio**:

 - [https://code.visualstudio.com/download]()

## Python Basic
    - Python introduction
    - Python Virtual Environment
    - Python Interpreter
    - syntax
    - Comments
    - Variables
    - Data Type
    - Numbers
    - Python casting
    - String
    - Boolean
    - Python Operators
    - List
    - Tuples
    - Sets
    - Dictionaries
    - Arrays
    - Python If else
    - While loops
    - For loops
    - Break/Continue statement
    - Python arguments: positional,keyword,arbitrary
    - Iterator
    - Python functions
    - Python Lambda
    - Class/Objects
    - Inheritance
    - Polymorphism
    - Scope
    - Modules
    - Date
    - Math
    - Json
    - Try Except
    - User Input
    - String Formatting.

   **Tutorials**
    [https://www.w3schools.com/python/]()
    [https://www.tutorialspoint.com/python/index.htm]()
    [https://www.geeksforgeeks.org/python-programming-language-tutorial/]()
    [https://docs.python.org/3/tutorial/index.html]()

## Advance Python

## Git 

