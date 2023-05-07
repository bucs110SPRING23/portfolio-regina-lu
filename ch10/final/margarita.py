import requests

class margaritaAPI:
    def __init__(self):
        self.url = "https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i=11007"
    
    def get(self):
        r = requests.get(self.url)
        response = r.json()
        if response.get('drinks'):
            return response['drinks']
        else:
            return None