import fastmcp
from dotenv import load_dotenv
from starlette.responses import JSONResponse
import uvicorn

from .tools import (
    multiple_reports_tools,
    single_report_tool,
    aggregation_tools,
    agency_tools,
)

load_dotenv()

mcp = fastmcp.FastMCP("ai-cop-mcp-demo-server")

@mcp.custom_route("/health", methods=["GET"])
async def health_check(request):
    return JSONResponse({"status": "healthy", "service": "mcp-server"})

single_report_tool.register_tools(mcp)
agency_tools.register_tools(mcp)
multiple_reports_tools.register_tools(mcp)
aggregation_tools.register_tools(mcp)


app = mcp.http_app()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)