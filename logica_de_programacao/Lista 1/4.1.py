soma_salarios = 0
soma_filhos = 0
maior_salario = 0
quantidade_pessoas = 0
salario_ate_100 = 0


salario = float(input("Digite o salário: "))


while salario >= 0:


    filhos = int(input("Digite o número de filhos: "))


    soma_salarios += salario
    soma_filhos += filhos
    quantidade_pessoas += 1


    if salario > maior_salario:
        maior_salario = salario


    if salario <= 100:
        salario_ate_100 += 1


    salario = float(input("Digite o salário: "))


if quantidade_pessoas > 0:
    media_salario = soma_salarios / quantidade_pessoas
    media_filhos = soma_filhos / quantidade_pessoas
    percentual = (salario_ate_100 / quantidade_pessoas) * 100


    print(f"Média do salário: R$ {media_salario:.2f}")
    print(f"Média de filhos: {media_filhos:.2f}")
    print(f"Maior salário: R$ {maior_salario:.2f}")
    print(f"Percentual com salário até R$100,00: {percentual:.2f}%")
else:
    print("Nenhum dado foi informado.")