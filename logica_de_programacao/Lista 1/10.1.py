n = int(input("Digite a quantidade de linha que você quer que o triângulo tenha: "))

for contador in range(1, n +1):

    for numero in range(1, contador +1):

        print(numero, end=" ")
    print()