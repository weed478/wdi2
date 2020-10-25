from math import log10

number = int(input("> "))

n_digits = int(log10(number)) + 1

while number > 0:
    number, digit = divmod(number, 10)
    if digit == n_digits:
        print("Tak")
        exit(0)

print("Nie")
