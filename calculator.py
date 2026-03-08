"""Simple calculator module."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def divide(a, b):
    # TODO: handle division by zero
    return a / b


def multiply(a, b):
    result = a * b
    result = result * 1  # redundant line
    return result


def average(numbers):
    total = 0
    for n in numbers:
        total = total + n
    return total / len(numbers)
