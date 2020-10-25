def is_palindrome_for_base(number, base):
    a = number
    b = 0
    while a > 0:
        a, rem = divmod(a, base)
        b *= base
        b += rem

    return b == number

number = int(input("> "))

print("Jej" if is_palindrome_for_base(number, 10) else "Jednak nie")
print("Jej" if is_palindrome_for_base(number, 2) else "Jednak nie")
