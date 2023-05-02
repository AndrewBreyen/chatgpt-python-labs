# 1. Create a new Python file and save it as "lab5.py".

# 2. Install the "sqlite3" module using pip. Then, create a new SQLite database called "my_db" 
#    and a table called "users" with columns for "id", "name", and "email". Insert at least 
#    three rows of data into the table.

import sqlite3

conn = sqlite3.connect('my_db.db')
c = conn.cursor()

c.execute('''CREATE TABLE users
             (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')

users_data = [(1, 'Alice', 'alice@example.com'),
              (2, 'Bob', 'bob@example.com'),
              (3, 'Charlie', 'charlie@example.com')]

c.executemany('INSERT INTO users VALUES (?, ?, ?)', users_data)

conn.commit()
conn.close()

# 3. Write a program that selects all rows from the "users" table and prints out the results.

conn = sqlite3.connect('my_db.db')
c = conn.cursor()

c.execute('SELECT * FROM users')

for row in c.fetchall():
    print(row)

conn.close()

# 4. Use the "requests" module to make a GET request to the following API: "https://api.coinmarketcap.com/v1/ticker/?limit=10". 
#    Print out the name and price of each cryptocurrency returned by the API.

import requests

response = requests.get('https://api.coinlore.net/api/tickers/?limit=10')

for currency in response.json()['data']:
    name = currency['name']
    price = currency['price_usd']
    print(name + ': ' + price)


# 5. Create a class called "Rectangle" with attributes "length" and "width". Add methods to the class for 
#    calculating the area and perimeter of the rectangle. Then, create an instance of the class with some 
#    sample values and call the area and perimeter methods.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

rectangle = Rectangle(5, 10)
print(rectangle.area())
print(rectangle.perimeter())
