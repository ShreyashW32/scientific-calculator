

import math

# Basic arithmetic operations


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

# Trigonometric functions


def sin(x):
    return math.sin(x)


def cos(x):
    return math.cos(x)


def tan(x):
    return math.tan(x)


def arcsin(x):
    return math.asin(x)


def arccos(x):
    return math.acos(x)


def arctan(x):
    return math.atan(x)

# Exponential and logarithmic functions


def exp(x):
    return math.exp(x)


def logarithm(x, base):
    return math.log(x, base)


def natural_logarithm(x):
    return math.log(x)


# Example usage:
print("Advanced Scientific Calculator")
print("--------------------------------")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Sine")
print("6. Cosine")
print("7. Tangent")
print("8. Arcsine")
print("9. Arccosine")
print("10. Arctangent")
print("11. Exponential")
print("12. Logarithm")
print("13. Natural Logarithm")
print("--------------------------------")

choice = input("Enter your choice (1-13): ")

if choice in ['1', '2', '3', '4']:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

if choice == '1':
    print("Result:", add(num1, num2))
elif choice == '2':
    print("Result:", subtract(num1, num2))
elif choice == '3':
    print("Result:", multiply(num1, num2))
elif choice == '4':
    print("Result:", divide(num1, num2))
elif choice == '5':
    num = float(input("Enter a number: "))
    print("Result:", sin(num))
elif choice == '6':
    num = float(input("Enter a number: "))
    print("Result:", cos(num))
elif choice == '7':
    num = float(input("Enter a number: "))
    print("Result:", tan(num))
elif choice == '8':
    num = float(input("Enter a number: "))
    print("Result:", arcsin(num))
elif choice == '9':
    num = float(input("Enter a number: "))
    print("Result:", arccos(num))
elif choice == '10':
    num = float(input("Enter a number: "))
    print("Result:", arctan(num))
elif choice == '11':
    num = float(input("Enter a number: "))
    print("Result:", exp(num))
elif choice == '12':
    num = float(input("Enter a number: "))
    base = float(input("Enter the base: "))
    print("Result:", logarithm(num, base))
elif choice == '13':
    num = float(input("Enter a number: "))
    print("Result:", natural_logarithm(num))
else:
    print("Invalid choice")
