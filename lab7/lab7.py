def is_palindrome(s):
    return s == s[::-1]

def count_substring(s, substring):
    count = 0
    index = 0
    while index < len(s):
        index = s.find(substring, index)
        if index == -1:
            break
        count += 1
        index += 1
    return count

def contains_special_characters(s):
    for c in "$%#@!":
        if c in s:
            return True
    return False

def odd_or_even(n):
    if n < 1 or n > 100:
        print("Number must be between 1 and 100!")
    elif n % 2 == 0:
        print("Even")
    else:
        print("Odd")








s = input("Enter a string: ")
if is_palindrome(s):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

s = input("Enter a string: ")
substring = input("Enter a substring: ")
count = count_substring(s, substring)
print(f"The substring appears {count} times in the string.")

s = input("Enter a string: ")
if contains_special_characters(s):
    print("Your string contains special characters!")

n = input("Enter a number between 1 and 100: ")
try:
    n = int(n)
    odd_or_even(n)
except ValueError:
    print("Invalid input. Please enter an integer.")
