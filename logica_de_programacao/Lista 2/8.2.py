valor = float(input("Digite o valor do carro: "))

pagamento = int(input("Qual a forma de pagamento\n1-À vista\n2-Parcelado\n"))

if pagamento == 1:
    valorA = valor * 0.80
    print(f"Valor à vista: R$ {valorA:.2f}")

elif pagamento == 2:

    parcelas = int(input("Digite a quantidade de parcelas: "))

    match parcelas:
        case 6:
            valor6 = valor * 0.03
            valorF = valor + valor6
            valorX = valorF / 6

        case 12:
            valor12 = valor * 0.06
            valorF = valor + valor12
            valorX = valorF / 12

        case 18:
            valor18 = valor * 0.09
            valorF = valor + valor18
            valorX = valorF / 18

        case 24:
            valor24 = valor * 0.12
            valorF = valor + valor24
            valorX = valorF / 24

        case 30:
            valor30 = valor * 0.15
            valorF = valor + valor30
            valorX = valorF / 30

        case 36:
            valor36 = valor * 0.18
            valorF = valor + valor36
            valorX = valorF / 36

        case 42:
            valor42 = valor * 0.21
            valorF = valor + valor42
            valorX = valorF / 42

        case 48:
            valor48 = valor * 0.24
            valorF = valor + valor48
            valorX = valorF / 48

        case 54:
            valor54 = valor * 0.27
            valorF = valor + valor54
            valorX = valorF / 54

        case 60:
            valor60 = valor * 0.30
            valorF = valor + valor60
            valorX = valorF / 60

        case _:
            print("Quantidade de parcelas inválida!")
            valorF = 0

    if valorF > 0:
        print(f"Valor final: R$ {valorF}")
        print(f"Valor das parcelas: R$ {valorX}")

else:
    print("Forma de pagamento inválida!")
