"""Exercise 001: Hello World and basic print statements.

Learn about:
- print() function
- String formatting (f-strings)
- Comments
"""


def main() -> None:
    # 基础打印
    print("Hello, World!")

    # f-string 格式化
    name = "Python"
    version = "3.12"
    print(f"Learning {name} {version}")

    # 表达式
    x, y = 10, 3
    print(f"{x} + {y} = {x + y}")
    print(f"{x} * {y} = {x * y}")

    # 多行字符串
    print(
        """
        This is a
        multi-line string.
        """
    )


if __name__ == "__main__":
    main()
