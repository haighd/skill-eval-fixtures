"""Simple calculator module."""

from collections.abc import Sequence


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def divide(a: float, b: float) -> float:
    """Raises ZeroDivisionError if b is 0."""
    return a / b


def multiply(a: float, b: float) -> float:
    return a * b


def average(numbers: Sequence[float]) -> float:
    """Raises ZeroDivisionError if sequence is empty."""
    total: float = 0
    for n in numbers:
        total = total + n
    return total / len(numbers)
