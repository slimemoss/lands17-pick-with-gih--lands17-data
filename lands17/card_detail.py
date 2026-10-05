from datetime import datetime

from cache import requests
from mtg.color import TWO_COLOR

from lands17.card_detail_schema import CardDetails


def getOneColor(
    expansion: str,
    color: str | None = None,
    start_date: datetime | None = None,
    time_period: str | None = "ALL_TIME",
):
    url = (
        f"https://www.17lands.com/api/card_data"
        f"?expansion={expansion.upper()}"
        f"&event_type=PremierDraft"
    )

    if time_period is not None:
        url += f"&time_period={time_period}"
    elif start_date is not None:
        url += (
            f"&start_date={start_date.strftime('%Y-%m-%d')}"
            f"&end_date={datetime.today().strftime('%Y-%m-%d')}"
        )

    if color is not None:
        url += f"&colors={color.upper()}"

    res = requests.get(url).json()
    if isinstance(res, dict) and "data" in res:
        return CardDetails(res["data"])
    return CardDetails(res)


def get(
    expansion: str,
    start_date: datetime | None = None,
    time_period: str | None = "ALL_TIME",
):
    colors: list[str | None] = [None, *TWO_COLOR]
    return [
        (c, getOneColor(expansion, color=c, start_date=start_date, time_period=time_period))
        for c in colors
    ]
