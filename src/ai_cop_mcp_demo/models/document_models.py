from typing import Optional
from pydantic import BaseModel, Field


class SearchDocumentsParams(BaseModel):
    search_term: Optional[str] = Field(None, description="Full-text search term")
    docket_id: Optional[str] = Field(None, description="Filter by docket ID")
    posted_date: Optional[str] = Field(None, description="Exact posted date YYYY-MM-DD")
    posted_date_ge: Optional[str] = Field(None, description="Posted date >= YYYY-MM-DD")
    posted_date_le: Optional[str] = Field(None, description="Posted date <= YYYY-MM-DD")
    document_type: Optional[str] = Field(None, description="Filter by document type")
    include: Optional[str] = Field(
        None, description="Include related objects like attachments"
    )
    fields: Optional[str] = Field(None, description="Sparse fieldset for documents")
    sort: Optional[str] = Field(
        "-postedDate", description="Sort expression, default desc by postedDate"
    )
    page_size: int = Field(25, ge=1, le=250, description="Number of results per page")
    page_number: int = Field(1, ge=1, description="Page number to fetch")
    auto_paginate: bool = Field(False, description="Fetch multiple pages automatically")
    max_pages: int = Field(
        5, ge=1, le=5, description="Max pages to fetch when auto_paginate=True"
    )
    api_key: Optional[str] = Field(None, description="API key for Regulations.gov")
