"""

A Python lib for the champion.gg API

Usage:

    import py_gg

    py_gg.init(API_KEY)
    champs = py_gg.champions.all()

"""

__title__ = "py_gg"
__version__ = '2.0.0'
__author__ = "Philip Fugate"
__copyright__ = "Copyright 2017 Solomid Corp"


api_key = ""
url = "http://api.champion.gg/v2"
champions = {}
statistics = {}

import requests
from .utils import InvalidAPIKeyError
from .champions import Champions
from .stats import Stats

def init(key):
    global api_key, champions, url, statistics
    api_key = key
    check = requests.get(url+"/ping?api_key="+api_key)
    if check.status_code == 403:
        raise InvalidAPIKeyError("Invalid API Key")
    champions = Champions(api_key, url)
    statistics = Stats(api_key, url)

