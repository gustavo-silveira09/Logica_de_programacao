#10-	Solicite ao usuário um número inteiro n e exiba uma
#estrutura em forma de triângulo numérico de tamanho n.
#Cada linha do triângulo deve conter números de 1 até o número
#da linha. Exemplo para 
#n = 5:

#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5

n = int(input("Digite a quantidade de linha que você quer que o triângulo tenha: "))

for contador in range(1, n +1):

    for numero in range(1, contador +1):

        print(numero, end=" ")
    print()