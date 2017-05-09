import requests
import urllib


class Stats:
    def __init__(self, key, url):
        self.key = key
        self.url = url

    def overall(self, options):
        r = requests.get("%s/overall/?api_key=%s&%s" % (self.url, self.key, urllib.urlencode(options)))
        return r.json()

    def general(self, options):
        r = requests.get("%s/general/?api_key=%s&%s" % (self.url, self.key, urllib.urlencode(options)))
        return r.json()
