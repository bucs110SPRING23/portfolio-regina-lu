# For Loop - repeat a sequential algorithm on sequential data

msg = "Enter 3 numbers"
mynums = []

for i in [0,0,0]:
    var = int(input(":"))
    mynums.append(var)
    print(mynums)
print("all done")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
for c in colors:
    print(c)
    c = "black"  # this gets overwritten (the c is only a temporary variable)
    print(c)

# Block Statement
# - always ends with a colon
# - everything that is part of the block is indented

for ch in "hello":
    print(ch)

# 2 ways of using a for loop
mylist = [1, 2, 3, 4, 5]
for i in mylist:
    print(i + i)

mylist = [0]*5
for _ in mylist:
    print('Happy Birthday')

## range()
# 'range(5)' = [0, 1, 2, 3, 4]

# range generates list values dynamically
'[0]*100' # generates a list of 100 0's and stores it in memory
'range(100)' # generates items from a list of 100 as needed

result = range(5) # starts at 0 (default), stops at 5 (non-inclusive)
print(list(result))
result = range(1, 5) # starts at 1 (inclusive), stops at 5 (non-inclusive)
print(list(result))

print(list(range(11)))
print(list(range(3, 11, 2)))
print(list(range(100, -1, -1)))

# range(stop)
# range(start, stop)
# range(start, stop, step)

colors = ['red', 'purple', 'yellow']
for color in colors:
    donatello.color(color)
    for _ in range(4):
        donatello.left(90)
        donatello.forward(50)
    donatello.up()
    donatello.forward(100)
    donatello.down()
wn.exitonclick