excelente = 0
bom = 0
regular = 0
mediaIdade = 0
percenBom = 0
idade = 0
opniao = 0
somaTotal = 0
idadeTotimo = 0
pessimo = 0

for i in range (40):

    idade=int(input("Digite sua idade:"))
    opniao=int(input("O que voce achou do filme:\n 1 - Pessimo \n2 - Regular\n3 - Bom\n 4 - Excelente"))
        
    if opniao == 1:
        pessimo += 1

    elif opniao == 2:
        regular += 1
        
    elif opniao == 3:
        bom += 1

    elif opniao == 4:
        excelente += 1
        idadeTE += idade

    somaTotal += 1
print(f"A média das idades das pessoas que votaram em excelente é {idadeTE/excelente}")
print(f"A quantidade de pessoas que responderam regular é {pessimo}")
print(f"A porcentagem é {(bom/somaTotal) * 100}")