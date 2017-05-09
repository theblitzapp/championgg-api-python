import requests
import urllib
from .utils import InvalidChampionIdError, InvalidRoleError

class Champions:
    def __init__(self, key, url):
        self.key = key
        self.url = url
        self.alldata = ""

    def all(self, options):
        if self.alldata == "":
            r = requests.get("%s/champions?api_key=%s&%s" % (self.url, self.key, urllib.urlencode(options)))
            self.alldata = r.json()
        return self.alldata

    def specific(self, id, options):
        if not id or type(id) is not 'integer':
            raise InvalidChampionIdError("Champion Id must be present and an integer.")
        r = requests.get("%s/champions/%d?api_key=%s&%s" % (self.url, id, self.key, urllib.urlencode(options)))
        return r.json()

    def specificRole(self, id, role, options):
        if not id or type(id) is not 'integer':
            raise InvalidChampionIdError("Champion Id must be present and an integer.")
        if role not in ['TOP', 'JUNGLE', 'MIDDLE', 'DUO_CARRY', 'DUO_SUPPORT']:
            raise InvalidRoleError("Role must be present and either be TOP, JUNGLE, MIDDLE, DUO_CARRY, or DUO_SUPPORT.")
        r = requests.get("%s/champions/%d/%s?api_key=%s&%s" % (self.url, id, role, self.key, urllib.urlencode(options)))
        return r.json()

    def specificMatchup(self, champ1, champ2, role, options):
        if not champ1 or type(champ1) is not 'integer':
            raise InvalidChampionIdError("Champion Id must be present and an integer.")
        if not champ2 or type(champ2) is not 'integer':
            raise InvalidChampionIdError("Champion Id must be present and an integer.")
        if role not in ['TOP', 'JUNGLE', 'MIDDLE', 'DUO_CARRY', 'DUO_SUPPORT']:
            raise InvalidRoleError("Role must be present and either be TOP, JUNGLE, MIDDLE, DUO_CARRY, or DUO_SUPPORT.")
        r = requests.get("%s/champions/%d/matchups/%d/%s?api_key=%s&%s" %
                         (self.url, champ1, champ2, role, self.key, urllib.urlencode(options)))
        return r.json()

