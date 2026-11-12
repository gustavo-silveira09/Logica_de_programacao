#8-	Peça ao usuário um número inteiro positivo e
#exiba todos os números pares de forma decrescente até
#chegar a zero. O programa deve exibir a sequência
#de forma organizada, considerando que o número de entrada
#pode ser par ou ímpar.

num = 0
par = 0

num = int(input("Digite um número inteiro e positivo: "))

if num % 2 == 0:
    for i in range (num, 0, -2):
        print(i)
else: 
    for i in range (num, -1,0,-2):
        print(i)