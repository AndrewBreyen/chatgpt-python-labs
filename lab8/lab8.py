# Part 1: String Manipulation
sentence = "The quick brown fox jumps over the lazy dog."

# Convert all characters in sentence to uppercase
print(sentence.upper())

# Replace "fox" with "cat" in sentence
print(sentence.replace("fox", "cat"))

# Count the number of occurrences of the letter "o" in sentence
print(sentence.count("o"))

# Use string concatenation to print a sentence with word "Python"
word = "Python"
print("I am learning " + word + " programming.")

# Part 2: List Comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create list of squares of numbers using list comprehension
squares = [n**2 for n in numbers]
print(squares)

# Create list of even numbers from numbers using list comprehension
evens = [n for n in numbers if n % 2 == 0]
print(evens)

# Create list of odd numbers from numbers using list comprehension
odds = [n for n in numbers if n % 2 == 1]
print(odds)

# Create list of lengths of words using list comprehension
words = ["apple", "banana", "cherry", "date", "elderberry", "fig"]
lengths = [len(word) for word in words]
print(lengths)

# Bonus Challenge: Reverse words function
def reverse_words(sentence):
    words = sentence.split()
    words.reverse()
    return " ".join(words)

# Test reverse_words function
print(reverse_words("hello world"))
print(reverse_words("the quick brown fox"))

