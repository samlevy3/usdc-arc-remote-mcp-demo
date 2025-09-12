# analytics.usa.gov MCP Server

⚠️ **DISCLAIMER: This is a proof of concept and is not intended for production use.**

Demo MCP Server for AI Community Of Practice

## Setup

### Using Hatch

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
    Or can also do:
    ```sh
    hatch shell 
    ai-cop-mcp-demo
    ```

### Using uv

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
Or can also do:
```sh
hatch shell 
ruff check src/
```

## Resources

- [Model Context Protocol Documentation](https://modelcontextprotocol.io/docs/getting-started/intro)
- [FastMCP Documentation](https://gofastmcp.com/getting-started/welcome)
- [GSA DAP API Documentation](https://open.gsa.gov/api/dap/)
