# analytics.usa.gov MCP Server

⚠️ **DISCLAIMER: This is a proof of concept and is not intended for production use.**

Demo MCP Server for AI Community Of Practice

## Overview

This project is a demonstration Model Context Protocol (MCP) server for analytics.usa.gov data, designed to showcase how LLMs can interact with government analytics APIs using the MCP standard. The codebase is structured to start simple and build up in capability:

- **single_report_tool**: Provides basic access to a single analytics report at a time, ideal for simple queries and initial integration.
- **multiple_reports_tools**: Adds support for fetching and handling multiple reports, allowing more complex queries and comparisons.
- **aggregation_tools**: Enables aggregation of analytics data over time periods (week, month, year) and by various dimensions (such as source or agency), supporting more advanced analytics and summarization.

Each tool is registered with the MCP server and can be called by an LLM or other MCP-compatible client. The project is intended as a learning and experimentation platform for building and extending MCP-based analytics APIs.

## Quick Start (Recommended)

### Option 1: Install via uv

```sh
uv tool install git+https://github.com/GSA-TTS/ai-cop-mcp-demo/
```

This will install the MCP server as a CLI tool. You can then run:

```sh
ai-cop-mcp-demo
```

#### Simple way to connect to Claude 

1. Get the installed tool path:
   ```sh
   which ai-cop-mcp-demo
   ```

2. Copy the path into Claude MCP config:
   ```json
   {
     "mcpServers": {
       "usa-spending": {
         "command": "/path/to/ai-cop-mcp-demo",
         "args": [],
         "env": {}
       }
     }
   }
   ```

## Development Setup

### Option 2: Using Hatch or uv

#### Using Hatch

1. Install [Hatch](https://hatch.pypa.io/latest/):
   ```sh
   pip install hatch
   ```
2. Create a virtual environment and install dependencies:
   ```sh
   hatch env create
   ```
3. Run the server:
   ```sh
   hatch run ai-cop-mcp-demo
   ```
   Or:
   ```sh
   hatch shell
   ai-cop-mcp-demo
   ```

#### Using uv

1. Install [uv](https://github.com/astral-sh/uv):
   ```sh
   pip install uv
   ```
2. Install dependencies:
   ```sh
   uv pip install -r requirements.txt
   ```
   Or, for PEP 621 projects:
   ```sh
   uv pip install -e .
   ```
3. Run the server:
   ```sh
   ai-cop-mcp-demo
   ```

## Configuration

Set your Regulations.gov API key in a `.env` file:
```
DAP_API_KEY=your_api_key_here
```

## Project Structure

- `src/ai_cop_mcp_demo/` – Main package code
- `test/` – Tests

## Linting

This project uses [ruff](https://docs.astral.sh/ruff/) for linting and code style checks.

To lint your code, run:
```sh
hatch run ruff check src/
```
Or:
```sh
hatch shell
ruff check src/
```

## Resources

- [Model Context Protocol Documentation](https://modelcontextprotocol.io/docs/getting-started/intro)
- [FastMCP Documentation](https://gofastmcp.com/getting-started/welcome)
- [GSA DAP API Documentation](https://open.gsa.gov/api/dap/)
