import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Dict, Optional

from pydantic import BaseModel


class CardData(BaseModel):
    gih: Dict[str, float | None]
    alsa: Optional[float] = None


SetData = Dict[str, CardData]


class CardDataFile(BaseModel):
    update_date: str
    data: SetData


def write(expansion: str, data: SetData):
    JST = timezone(timedelta(hours=9))
    now_jst = datetime.now(JST)
    now_str = now_jst.strftime("%Y-%m-%d %H:%M:%S (JST)")

    filepath = Path("public_data", "{}.json".format(expansion))
    filepath.parent.mkdir(exist_ok=True, parents=True)
    with open(filepath, 'w') as f:
        json.dump(CardDataFile(update_date=now_str, data=data).model_dump(), f)
