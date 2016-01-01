import requests


class Champions:
    def __init__(self, key, url):
        self.key = key
        self.url = url
        self.alldata = ""

    def all(self):
        if self.alldata == "":
            r = requests.get(self.url+"/champion?api_key="+self.key)
            self.alldata = r.json()
        return self.alldata

    def specific(self, name):
        r = requests.get(self.url+"/champion/"+name+"?api_key="+self.key)
        return r.json()

    def general(self, name):
        r = requests.get(self.url+"/champion/"+name+"/general?api_key="+self.key)
        return r.json()

    def skills(self, name, order=""):
        if order == "popular":
            r = requests.get(self.url+"/champion/"+name+"/skills/mostPopular?api_key="+self.key)
        elif order == "winning":
            r = requests.get(self.url+"/champion/"+name+"/skills/mostWins?api_key="+self.key)
        else:
            r = requests.get(self.url+"/champion/"+name+"/skills?api_key="+self.key)
        return r.json()

    def items(self, name, starting=True, order="popular"):
        if starting:
            if order == "popular":
                r = requests.get(self.url+"/champion/"+name+"/items/starters/mostPopular?api_key="+self.key)
            else:
                r = requests.get(self.url+"/champion/"+name+"/items/starters/mostWins?api_key="+self.key)
        else:
            if order == "popular":
                r = requests.get(self.url+"/champion/"+name+"/items/finished/mostPopular?api_key="+self.key)
            else:
                r = requests.get(self.url+"/champion/"+name+"/items/finished/mostWins?api_key="+self.key)
        return r.json()

    def runes(self, name, order="popular"):
        if order == "popular":
            r = requests.get(self.url+"/champion/"+name+"/runes/mostPopular?api_key="+self.key)
        else:
            r = requests.get(self.url+"/champion/"+name+"/runes/mostWins?api_key="+self.key)
        return r.json()

    def matchup(self, name, enemy=""):
        if enemy == "":
            r = requests.get(self.url+"/champion/"+name+"/matchup?api_key="+self.key)
        else:
            r = requests.get(self.url+"/champion/"+name+"/matchup/"+enemy+"?api_key="+self.key)
        return r.json()
