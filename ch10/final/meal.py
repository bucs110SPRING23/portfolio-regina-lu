import requests

class mealAPI:
    def __init__(self):
        self.url = "www.themealdb.com/api/json/v1/1/random.php"
    
    def get(self):
        r = requests.get(self.url)
        response = r.json()
        if response.get('meals'):
            return response['meals']
        else:
            return None