# FastAPI Notes Demo

一个使用 [FastAPI](https://fastapi.tiangolo.com/) 构建的最小化内存笔记 API，用于演示 FastAPI 的核心概念。

## 演示内容

| 概念 | 对应代码 |
|------|----------|
| Pydantic 请求/响应模型 | `NoteCreate` / `NoteUpdate` / `Note` |
| 路径参数 | `GET /notes/{note_id}` |
| 查询参数 + 校验 | `list_notes(skip, limit)` |
| CRUD 操作 | `POST` / `GET` / `PUT` / `DELETE` |
| HTTP 状态码 | `201` 创建、`204` 删除、`404` 未找到 |
| Lifespan 事件 | 启动时注入示例数据，关闭时清理 |
| 自动 OpenAPI 文档 | 访问 `/docs`（Swagger UI） |

## 运行

```bash
# 同步依赖（首次）
uv sync

# 启动开发服务器（带热重载）
uv run uvicorn demos.fastapi_demo.app:app --reload
```

启动后访问：

- 交互式文档（Swagger UI）：<http://127.0.0.1:8000/docs>
- ReDoc 文档：<http://127.0.0.1:8000/redoc>
- 健康检查：<http://127.0.0.1:8000/health>

也可以直接运行模块：

```bash
uv run python -m demos.fastapi_demo.app
```

## API 一览

| 方法 | 路径 | 说明 |
|------|------|------|
| `GET` | `/` | 落地页，指向文档 |
| `GET` | `/health` | 健康检查 |
| `GET` | `/notes` | 列出笔记（支持 `skip` / `limit` 分页） |
| `GET` | `/notes/{id}` | 获取单条笔记 |
| `POST` | `/notes` | 创建笔记（返回 `201`） |
| `PUT` | `/notes/{id}` | 更新笔记（支持部分更新） |
| `DELETE` | `/notes/{id}` | 删除笔记（返回 `204`） |

### 请求示例

创建笔记：

```bash
curl -X POST http://127.0.0.1:8000/notes \
  -H "Content-Type: application/json" \
  -d '{"title": "我的第一条笔记", "content": "Hello FastAPI"}'
```

更新笔记（只改标题）：

```bash
curl -X PUT http://127.0.0.1:8000/notes/2 \
  -H "Content-Type: application/json" \
  -d '{"title": "新标题"}'
```

## 测试

```bash
uv run pytest tests/test_fastapi_demo.py -v
```

测试使用 FastAPI 的 `TestClient`（基于 `httpx`），无需真正启动服务器。

## 项目结构

```
demos/fastapi_demo/
├── __init__.py
├── app.py          # FastAPI 应用（模型 + 路由 + lifespan）
└── README.md       # 本文件
```

> 数据保存在内存中，重启服务器后所有笔记会丢失（仅保留启动时注入的示例笔记）。
