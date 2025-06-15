from pydantic import BaseModel
from typing import List, Optional, Dict
from datetime import datetime


class Filter(BaseModel):
    colors: List[Optional[str]]
    expansions: List[str]
    formats: List[str]
    formats_by_expansion: Dict[str, List[str]]
    groups: List[Optional[str]]
    ranked_formats: List[str]
    start_dates: Dict[str, datetime]
