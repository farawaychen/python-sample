"""Tests for the utils module."""

from utils import fibonacci, is_prime, to_celsius


class TestIsPrime:
    """Tests for is_prime function."""

    def test_small_primes(self) -> None:
        assert is_prime(2) is True
        assert is_prime(3) is True
        assert is_prime(5) is True
        assert is_prime(7) is True

    def test_non_primes(self) -> None:
        assert is_prime(0) is False
        assert is_prime(1) is False
        assert is_prime(4) is False
        assert is_prime(9) is False
        assert is_prime(-5) is False

    def test_large_prime(self) -> None:
        assert is_prime(97) is True


class TestFibonacci:
    """Tests for fibonacci function."""

    def test_empty(self) -> None:
        assert fibonacci(0) == []

    def test_one(self) -> None:
        assert fibonacci(1) == [0]

    def test_first_ten(self) -> None:
        assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


class TestToCelsius:
    """Tests for to_celsius function."""

    def test_known_values(self) -> None:
        assert to_celsius(32) == 0
        assert to_celsius(212) == 100
        assert abs(to_celsius(98.6) - 37.0) < 0.1
