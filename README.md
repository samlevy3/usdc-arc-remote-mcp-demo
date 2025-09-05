# ai-cop-mcp-demo

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
REGSGOV_API_KEY=your_api_key_here
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
