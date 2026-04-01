"""Statistical analysis built on the calculator module."""

from collections.abc import Sequence

from calculator import add, divide, average, multiply


def mean(numbers: Sequence[float]) -> float:
    """Return the arithmetic mean of a list of numbers.

    Raises ZeroDivisionError if sequence is empty.
    """
    total: float = 0
    for n in numbers:
        total = add(total, n)
    return divide(total, len(numbers))


def variance(numbers: Sequence[float]) -> float:
    """Return the population variance of a list of numbers.

    Raises ZeroDivisionError if sequence is empty.
    """
    m = mean(numbers)
    sq_diffs = []
    for n in numbers:
        diff = add(n, -m)
        sq_diffs.append(multiply(diff, diff))
    return average(sq_diffs)


def std_dev(numbers: Sequence[float]) -> float:
    """Return the population standard deviation.

    Returns 0.0 for zero-variance input. Raises ZeroDivisionError if sequence is empty.
    """
    v = variance(numbers)
    if v == 0:
        return 0.0
    # Manual sqrt via Newton's method
    x = v
    for _ in range(50):
        x = divide(add(x, divide(v, x)), 2)
    return x


def normalize(numbers: Sequence[float]) -> list[float]:
    """Return z-scores for a list of numbers.

    Returns input unchanged for zero-variance input. Raises ZeroDivisionError if sequence is empty.
    """
    m = mean(numbers)
    sd = std_dev(numbers)
    if sd == 0.0:
        return list(numbers)
    result = []
    for n in numbers:
        result.append(divide(add(n, -m), sd))
    return result
