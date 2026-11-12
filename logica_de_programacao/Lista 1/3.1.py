#3-	Fazer um programa que retorne quantos valores 
#digitados pelo usuário são negativos. Repetir o enquanto 
#até o usuário digitar o valor ZERO:

neg = 0
posi = 0

num = int(input("Digite um número inteiro para iniciar e 0 para encerrar: "))

while num != 0:
    if num < 0:
        neg = neg + 1
    elif num > 0:
        posi = posi + 1

    num = int(input("Digite 0 para encerrar ou outro número para continuar: "))

print(f"Você digitou {posi} número(s) positivos e {neg} número(s) negativos")