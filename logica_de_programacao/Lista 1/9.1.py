import random
numero = random.randint(1,50)
for contador in range (5):
    num = int(input("Digite um número: "))
    if num == numero:
        print("Acertou")
        errou = 0
        break
    if num < numero: 
        print("Tente novamente, o número é maior")
    if num > numero: 
        print("Tente novamente, o número é menor")
if (errou == 1):
    print("O número sorteado foi: ", numero)