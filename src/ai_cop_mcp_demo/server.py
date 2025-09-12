import fastmcp
from dotenv import load_dotenv

from .tools import (
    multiple_reports_tools,
    single_report_tool,
    aggregation_tools,
    agency_tools,
)

load_dotenv()

mcp = fastmcp.FastMCP("ai-cop-mcp-demo-server")

# Example tool 
@mcp.tool("add", description="Add two numbers")
def add(a: int, b: int) -> int:
    return a + b

single_report_tool.register_tools(mcp)
agency_tools.register_tools(mcp)
multiple_reports_tools.register_tools(mcp)
aggregation_tools.register_tools(mcp)


def main():
    mcp.run()


if __name__ == "__main__":
    main()
