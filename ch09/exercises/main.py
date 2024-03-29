# Network Programming

# Build a program that asks trivia questions

# Server: any computer listening for incoming network connections

# Request: an incoming connection that asks for some resource from the server
# - images, video, music
# - text
# - JSON
# - HTML

# Types of Requests
# - GET - read
# -- visiting, downloading a file, etc
# - PUT - write operation (requires security)
# -- login, deleting

# Headers
# sent with request and the response
# - status codes
# -- 200: ok, everything went fine
# -- 400: resource cannot be delivered
# -- 500: bad code server
# - ip address
# - system information (geolocation)

## urllib

# Requests

# API - Application Programmer's Interface
# APIS can return data in any format, usually returns in JSON

# - ?, &
# binghamton.edu/cs?var1=100

import requests
import random

class TriviaProxyAPI:
    def __init__(self):
        self.url = "https://opentdb.com/api.php?"
        self.varstr = "amount=1&category=18"
    
    def get(self):
        url = self.url + self.varstr
        response = requests.get(url)
        data = response.json()
        return data ['results']
    
    # def csquestions(self):
    #     self.varstr = "amount=1&category=18"
    #     return self.get()
    # def general(self):
    #     self.varstr = "amount=2"
    #     return self.get()

def main():
    tp = TriviaProxyAPI()
    results = tp.get()

    for r in results:
        print(r['question'])
        # possibilities = [r["correct_answer"], *r["incorrect_answer"]]
        possibles = [r["correct_answer"]] + r["incorrect_answers"]
        random.shuffle(possibles)
        print("Make your selection.")
        for i, p in enumerate(possibles):
            print(rf"{i}) {p}")
        
        selection = int(input(": "))
        if possibles[selection] == r["correct_answer"]:
            print("You are correct")
        else:
            print(f"You need to study more. The correct answer is: {r['correct_answer']}")

main()