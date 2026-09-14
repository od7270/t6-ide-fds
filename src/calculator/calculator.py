def add(a, b):
    return a + b


def subtract(a, b):
    if a >= b:
        return a - b
    else:
        return b - a


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")

    return a / b