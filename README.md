<div align="center">

# ⚡ FastMCP Template

**A production-ready template for building [Model Context Protocol (MCP)](https://modelcontextprotocol.io) servers with [FastMCP](https://github.com/jlowin/fastmcp).**

![Python](https://img.shields.io/badge/python-3.14+-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![FastMCP](https://img.shields.io/badge/FastMCP-3.0.0b2-blue.svg?style=for-the-badge)

</div>

---

## Features

- **[FastMCP](https://github.com/jlowin/fastmcp)** — Framework for building MCP servers
- **[uv](https://docs.astral.sh/uv/)** — Modern Python package and dependency manager
- **Python 3.14** — Latest Python version
- **[ty](https://github.com/tjdevries/ty)** — Static type checker
- **[ruff](https://docs.astral.sh/ruff/)** — Fast Python linter & formatter
- **[pydantic-settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)** — Configuration management from environment variables
- **Testing with coverage** — pytest + pytest-asyncio with code coverage reports
- **Production-ready Dockerfile** — Multi-stage build with non-root user, bytecode compilation, and minimal base image

---

## Requirements

- [uv](https://docs.astral.sh/uv/) (package manager)

---

## Getting Started

### 1. Install dependencies

```bash
uv sync
```

### 2. Run the server (development)

```bash
make dev
```

This starts the server with `--reload` on `http://0.0.0.0:8000` using the `http` transport by default.

Override transport or port:

```bash
make dev MCP_TRANSPORT=stdio
make dev MCP_PORT=9000
```

### 3. Run manually

```bash
python -m app.main
```

---

## Configuration

Settings are loaded from environment variables (prefix `MCP_`) or a `.env` file.

| Variable        | Default  | Description                                      |
|-----------------|----------|--------------------------------------------------|
| `MCP_TRANSPORT` | `stdio`  | Transport: `stdio`, `http`, `sse`, `streamable-http` |
| `MCP_PORT`      | `8000`   | Port (used only for HTTP-based transports)       |

**Example `.env`:**

```env
MCP_TRANSPORT=http
MCP_PORT=8080
```

---

## Available Commands

| Command       | Description                                    |
|---------------|------------------------------------------------|
| `make dev`    | Start server in dev mode with auto-reload      |
| `make test`   | Run the test suite with coverage report        |
| `make build`  | Build the Docker image (`podman build`)        |
| `make start`  | Run the container in production (`podman run`) |

---


### Build

```bash
make build
```

or directly with podman:

```bash
podman build -t mcp:latest .
```

### Run

```bash
make start
```

The container exposes port `8080` by default (`MCP_PORT=8080`, `MCP_TRANSPORT=http`).

---

## Testing

```bash
make test
```

Tests use `pytest-asyncio` and a shared `Client` fixture from `tests/conftest.py`.

---

## Adding Tools

Register new tools in [app/mcp/server.py](app/mcp/server.py):

```python
@mcp.tool
def my_tool(param: str) -> str:
    """Description shown to the LLM."""
    return param.upper()
```
