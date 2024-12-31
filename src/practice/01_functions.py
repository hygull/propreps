# python3 src/practice/functions.py


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    # Assumes that b is always a non zero number
    return a / b


print(
    addition(60, 40) + subtraction(150, 50) + multiplication(50, 2) + division(1500, 15)
)
