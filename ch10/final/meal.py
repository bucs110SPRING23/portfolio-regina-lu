import requests

class mealAPI:
    def __init__(self):
        self.url = "https://www.themealdb.com/api/json/v1/1/random.php?"
    
    def get(self):
        r = requests.get(self.url)
        response = r.json()
        if response.get('meals'):
            return response['meals']
        else:
            return None
    
    def change_meal(self):
        number = int(input('Choose a number between 52780 and 53050: '))
        if 52780 <= number <= 53050:
            number = str(number)
            self.url = f'https://themealdb.com/api/json/v1/1/lookup.php?i={number}'
        else:
            self.url = "https://www.themealdb.com/api/json/v1/1/random.php?"