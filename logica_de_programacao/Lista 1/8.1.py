num = 0
par = 0

num = int(input("Digite um número inteiro e positivo: "))

if num % 2 == 0:
    for i in range (num, 0, -2):
        print(i)
else: 
    for i in range (num, -1,0,-2):
        print(i)