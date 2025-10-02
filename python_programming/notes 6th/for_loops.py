# VL 6th Time and For Loops notes!

import datetime

current = datetime.datetime.now()
hour = current.hour

#print(f"The time in seconds since Jan 1, 1970: {epoch}")
print(f"The time is: {current}")
print(f"The hour is: {hour}")

# Lists
siblings = ["Alex", "Katie", "Andrew", "Vienna", "Victoria", "Treyson", "Jefferson", "Jake"]

print(siblings[3])
print(siblings)
siblings[4] = "Tia"
siblings[6] = "Xavier"
siblings.remove("Vienna")

#For loop
for sibling in siblings:
    #print(f"Hello {sibling}")
    print("Hi")

for x in range(20,-11, -1):
    print(x)

#While Loops
#infinite Loops
#while True:
#    print("Oh NO!")


#Good While loop
i = 1

while i < 21:
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
    i += 1

import random

number = random.randint(1,20)
x = 1
"""while x != number:
    print("Duck") 
    x += 1

print("Goose!")"""

while True:
    if number == x:
        print("Goose!")
        break
    else:
        print("Duck")
        x += 1