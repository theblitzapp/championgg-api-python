import requests


class Stats:
    def __init__(self, key, url):
        self.key = key
        self.url = url

    def all(self):
        r = requests.get(self.url+"/stats?api_key="+self.key)
        return r.json()

    def role(self, role, type="improvement", order="most", p={}):
        params = {"api_key": self.key}
        params.update(p)
        if type == "improvement":
            if order == "most":
                r = requests.get(self.url+"/stats/role/"+role+"/mostImproved", params=params)
            else:
                r = requests.get(self.url+"/stats/role/"+role+"/leastImproved", params=params)
        elif type == "winning":
            if order == "most":
                r = requests.get(self.url+"/stats/role/"+role+"/mostWinning", params=params)
            else:
                r = requests.get(self.url+"/stats/role/"+role+"/leastWinning", params=params)
        else:
            if order == "most":
                r = requests.get(self.url+"/stats/role/"+role+"/bestPerformance", params=params)
            else:
                r = requests.get(self.url+"/stats/role/"+role+"/worstPerformance", params=params)
        print r.text
        return r.json()

    def champion(self, name):
        r = requests.get(self.url+"/stats/"+name+"?api_key="+self.key)
        return r.json()

    def champs(self, type="played", order="most", p={}):
        params = {"api_key": self.key}
        params.update(p)
        if type == "played":
            if order == "most":
                r = requests.get(self.url+"/stats/champs/mostPlayed", params=params)
            else:
                r = requests.get(self.url+"/stats/champs/leastPlayed", params=params)
        elif type == "winning":
            if order == "most":
                r = requests.get(self.url+"/stats/champs/mostWinning", params=params)
            else:
                r = requests.get(self.url+"/stats/champs/leastWinning", params=params)
        elif type == "rated":
            if order == "most":
                r = requests.get(self.url+"/stats/champs/bestRated", params=params)
            else:
                r = requests.get(self.url+"/stats/champs/worstRated", params=params)
        else:
            r = requests.get(self.url+"/stats/champs/mostBanned", params=params)
        return r.json()