contador = 0
nomeCliente = 0

while contador < 150:

    contador += 1

    valorCompras = int(input("Insira o valor das compras do cliente: "))
    nome = str(input("Insira o nome do cliente: "))

    if valorCompras < 500000:
        print(f"{nome}, parabéns! Você acabou de receber um bônus de 10%")

    else:
        print(f"{nome}, parabéns! Você acabou de receber um bônus de 15%")