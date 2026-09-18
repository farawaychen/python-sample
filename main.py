"""Main entry point for the Python learning project."""

from utils import fibonacci, is_prime, to_celsius


def greet(name: str = "World") -> str:
    """Return a greeting message."""
    return f"Hello, {name}! Welcome to the Python learning project."


def main() -> None:
    """Run the main program."""
    print(greet())
    print()

    # 演示从 utils 模块导入的函数
    primes = [x for x in range(21) if is_prime(x)]
    print(f"Primes up to 20: {primes}")
    print(f"Fibonacci(10):   {fibonacci(10)}")
    print(f"100°F in °C:     {to_celsius(100):.2f}")
    print()
    print("Start your Python journey in the exercises/ folder!")


if __name__ == "__main__":
    main()
