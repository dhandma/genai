# Simple MCP Server — Remote Setup Guide

This guide covers setting up a simple FastMCP server to host on a remote server.

## Prerequisites

- Python 3.10+ installed
- `git` (optional, for cloning)

## Setup Steps

### 1. Create a folder for the MCP server

```bash
mkdir remote_mcp_server
cd remote_mcp_server
```

### 2. Install `uv` (if not already installed)

Check if `uv` is installed:

```bash
uv --version
```

If not installed, install it:

```bash
pip install uv
```

### 3. Initialize the project using `uv init`

```bash
uv init
```

This creates a Python project structure with `pyproject.toml` and other necessary files.

### 4. Install FastMCP using `uv add`

```bash
uv add fastmcp
```

This adds `fastmcp` to your project dependencies.

### 5. Update `main.py`

Add your MCP server code to `main.py`. Here's a basic example:

```python
from fastmcp import FastMCP
import random
import json

mcp = FastMCP("Simple calculator server")

@mcp.tool()
def add(a: float, b: float) -> float:
    """Returns the sum of two numbers."""
    return a + b

@mcp.tool()
def random_number(min_val: int = 1, max_val: int = 100) -> int:
    """Returns a random integer between min_val and max_val."""
    return random.randint(min_val, max_val)

@mcp.resource("info://server")
def server_info() -> str:
    """Returns server information in JSON format."""
    info = {
        "name": "Simple Calculator Server",
        "version": "1.0",
        "description": "A server that provides basic calculator functions and random number generation."
    }
    return json.dumps(info, indent=2)

# Start the server
if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8080)
```

## Running the Server

### Terminal 1: Start the main server

```bash
uv run main.py
```

This starts the FastMCP server listening on `http://0.0.0.0:8080`.

## Debugging the Setup

### Terminal 2: Run the MCP Inspector (for debugging)

Open a new terminal in the same project directory and run:

```bash
uv run fastmcp dev main.py
```

This opens the **MCP Inspector** where you can:
- List available tools
- List available resources
- Test tool execution
- Inspect resource outputs

## Testing the Server

Once the server is running, you can test it using `curl`:

```bash
# Test the MCP endpoint
curl -v http://127.0.0.1:8080/mcp

# Or if running locally:
curl http://localhost:8080/
```

## File Structure

After setup, your project should look like:

```
remote_mcp_server/
├── .venv/                  (virtual environment, if created)
├── pyproject.toml          (project configuration, created by uv init)
├── main.py                 (your FastMCP server code)
├── uv.lock                 (dependency lock file)
└── README.md               (this file)
```

## Troubleshooting

- **`uv` command not found**: Make sure `uv` is installed and in your PATH. Run `pip install uv` if needed.
- **`fastmcp` import error**: Ensure `fastmcp` was installed via `uv add fastmcp`.
- **Port already in use**: If port 8080 is in use, modify the `port` parameter in `main.py` (e.g., change to `port=8081`).
- **MCP Inspector won't open**: Make sure the server code is valid and the `fastmcp` package is properly installed.

## Next Steps

- Customize the tools and resources in `main.py` for your use case.
- Deploy to a remote server by copying the project files and running `uv run main.py` on the remote machine.
- Integrate with clients or proxies that communicate with the MCP server via HTTP.
