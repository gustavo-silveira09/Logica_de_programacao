totalP = 0
totalA = 0
total = 0

for i in range (15):

    codigo = int(input("Selecione a forma de pagamento:\n 1 - Avista\n 2 - Parcelado"))
    valor = float(input("Digite o valor da sua compra:"))
    
    if codigo == 1:
    totalA += valor
    total += valor 

    elif codigo == 2:
    totalP += valor
    total += valor 
    print(f"O valor da parcela é {valor/3}")

print(f"O total de todas as transações é {total}")
print(f"O total das transacoes à vista é {totalA}") 
print(f"O total das transacoes a prazo é {totalP}") 
        