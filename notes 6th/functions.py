# VL 6th Functions Notes

import random

def welcome():
    name = input("What is your name\n")
    print(f"Hello {name}!")

print(f"The function is over!")

#welcome() Fucntion Call



def add(number, number_two): #Parameters given when we define the function
    number = number + number_two
    print(number)

num_one = 12
num_two = 14
#add(num_one, num_two) #Arguments are given when we call the function
#add(4, 8)
#add(9, 700)
#add(87, 45)

def clean(info):
    return info.strip().lower()

name = input("What is your name?")
quest = input("What is your quest?")
color = input("What is your favorite color?")

print(f"Hello, {clean(name)}. I have heard you are trying to {clean(quest)}, that is super cool! Are you sure {clean(color)} is your favorite color?")

def believe(sentence):
    length = len(sentence)
    spot_one = random.randint(0, length -1)
    spot_two = random.randint(0, length -1)
    spot_three = random.randint(0, length -1)
    full_sentence = sentence.split(" ")
    full_sentence.insert(spot_one, "Beleive it!")
    full_sentence.insert(spot_two, "Beleive it!")
    full_sentence.insert(spot_three, "Beleive it!")
    sentence = " ".join(full_sentence)
    return sentence


new_sentnece = believe("The quick brown fox jumps over the lazy dog!")
print(new_sentnece)
print(believe("Peter Piper picked a peck of pickled peppers!"))
