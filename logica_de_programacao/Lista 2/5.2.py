a = 90000000
b = 140000000
i = 0

while a < b:
    a += (a * 0.035)
    b += (b * 0.01)
    i += 1

print(f"Foram necessarios {i} anos para País A ser maior que País B")