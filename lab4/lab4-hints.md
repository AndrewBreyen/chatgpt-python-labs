
2. For file handling and error handling:
User input can be handled in one of two ways depending on your Python version
https://www.w3schools.com/python/python_user_input.asp
Use the `try`-`except` statements to handle errors related to opening files.
https://www.w3schools.com/python/python_try_except.asp
Use the `open()` function to open files.
https://www.w3schools.com/python/python_file_handling.asp
Use the `.read()` method to read the contents of the file.
https://www.w3schools.com/python/python_file_open.asp

3. For using modules:
   - Import the desired module at the beginning of your code with `import` statement.
   - Use dot notation to call methods within the imported module. 

4. For creating classes and inheritance:
   - Use the `class` keyword to define the class.
   - Define the `__init__` method to initialize the attributes of the class.
   - Define any additional methods of the class.
   - Use the `super()` function in the subclass to inherit attributes and methods from the parent class.

5. For interacting with APIs:
   - Use the `requests` module to make API requests.
   - Use `.get()` method to get the API response.
   - Use the `.json()` method to convert the API response into JSON format.

6. For using regular expressions:
   - Import the `re` module at the beginning of the code with `import` statement.
   - Use the `re.match()` function to match the user input to a pattern
   - The pattern `^[a-zA-Z0-9]+$` matches any input that only contains alphanumeric characters.


Note: These hints are not a full solution, but are meant to provide guidance for completing the lab.




Expected Output:
2. Enter file name: test.txt
This is a test file.
It is being used to demonstrate file handling in Python.
The contents of this file will be printed out to the console.

3. Enter a number: 16
The square root of 16 is 4.0

4. The cat goes meow.

5. 
{
  "message": {
    "affenpinscher": [],
    "african": [],
    "airedale": [],
    "akita": [],
    "appenzeller": [],
    "australian": [
      "shepherd"
    ]
……… more things here
  },
  "status": "success"
}
