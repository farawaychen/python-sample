# Python Sample

一个使用 [uv](https://docs.astral.sh/uv/) 管理的 Python 学习项目。

## 项目结构

```
python-sample/
├── pyproject.toml        # 项目配置（依赖、脚本、元数据）
├── main.py               # 主入口，演示模块导入
├── utils.py              # 工具函数模块（可复用代码）
├── exercises/            # 练习目录
│   ├── __init__.py
│   ├── 001_hello.py      # 基础打印与 f-string
│   └── 002_variables.py  # 变量、类型与函数
├── demos/                # 独立示例项目
│   └── fastapi_demo/     # FastAPI 笔记 API 示例
│       ├── __init__.py
│       ├── app.py        # FastAPI 应用（模型 + 路由 + lifespan）
│       └── README.md     # 示例说明
├── notes/                # 学习笔记
└── tests/                # 测试文件
```

## 前置要求

- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- Python 3.12+（uv 会自动管理）

## 快速开始

```bash
# 同步依赖（自动创建 .venv 虚拟环境）
uv sync

# 运行主程序
uv run main.py

# 运行某个练习
uv run exercises/001_hello.py
uv run exercises/002_variables.py

# 运行工具模块自检
uv run utils.py
```

## 示例项目

### FastAPI 笔记 API

一个使用 [FastAPI](https://fastapi.tiangolo.com/) 构建的内存笔记 API，演示 Pydantic 模型、CRUD、路径/查询参数、lifespan 事件与自动 OpenAPI 文档。

```bash
# 启动开发服务器
uv run uvicorn demos.fastapi_demo.app:app --reload

# 打开交互式文档
# http://127.0.0.1:8000/docs
```

详见 [`demos/fastapi_demo/README.md`](demos/fastapi_demo/README.md)。

## 常用 uv 命令

| 命令 | 说明 |
|------|------|
| `uv sync` | 安装/同步所有依赖 |
| `uv run <cmd>` | 在虚拟环境中运行命令 |
| `uv add <pkg>` | 添加运行时依赖 |
| `uv add --dev <pkg>` | 添加开发依赖 |
| `uv remove <pkg>` | 移除依赖 |
| `uv lock` | 更新依赖锁文件 |
| `uv pip install <pkg>` | 临时安装（不更新 pyproject.toml） |

## 测试与代码质量

```bash
# 运行测试
uv run pytest

# 代码检查
uv run ruff check .

# 自动格式化
uv run ruff format .
```

## 学习计划

- [ ] 001 - Hello World 与 print
- [ ] 002 - 变量、类型与函数
- [ ] 003 - 控制流（if / for / while）
- [ ] 004 - 数据结构（list / dict / set / tuple）
- [ ] 005 - 模块与包
- [ ] 006 - 面向对象
- [ ] 007 - 异常处理
- [ ] 008 - 文件 I/O
- [ ] 009 - 装饰器与生成器
- [ ] 010 - 异步编程入门
