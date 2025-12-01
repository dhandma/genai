from fastmcp import FastMCP 
import random 
import json 

mcp = FastMCP("Simple calculkator server")

@mcp.tool()
def add(a: float, b: float) -> float:
    """Returns the sum of two numbers."""
    return a + b

@mcp.tool()
def random_numer(min_val: int=1, max_val: int=100) -> int:
    """Returns a random integer between min_val and max_val."""
    return random.randint(min_val, max_val)

@mcp.resource("info://server")
def server_info()->str:
    """Returns server information in JSON format."""
    info = {
        "name": "Simple Calculator Server",
        "version": "1.0",
        "description": "A server that provides basic calculator functions and random number generation."
    }
    return json.dumps(info, indent=2)

#start the server 
if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)