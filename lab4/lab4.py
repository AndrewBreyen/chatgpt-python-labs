filename = input("Enter a file name: ")
try:
    with open(filename, 'r') as file:
        print(file.read())
except FileNotFoundError:
    print("Error: File not found.")





import math

number = float(input("Enter a number: "))
print("The square root of", number, "is", math.sqrt(number))

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def speak(self):
        print("The", self.species, self.name, "is making a noise.")

class Cat(Animal):
    def speak(self):
        print("The cat", self.name, "says meow.")

class Dog(Animal):
    def speak(self):
        print("The dog", self.name, "says woof.")

cat = Cat("Fluffy", "cat")
dog = Dog("Nemo", "dog")
cat.speak()
dog.speak()




import requests
from pprint import pprint

response = requests.get("https://dog.ceo/api/breeds/list/all")
pprint(response.json())








import re

string = input("Enter a string: ")
if re.match("^[a-zA-Z0-9]+$", string):
    print("Success: The string matches the pattern.")
else:
    print("Error: The string does not match the pattern.")