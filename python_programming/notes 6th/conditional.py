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
    if num == 4:
        print("That is my favorite number!")
elif name == "Tia" or name == "Andrew":
    print("You are the TA!")
else:
    if name == "Lucas":
        print("You are in 6th period!")
    print(f"Hello {name}, you are a student!")


# AND OR NOT

if num >=0 and num < 10: #and means both must be true
    print(f"{num} is a single digit number")
elif num < 25 or num == 50: #or means only 1 must be true
    print(f"Wow {num} is a realy cool number!")
elif not num < 100: #not checks if the opposit is true
    print(f"{num} is a large number")
else:
    print(f"You typed in a {num}")