# function_definitions.py

import math


def square(x):
    return x ** 2


def is_even(x):
    return x % 2 == 0


def print_hello():
    print("Hello, world!")


def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


def greet(name="stranger"):
    print(f"Hello, {name}!")


def calculate_area(radius):
    return math.pi * radius ** 2


def calculate_hypotenuse(a, b):
    return math.sqrt(a ** 2 + b ** 2)


def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n-1)


def calculate_mean(numbers):
    return sum(numbers) / len(numbers)


# main.py
def main():
    print(square(3))
    print(is_even(3))
    print(print_hello())
    print(add(3, 4))
    print(multiply(3, 4))
    greet()
    greet("Andrew")
    print(calculate_area(5))
    print(calculate_hypotenuse(3, 4))
    print(calculate_factorial(5))
    print(calculate_mean([1, 2, 3, 4, 5]))


if __name__ == "__main__":
    main()
