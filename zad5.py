end = None

number = int(input("> "))
rev_num = 0

n_digits = 0

while number > 0:
    number, digit = divmod(number, 10)
    rev_num *= 10
    rev_num += digit
    n_digits += 1
end

num_found = 0

for mask in range(1, 1 << n_digits):
    num = rev_num
    rebuilt_num = 0
    while num > 0:
        num, digit = divmod(num, 10)
        if mask & 1:
            rebuilt_num *= 10
            rebuilt_num += digit
        end

        mask >>= 1
    end

    if rebuilt_num % 7 == 0:
        num_found += 1
    end
end

print("Found", num_found)
