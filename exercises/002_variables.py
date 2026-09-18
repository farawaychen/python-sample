"""Exercise 002: Variables, types, and functions.

Learn about:
- Variable assignment
- Basic types (int, float, str, bool, list, dict)
- Defining and calling functions
- Type hints
"""


def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


def describe() -> None:
    """Demonstrate basic types."""
    # 基本类型
    count: int = 42
    price: float = 9.99
    title: str = "Python"
    is_valid: bool = True

    print(f"int: {count} -> {type(count).__name__}")
    print(f"float: {price} -> {type(price).__name__}")
    print(f"str: {title} -> {type(title).__name__}")
    print(f"bool: {is_valid} -> {type(is_valid).__name__}")

    # 列表
    fruits: list[str] = ["apple", "banana", "cherry"]
    print(f"list: {fruits}")
    fruits.append("date")
    print(f"after append: {fruits}")

    # 字典
    person: dict[str, object] = {"name": "Alice", "age": 30}
    print(f"dict: {person}")
    print(f"name: {person['name']}")

    # 函数调用
    print(f"add(3, 5) = {add(3, 5)}")


if __name__ == "__main__":
    describe()
