# VL 6th Conditionals Notes

num = int(input("Tell me a whole number: "))

if num < 10:
    print(f"{num} is a single digit number")
elif num < 100:
    print(f"{num} is a two digit number")
elif num == 4:
    print("That is the winning number!")
else:
    print(f"{num} is a big number")

name = input("Please tell me your name: ")

if name == "Ms LaRose":
    print("You are the teacher!")
elif name == "Tia":
    print("You are the TA!")
else:
    print(f"Hello {name}, you are a student!")