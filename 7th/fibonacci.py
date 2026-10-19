while True:
    try:
        number_count = int(input("How many Fibonacci numbers would you like to see? "))
    except ValueError:
        print("Please type a whole number.")
        continue

    if number_count < 1 or number_count > 20:
        print("Please stay in the range of 1 to 20.")
        continue

    break

fibonacci_numbers = []
first_number = 0
second_number = 1

for _ in range(number_count):
    fibonacci_numbers.append(first_number)
    first_number, second_number = second_number, first_number + second_number

print(*fibonacci_numbers)
