i = 0
somaPar = 0
media = 0

num = int(input("Digite um número ou 0 para encerrar: "))

while num != 0:
    if num % 2 == 0:
        somaPar = somaPar + num
        i += 1
    num = int (input("Digite outro número ou digite 0 para encerrar: "))

if i > 0: 
    media = somaPar / i
    print(f"A média dos números pares é {media}")

else: 
    print("Nenhum número par foi digitado")