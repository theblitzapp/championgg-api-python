"""

A Python lib for the champion.gg API

Usage:

    import py_gg

    py_gg.init(API_KEY)
    champs = py_gg.champions.all()

"""

__title__ = "py_gg"
__version__ = '2.0.1'
__author__ = "Philip Fugate"
__copyright__ = "Copyright 2017 Solomid Corp"


_api_key = ""
_url = "http://api.champion.gg/v2"
champions = {}
statistics = {}

import requests as _requests
from .utils import InvalidAPIKeyError as _InvalidAPIKeyError
from .champions import Champions as _Champions
from .stats import Stats as _Stats


def init(key):
    global _api_key, champions, _url, statistics
    _api_key = key
    check = _requests.get(_url+"/ping?api_key="+_api_key)
    if check.status_code == 403:
        raise _InvalidAPIKeyError("Invalid API Key")
    champions = _Champions(_api_key, _url)
    statistics = _Stats(_api_key, _url)
