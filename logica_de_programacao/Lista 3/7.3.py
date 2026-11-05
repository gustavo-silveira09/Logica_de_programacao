



divida= float(input("Digite o valor da dívida: "))

print("\nValor da Dívida | Valor dos Juros | Qtd de Parcelas | Valor da Parcela")

for parcelas in [1, 3, 6, 9, 12]:
    
    if parcelas == 1:
        juros = 0
    elif parcelas == 3:
        juros = 10
    elif parcelas == 6:
        juros = 15
    elif parcelas == 9:
        juros = 20
    elif parcelas == 12:
        juros = 25

   
    valorJ = divida * (juros / 100)
    dividaT = divida + valorJ
    valorP = divida / parcelas

    
    print(f"R$ {dividaT:.2f} | R$ {valorJ:.2f} | {parcelas} | R$ {valorP:.2f}")