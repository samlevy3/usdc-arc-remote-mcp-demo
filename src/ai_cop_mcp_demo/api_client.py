import os
import httpx
from typing import Any, Dict

API_BASE = "https://api.regulations.gov/v4"


def fetch_documents(params: Dict[str, Any], page: int = 1) -> Dict:
    local_params = dict(params)
    local_params["page[number]"] = page

    # Set api_key as a URL param
    if "api_key" not in local_params or not local_params["api_key"]:
        local_params["api_key"] = os.getenv("REGSGOV_API_KEY") or "DEMO_KEY"

    with httpx.Client(timeout=30.0) as client:
        resp = client.get(f"{API_BASE}/documents", headers={}, params=local_params)
        resp.raise_for_status()
        return resp.json()
