import fastmcp
from dotenv import load_dotenv
from starlette.responses import JSONResponse

from usdc_arc_mcp_demo.tools import (
    multiple_reports_tools,
    single_report_tool,
    aggregation_tools,
    agency_tools,
)
import os, sys


print("Environment PYTHONPATH:", os.getenv("PYTHONPATH"))
print("sys.path:", sys.path)

load_dotenv()

mcp = fastmcp.FastMCP("ai-cop-mcp-demo-server", stateless_http=True)

@mcp.custom_route("/health", methods=["GET"])
async def health_check(request):
    return JSONResponse({"status": "healthy", "service": "mcp-server"})

single_report_tool.register_tools(mcp)
agency_tools.register_tools(mcp)
multiple_reports_tools.register_tools(mcp)
aggregation_tools.register_tools(mcp)


app = mcp.http_app()
