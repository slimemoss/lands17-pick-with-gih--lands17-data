from datetime import datetime

from cache import requests
from mtg.color import TWO_COLOR

from lands17.card_detail_schema import CardDetails


def getOneColor(expansion: str, start_date: datetime, color: str | None):
    url = (
        f"https://www.17lands.com/card_ratings/data"
        f"?expansion={expansion.upper()}"
        f"&event_type=PremierDraft"
        f"&start_date={start_date.strftime('%Y-%m-%d')}"
        f"&end_date={datetime.today().strftime('%Y-%m-%d')}"
    )

    if color is not None:
        url += f"&colors={color.upper()}"

    return CardDetails(requests.get(url).json())


def get(expansion: str, start_date: datetime):
    colors: list[str | None] = [None, *TWO_COLOR]
    return [(c, getOneColor(expansion, start_date, c)) for c in colors]
