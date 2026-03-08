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


def median(numbers):
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    return sorted_nums[mid]


def variance(numbers):
    avg = average(numbers)
    return sum((x - avg) ** 2 for x in numbers) / len(numbers)


def std_dev(numbers):
    return variance(numbers) ** 0.5
