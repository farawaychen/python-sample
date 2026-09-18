# uv 常用命令速查表

## 项目初始化

```bash
uv init              # 初始化项目（含 src 布局 + main.py）
uv init --bare       # 仅生成 pyproject.toml
uv init --name myapp # 指定项目名
```

## 依赖管理

```bash
uv add requests            # 添加依赖
uv add --dev pytest        # 添加开发依赖
uv add --optional dev x    # 添加可选依赖组
uv remove requests         # 移除依赖
uv sync                    # 同步环境到锁定状态
uv lock                    # 重新解析锁定文件
uv lock --upgrade          # 升级所有依赖
uv pip list                # 列出已安装包
```

## 运行

```bash
uv run python main.py      # 在虚拟环境中运行
uv run pytest              # 运行测试
uv tool run ruff check .   # 运行工具
uv python install 3.13     # 安装特定 Python 版本
uv python list             # 列出可用的 Python
```

## 虚拟环境

```bash
uv venv              # 创建 .venv
uv venv --python 3.13  # 指定版本
uv python pin 3.12   # 在项目中固定 Python 版本
```

## 工具管理

```bash
uv tool install ruff       # 全局安装工具
uv tool list               # 列出工具
uv tool run black --help   # 临时运行工具
```
