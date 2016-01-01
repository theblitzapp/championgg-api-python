"""

A Python lib for the champion.gg API

Usage:

    import py_gg

    py_gg.init(API_KEY)
    champs = py_gg.champion.all()

"""

__title__ = "py_gg"
__version__ = '1.0.0'
__author__ = "Philip Fugate"
__copyright__ = "Copyright 2016 Solomid Corp"


api_key = ""
url = "http://api.champion.gg"
champion = {}
stats = {}

import requests
from .utils import InvalidAPIKeyError


def init(key):
    global api_key, champion, url, stats
    api_key = key
    check = requests.get(url+"/ping?api_key="+api_key)
    if check.status_code == 403:
        raise InvalidAPIKeyError("Invalid API Key")
    import champions as c
    import stats as s
    champion = c.Champions(api_key, url)
    stats = s.Stats(api_key, url)
