from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, RootModel


class Layout(Enum):
    STANDARD = "standard"


class Rarity(Enum):
    COMMON = "common"
    MYTHIC = "mythic"
    RARE = "rare"
    UNCOMMON = "uncommon"


class CardDetail(BaseModel):
    name: str
    mtga_id: int
    color: str
    rarity: Rarity
    url: str
    url_back: str
    types: List[str]
    layout: Layout
    seen_count: int
    pick_count: int
    game_count: int
    pool_count: int
    play_rate: Optional[float] = None
    opening_hand_game_count: int
    drawn_game_count: int
    ever_drawn_game_count: int
    never_drawn_game_count: int
    avg_seen: Optional[float] = None
    avg_pick: Optional[float] = None
    win_rate: Optional[float] = None
    opening_hand_win_rate: Optional[float] = None
    drawn_win_rate: Optional[float] = None
    ever_drawn_win_rate: Optional[float] = None
    never_drawn_win_rate: Optional[float] = None
    drawn_improvement_win_rate: Optional[float] = None


class CardDetails(RootModel):
    root: list[CardDetail]
