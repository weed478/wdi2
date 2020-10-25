number = int(input("> "))

a = 1
b = 1

mul = 1
while a <= number:
    mul *= a
    if mul % number == 0:
        print("git majonez")
        exit(0)

    a, b = b, a + b

print("Nie działa")

