from typing import Optional
from pydantic import BaseModel, Field, field_validator


class QueryParams(BaseModel):
    after: Optional[str] = Field(None, description="Start date (YYYY-MM-DD)")
    before: Optional[str] = Field(None, description="End date (YYYY-MM-DD)")
    limit: Optional[int] = Field(None, description="Number of results per page")
    page: Optional[int] = Field(None, description="Page number for pagination")


class BaseReportParams(BaseModel):
    report_name: str = Field(
        ..., description="Report type (e.g., site, download, os, traffic-source)"
    )
    query_params: Optional[QueryParams] = Field(
        ..., description="Additional query parameters"
    )


class ReportParams(BaseReportParams):
    """Parameters for global reports."""

    pass


class AgencyReportParams(BaseReportParams):
    agency: str = Field(..., description="Agency slug (e.g., nasa, gsa, nih)")


class DomainReportParams(BaseReportParams):
    domain: str = Field(..., description="Domain name (e.g., gsa.gov, nasa.gov)")
    report_name: str = Field(
        ...,
        description="Report type (can only be site, download, os, or traffic-source)",
    )

    @field_validator("report_name")
    @classmethod
    def validate_report_name(cls, v):
        allowed = ["site", "domain", "download", "second-level"]
        if v not in allowed:
            raise ValueError(f"report_name must be one of: {allowed}")
        return v
