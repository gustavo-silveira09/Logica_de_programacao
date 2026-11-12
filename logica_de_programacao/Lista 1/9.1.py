#9-	Crie um programa de adivinhação em que o computador escolhe
#aleatoriamente um número entre 1 e 50, e o usuário precisa
#adivinhar. O programa deve fornecer feedback (maior ou menor)
#a cada tentativa e permitir apenas 5 tentativas para acertar.
#Se o usuário acertar antes do limite, exiba uma mensagem de
#vitória caso contrário, revele o número ao final.

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