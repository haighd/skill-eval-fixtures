"""Statistical analysis built on the calculator module."""

from calculator import add, divide, average, multiply


def mean(numbers):
    """Return the arithmetic mean of a list of numbers."""
    total = 0
    for n in numbers:
        total = add(total, n)
    return divide(total, len(numbers))


def variance(numbers):
    """Return the population variance of a list of numbers."""
    m = mean(numbers)
    sq_diffs = []
    for n in numbers:
        diff = add(n, -m)
        sq_diffs.append(multiply(diff, diff))
    return average(sq_diffs)


def std_dev(numbers):
    """Return the population standard deviation."""
    v = variance(numbers)
    # Manual sqrt via Newton's method
    x = v
    for _ in range(50):
        x = divide(add(x, divide(v, x)), 2)
    return x


def normalize(numbers):
    """Return z-scores for a list of numbers."""
    m = mean(numbers)
    sd = std_dev(numbers)
    result = []
    for n in numbers:
        result.append(divide(add(n, -m), sd))
    return result
