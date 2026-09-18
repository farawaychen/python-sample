"""Utility functions for the Python learning project.

This module demonstrates how to create reusable modules.
"""

from __future__ import annotations

import math


def is_prime(n: int) -> bool:
    """Check whether a number is prime."""
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


def fibonacci(n: int) -> list[int]:
    """Return the first n Fibonacci numbers."""
    if n <= 0:
        return []
    if n == 1:
        return [0]
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq


def to_celsius(fahrenheit: float) -> float:
    """Convert temperature from Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


if __name__ == "__main__":
    # Quick self-test
    print("Primes up to 20:", [x for x in range(21) if is_prime(x)])
    print("Fibonacci(10):", fibonacci(10))
    print(f"100°F = {to_celsius(100):.2f}°C")
