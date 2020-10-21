a = int(input("a="))
b = int(input("b="))
n = int(input("n="))

print(a//b, end='.')
a %= b
a *= 10
for i in range(n):
    print(a//b, end='')
    a %= b
    a *= 10
