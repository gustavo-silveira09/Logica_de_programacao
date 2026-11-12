#7-	Crie um programa que solicite números ao usuário continuamente
#até que ele insira um número negativo. Em seguida, exiba
#a média dos números positivos fornecidos.

i = 0
somaPos = 0
media = 0

while True:
    num = float(input("Digite outro número para continuar ou digite um número negativo para encerrar: "))
    if num < 0:
        break
    somaPos += num
    i += 1
    if i > 0:
        media = somaPos/i
        
    else:
        print("Nenhum número positivo foi digitado.")
        
print(f"A média dos números pares é {media}")