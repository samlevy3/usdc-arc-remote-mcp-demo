from enum import Enum

MCP_TOOL_LIST_LIMIT = 10000

MAX_PAGE_SIZE = 10000


class AggregationLevel(str, Enum):
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    YEARLY = "yearly"


REPORT_GROUP_BY = {
    "download": {
        "group_by": ["page", "file_name", "page_title"],
        "value_key": "total_events",
    },
    "traffic-source": {
        "group_by": ["source", "session_default_channel_group"],
        "value_key": "visits",
    },
    "device-model": {"group_by": ["mobile_device"], "value_key": "visits"},
    "domain": {"group_by": ["domain"], "value_key": "visits"},
    "site": {"group_by": ["domain"], "value_key": "visits"},
    "second-level-domain": {"group_by": ["domain"], "value_key": "visits"},
    "language": {"group_by": ["language"], "value_key": "visits"},
    "os-browser": {"group_by": ["os", "browser"], "value_key": "visits"},
    "windows-browser": {"group_by": ["browser", "os_version"], "value_key": "visits"},
    "browser": {"group_by": ["browser"], "value_key": "visits"},
    "os": {"group_by": ["os"], "value_key": "visits"},
    "windows": {"group_by": ["os_version"], "value_key": "visits"},
    "device": {"group_by": ["device"], "value_key": "visits"},
}
