# VL 7th Conditionals Notes

#homework_done = input("Is your homework done: ").strip().capitalize()

#if homework_done == "Yes":
    #print("Yes you can go!")
#else:
    #print("Then go do your homework!")

grade = 110

if grade >= 90:
    if grade > 100:
        print("You cheated that isn't possible!")
    else:
        print(f"You have {grade}% that is an A!")
elif grade >= 80:
    print(f"You have {grade}% that is a B!")
elif grade >= 70:
    print(f"You have {grade}% that is a C!")
else:
    print(f"You have a {grade}% that is a D or lower :(")

#logical operators and, or not

name = input("What is your name: ")

if name == "Ms LaRose":
    print("You are the teacher!")
elif name == "Tia" or name == "Ashley":
    print("You are the TA")
else:
    print(f"Hello {name}, you are a student!")
    if grade >= 70:
        print("And you are passing the class!")