from typing import Any
from ..api_client import fetch_documents
from ..models.document_models import SearchDocumentsParams


def register_tools(mcp):
    @mcp.tool
    def search_documents(params: SearchDocumentsParams) -> Any:
        # Map Pydantic model to API filters
        api_params = {}
        if params.search_term:
            api_params["filter[searchTerm]"] = params.search_term
        if params.docket_id:
            api_params["filter[docketId]"] = params.docket_id
        if params.posted_date:
            api_params["filter[postedDate]"] = params.posted_date
        if params.posted_date_ge:
            api_params["filter[postedDate][ge]"] = params.posted_date_ge
        if params.posted_date_le:
            api_params["filter[postedDate][le]"] = params.posted_date_le
        if params.document_type:
            api_params["filter[documentType]"] = params.document_type
        if params.include:
            api_params["include"] = params.include
        if params.fields:
            api_params["fields[documents]"] = params.fields
        if params.sort:
            api_params["sort"] = params.sort
        api_params["page[size]"] = params.page_size
        if params.api_key:
            api_params["api_key"] = params.api_key

        if not params.auto_paginate:
            return fetch_documents(api_params, page=params.page_number)

        combined = {"data": [], "meta": {}, "links": {}}  # Ensure correct types
        current_page = params.page_number
        pages_fetched = 0

        while pages_fetched < params.max_pages:
            payload = fetch_documents(api_params, page=current_page)
            data = payload.get("data", [])
            combined["data"].extend(data)
            combined["meta"] = payload.get("meta") or {}
            combined["links"] = payload.get("links") or {}
            pages_fetched += 1

            links = payload.get("links") or {}
            next_link = links.get("next")
            if not next_link or not data:
                break

            current_page += 1

        return combined
