import random

x = random.randint(1, 11)

for tries in range(0,3):
    num = int(input("Guess a number between 1 and 10 "))
    if num < x:
        print("Too Low")
    if num > x:
        print("Too High")
    if num == x:
        print("correct!")
        break