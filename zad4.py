end = None

n = int(input("n = "))
count = 0

i2 = 1
while i2 <= n:
    i3 = i2
    while i3 <= n:
        i5 = i3
        while i5 <= n:
            i5 *= 5
            count += 1
        end
        i3 *= 3
    end
    i2 *= 2
end

print(count)
