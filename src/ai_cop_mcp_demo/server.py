import logging
import fastmcp
from .tools import documents
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger("ai-cop-mcp-demo")
logger.setLevel(logging.INFO)

mcp = fastmcp.FastMCP("ai-cop-mcp-demo-server")
documents.register_tools(mcp)


def main():
    mcp.run()


if __name__ == "__main__":
    main()
