# VL 6th Strings Notes

#Examples of strings
first_name = input("What is your first name:\n").strip().title()

last_name = input("What is your last name:\n").strip().title()

full_name = first_name + " " + last_name

sentence = "The quick brown fox jumps over the lazy dog."

print("Welcome to my program", full_name + "!")
print(sentence.find("brown"))
print(sentence[10:15])

# Debugging is fixing problems in my code!
    # Syntax Error
string = 'This is my string'
    # Logic Error
numOne = "1"
numTwo = "3"
print(numOne + numTwo)
    # Run-Time Error 

letter = "a"
#int(letter)