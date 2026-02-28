from mcp.server.fastmcp import FastMCP
from math import pow

# Initialize FastMCP server
mcp = FastMCP("dbconnect")

# Constants
USER_AGENT = "dbconnect/1.0"

@mcp.tool()
def calculate(a:int, b:int)->str:
    """Run some custom calculation logic"""
    return f"The calculated value would be {pow(a+b, 2) }"

@mcp.resource("greeting://{name}")
def get_greeting(name:str)->str:
    return f"Hello, {name}"

def main():
    # Initialize and run the server
    mcp.run(transport="sse")


if __name__ == "__main__":
    main()