a = int(input("Qual a população do país A? "))
b = int(input("Qual a população do país B? "))
i = 0

while a < b:

    b = b * 1.015
    a = a * 1.03
    i += 1

    if i % 5 == 0 and i != 0:
        a = a * 0.93
        b = b * 0.93

print(f"Em {i} anos o A será maior que o B")