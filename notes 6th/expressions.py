# VL 6th Expressions Notes! 

# What is an algorithm?
    # answer here
name = input("What is your name? ")
print("Hello", name)

#algorithm for area
length = 5
width = 20
area = length * width 
print(length, "X", width, "=", area)

#1
age_one = 55
age_two = 12
age_three = 6
age_four = 19
#2
total = age_one + age_two + age_three + age_four
average = total/4
#3
print("The average age between:", age_one, "-", age_two, "-", age_three, "-", age_four, "=", average)

#Math equations!
num_one = float(input("Give me a number:\n"))
num_two = int(input("Give me a number:\n"))

num_one += num_two
print("addition (+):", round(num_one, 0)) #1. What needs rounded 2. How many decimals
num_one -= num_two
print("subtraction(-):", num_one)
num_one *= num_two
print("multiplication(*):", num_one)
num_one /= num_two
print("division(/):", round(11/3, 2))
num_one **= num_two
print("exponents(**):", num_one)
num_one //= num_two
print("integer division(//):", num_one)
num_one %= num_two
print("modulo (remainder)(%):", num_one)
print("(3*5**2/15)-(5-2**2)=",(3*5**2/15)-(5-2**2))
