from fastmcp import FastMCP
from tools.fetch import fetch_data
from tools.store import store_data

# Initialize the MCP server
mcp = FastMCP("Registration APP")

# Register tools
mcp.tool(name = "store_data",
         description="Register a new user by saving their info to a CSV.",
         func = store_data)

mcp.tool(description="""
This tool fetches all previously stored user data from the CSV file and formats it for display.
""")(fetch_data)

if __name__ == "__main__":
    mcp.run(transport="streamable-http")