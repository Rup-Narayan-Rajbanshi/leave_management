# Leave Tracker

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
