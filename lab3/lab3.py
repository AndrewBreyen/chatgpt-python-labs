# Lab 3 Solution

# 2. Conditional Statements and Loops
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# 3. Working with Dictionaries
my_dict = {"apple": 1, "banana": 2, "cherry": 3, "date": 4, "elderberry": 5}
print(len(my_dict))
for key, value in my_dict.items():
    print(key, value)

# 4. File Handling
with open("my_file.txt", "w") as file:
    file.write("Hello, world!")
    
with open("my_file.txt", "r") as file:
    contents = file.read()
    print(contents)

# 5. Working with Modules
import random
random_number = random.randint(1, 10)
print(random_number)

# 6. Working with Classes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
        
# create an instance of the Person class
person1 = Person("Alice", 25)

# call the greet method
person1.greet()
