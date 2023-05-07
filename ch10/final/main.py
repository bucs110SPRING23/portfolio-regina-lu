import requests
import numbers, uselessfacts

def main():
   number = numbers.numbersAPI()
   quote1 = number.get()
   todayfact = uselessfacts.uselessfactsAPI()
   quote2 = todayfact.get()

   for quote in quote1:
      num_quote = quote['random_number']
   for otherquote in quote2:
      today_quote = otherquote['today']
   
   print(num_quote + today_quote) 

main()