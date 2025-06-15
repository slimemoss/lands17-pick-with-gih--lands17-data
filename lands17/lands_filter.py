from cache import requests

from lands17.filter_schema import Filter


def get():
    url = "https://www.17lands.com/data/filters"
    return Filter(**requests.get(url).json())
