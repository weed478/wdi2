number = int(input("> "))

a = number
b = 0
while a > 0:
    a, rem = divmod(a, 10)
    b *= 10
    b += rem

print("Jej" if b == number else "Jednak nie")

a = number
b = 0
while a > 0:
    a, rem = divmod(a, 2)
    b *= 2
    b += rem

print("Jej" if b == number else "Jednak nie")
