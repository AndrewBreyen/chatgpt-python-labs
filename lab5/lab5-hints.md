Lab 5- Hints


#2/#3: For working with databases in Python:
https://www.geeksforgeeks.org/sql-create-table/

Use the sqlite3 module to connect to SQLite databases.
connection = sqlite3.connect(‘my_db.db’)
Create a cursor variable called ‘c’, and assign it to a new cursor
c = connection.cursor()
Use the cursor() method to create a cursor object for executing SQL commands.
c.execute(your_SQL_statement_here)
Use SQL statements to create tables: https://www.geeksforgeeks.org/sql-create-table/
Use SQL statements to insert data into the newly created table.


Use the cursor object's execute() method to execute a SQL query.
Use the cursor object’s fetchall() method to retrieve all rows in a result set.
Use a for loop to iterate over the rows in the result set and print out each row.


#4: For interacting with APIs and data manipulation:

Use the requests module to make HTTP requests to APIs.
Use the .get() method to make a GET request to the API.
Use the .json() method to convert the API response into a JSON object.
Use a for loop to iterate over the JSON object within the ‘data’ key and extract the desired data.
Example:
for item in response.json()['data']:
	do_things_with_item



#5: For creating classes: 


Use the class keyword to define a class.
Use the __init__() method to initialize the attributes of the class.
Define methods and functions within the class definition.
Note: These hints are not a full solution, but are meant to provide guidance for completing the lab.
