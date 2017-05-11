import requests
import urllib

try:
    urlencode = urllib.urlencode
except AttributeError:  # They moved this function in Python 3
    urlencode = urllib.parse.urlencode


class Stats(object):
    def __init__(self, key, url):
        self.key = key
        self.url = url

    def overall(self, options=None):
        if options is None:
            options = {}
        r = requests.get("%s/overall/?api_key=%s&%s" % (self.url, self.key, urlencode(options)))
        return r.json()

    def general(self, options=None):
        if options is None:
            options = {}
        r = requests.get("%s/general/?api_key=%s&%s" % (self.url, self.key, urlencode(options)))
        return r.json()
