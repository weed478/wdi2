number = int(input("> "))

number, last_digit = divmod(number, 10)
while number > 0:
    number, digit = divmod(number, 10)
    if digit >= last_digit:
        print("Nie działa")
        exit(0)

    last_digit = digit

print("Działa")

