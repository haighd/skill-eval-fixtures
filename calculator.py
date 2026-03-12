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
    if not numbers:
        raise ValueError("numbers must not be empty")
    total = 0
    for n in numbers:
        total = total + n
    return total / len(numbers)


def median(numbers: list[float]) -> float:
    if not numbers:
        raise ValueError("numbers must not be empty")
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    # simplified even/odd branching per review suggestion
    return (
        sorted_nums[mid]
        if n % 2 != 0
        else (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    )


def variance(numbers: list[float]) -> float:
    if not numbers:
        raise ValueError("numbers must not be empty")
    avg = average(numbers)
    return sum((x - avg) ** 2 for x in numbers) / (len(numbers) - 1)


def std_dev(numbers: list[float]) -> float:
    return variance(numbers) ** 0.5
