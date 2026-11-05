
otimo = 0
bom = 0
regular = 0
mediaIdade = 0
percenBom = 0
idade = 0
opniao = 0
somaTotal = 0
idadeTotimo = 0

for i in range (15):

    idade=int(input("Qual a sua idade?:"))
    opniao=int(input("O que voce achou do filme:\n 1 - Regular\n2 - Bom\n 3 - Ótimo"))
        
        if opniao == 1
            regular += 1
        
        elif opniao == 2
            bom += 1

        elif opniao == 3
            otimo += 1
            idadeTotimo += idade

    somaTotal += 1
print(f"A média das idades das pessoas que votaram em ótimo é {idadeTotimo/otimo}")
print(f"A quantidade de pessoas que responderam regular é {regular}")
print(f"A porcentagem é {(bom/somaTotal) * 100}")