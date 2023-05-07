import requests
from random import choice, randrange

class numbersAPI:
    def __init__(self):
        self.url = "http://numbersapi.com/#40"
        number = input("Enter a number: ")
        if number.isdigit():
            self.varstr = number
        else:
            number = randrange(1, 100)
            self.varstr = number
        #self.url = f'http://numbersapi.com/{number}'
#         type = ["trivia", "math", "date", "year"]
        self.url = self.url + str(self.varstr)

    def get(self):
        r = requests.get(self.url)
        response = r.json()
        if response.get('text'):
            return response['text']
        else:
            return None
    
    # def change_type(self):
    #     pass