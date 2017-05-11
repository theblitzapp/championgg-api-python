import requests
import urllib
from .utils import InvalidChampionIdError as _InvalidChampionIdError, InvalidRoleError as _InvalidRoleError

try:
    urlencode = urllib.urlencode
except AttributeError:  # They moved this function in Python 3
    urlencode = urllib.parse.urlencode


class Champions(object):
    def __init__(self, key, url):
        self.__key = key
        self.__url = url
        self.__alldata = ""

    def all(self, options=None):
        if options is None:
            options = {}
        if self.__alldata == "":
            r = requests.get("%s/champions?api_key=%s&%s" % (self.__url, self.__key, urlencode(options)))
            self.__alldata = r.json()
        return self.__alldata

    def specific(self, id, options=None):
        if options is None:
            options = {}
        if not isinstance(id, int):
            raise _InvalidChampionIdError("Champion Id must be present and an integer.")
        r = requests.get("%s/champions/%d?api_key=%s&%s" % (self.__url, id, self.__key, urlencode(options)))
        return r.json()

    def specific_role(self, id, role, options=None):
        if options is None:
            options = {}
        if not isinstance(id, int):
            raise _InvalidChampionIdError("Champion Id must be present and an integer.")
        if role not in ['TOP', 'JUNGLE', 'MIDDLE', 'DUO_CARRY', 'DUO_SUPPORT']:
            raise _InvalidRoleError("Role must be present and either be TOP, JUNGLE, MIDDLE, DUO_CARRY, or DUO_SUPPORT.")
        r = requests.get("%s/champions/%d/%s?api_key=%s&%s" % (self.__url, id, role, self.__key, urlencode(options)))
        try:
            return r.json()[0]
        except IndexError:
            return None

    def specific_matchup(self, champ1, champ2, role, options=None):
        if options is None:
            options = {}
        if not isinstance(champ1, int):
            raise _InvalidChampionIdError("Champion Id must be present and an integer.")
        if not isinstance(champ2, int):
            raise _InvalidChampionIdError("Champion Id must be present and an integer.")
        if role not in ['TOP', 'JUNGLE', 'MIDDLE', 'DUO_CARRY', 'DUO_SUPPORT']:
            raise _InvalidRoleError("Role must be present and either be TOP, JUNGLE, MIDDLE, DUO_CARRY, or DUO_SUPPORT.")
        r = requests.get("%s/champions/%d/matchups/%d/%s?api_key=%s&%s" %
                         (self.__url, champ1, champ2, role, self.__key, urlencode(options)))
        return r.json()
