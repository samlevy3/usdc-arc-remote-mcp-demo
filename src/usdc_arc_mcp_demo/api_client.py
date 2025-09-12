import os
import httpx
from typing import Any, Dict, Optional

API_BASE = "https://api.gsa.gov/analytics/dap/v2"


async def get(endpoint: str, params: Optional[Dict[str, Any]] = None) -> Any:
    headers = {"x-api-key": os.getenv("DAP_API_KEY", "DEMO_KEY")}

    url = f"{API_BASE}{endpoint}"

    async with httpx.AsyncClient(timeout=30.0) as client:
        resp = await client.get(url, headers=headers, params=params)
        resp.raise_for_status()
        return resp.json()
