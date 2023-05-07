import requests

class uselessfactsAPI:
    def __init__(self):
        self.url = "https://uselessfacts.jsph.pl/api/v2/facts/today"
    
    def get(self):
        r = requests.get(self.url)
        response = r.json()
        if response.get('text'):
            return response['text']
        else:
            return None
