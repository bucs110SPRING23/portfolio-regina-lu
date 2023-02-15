# bool - boolean value
# True/Falso
# - caps are important

# True, 1, "Hello"

print(type(True))   # output: <class 'bool>
print(bool(1), bool(-1), bool("hello"))  # output: True True True
print(bool(0), bool(("")), bool([]))  # output: False False False

# boolean expressions
x = 5
y = 10
print(x == y)  # equality, == boolean equality test, = is assignment
print(x > y)
print(x < y)
print(x >= y)  # => - ERROR!
print(x <= y)  # =< - ERROR!
print(x != y)  # not equal

# and, or, not - semantic operators
# and: and == True, when x and y are both True
print(True and True)  # true
print(True and False)  # false
print(False and True)
print(False and False)

# or - at least one True
print(True or True)  # true
print(True or False)  # true
print(False or True)  # true
print(False or False)  # false

# not - negotiation[!]
print(not True)  # false
print("apple" == "apple")

print("apple" < "Apple Pie")
print(ord("a", ord("A")))

print(1 == 1.0)
print(1 is 1.0)
print(1 is 5 / 5) # false - returns a float
print(1 is 5 // 5) # True - returns an int

# is checks to see if it is the exact same object
print(1 is 1)

mynums = [1, 2, 3, 4, 5, 6, 7]
print(1 in mynums)
print(10 in mynums)

a = int(input("num:"))
if a < 0: # colon
    a = abs(a) #indentation
else: # no condition, always optional
    print("positive")
print(a) # de-indentation to end the if statement

a = int(input("num:"))
if a > 5:
    print("x is greater than 5")
    if a > 10:
        print("x is greater than 10")
    else:
        print("x is greater than 5")
else:
    print("x is less than or equal to 5")

# elif
# always goes between the if and else 
# is optional
# can have as many as you like

# if statements - only one condition will execute

a = int(input("num:"))
if a > 5:
    print("x is greater than 5")
elif a > 10:
    print("x is greater than 10")
else:
    print("x is less than or equal to 5")

a = int(input("num:"))
if a > 10:
    print("x is greater than 10")
elif a > 5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")
# if <condition>: #required
#...# do something
# elif <boolean condition>: #optional
#...# do something
# else: #optional
#...# do something