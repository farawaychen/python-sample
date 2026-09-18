# Python 基础学习笔记

## 变量与类型

Python 是动态类型语言，变量无需声明类型，但推荐使用类型提示：

```python
x: int = 10          # 类型提示（可选，不影响运行时）
name: str = "Alice"
height: float = 1.75
is_admin: bool = True
```

## f-string 格式化

```python
name, age = "Alice", 30
print(f"{name} is {age} years old")      # Alice is 30 years old
print(f"{age + 1}")                       # 31
print(f"{'center':^20}")                  # 居中
print(f"{3.14159:.2f}")                   # 3.14
```

## 列表推导式

```python
squares = [x**2 for x in range(10)]          # [0, 1, 4, 9, ...]
evens = [x for x in range(20) if x % 2 == 0]  # 带条件
```

## 函数

```python
def greet(name: str, greeting: str = "Hello") -> str:
    """带默认参数和类型提示的函数。"""
    return f"{greeting}, {name}!"
```

## 下一步

- [ ] 控制流
- [ ] 数据结构
- [ ] 模块与包
- [ ] 面向对象
