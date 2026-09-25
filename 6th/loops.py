# VL, Loops Notes
import random 
# code that will repeat over and over again
count = 1

while count <= 10:
    print(count)
    count += 1


goose = random.randint(1,11)
ducks = 1

while True:
    print("duck")
    if ducks == goose:
        break
    ducks += 1
print("GOOSE!!!!")


siblings = ["Alex", "Katie", "Andrew", "Tia", "Treyson", "Xavier", "Jake"]

print(siblings[2])
print(siblings)
#add to the list
item = input("What needs to be added to the list: ")
siblings.append("Jayshree")
siblings.insert(3,item)
#remove from list
print(siblings)
print(siblings.pop(3))
print(siblings)

# For Loops
for number in range(1,11,2):
    print(number)

for sibling in siblings:
    print(sibling + " LaRose")