import random

x = random.randint(1, 1001)
answer = 0
num = int(input("Guess a number between 1 and 1000 "))

while x != num:
    if num < x:
        print("Too Low")
        answer = answer + 1
        num = int(input("Guess a number between 1 and 1000 "))
    if num > x:
        print("Too High")
        answer = answer + 1
        num = int(input("Guess a number between 1 and 1000 "))

print("correct!, the answer is ", x)
print("It look you ", answer, " tries")