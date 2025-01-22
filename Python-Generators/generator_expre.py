num = (n**2 for n in range(1, 11))

print(list(num))

for n in (n**2 for n in range(1, 11)):
    print(n)
