import time
from hashlib import sha256
from pathlib import Path

import requests
from cache import core


def _path(url: str) -> Path:
    hash = sha256(url.encode()).hexdigest()[:200]
    return Path('limited.cache.requests.get', f'{hash}.pickle')


def _get(url: str) -> requests.Response:
    print(f'Download: {url}')
    return requests.get(url)


def get(url: str, clear_cache=False) -> requests.Response:
    r''' http.GET with cache
    '''

    path = _path(url)

    resp, isHit = core.read_cache(path, lambda: _get(url), clear_cache)
    if resp.status_code != 200:
        core.clear_cache(path)
    if not isHit:
        time.sleep(3)
    return resp
