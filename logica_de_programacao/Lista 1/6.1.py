#6-	Peça ao usuário para fornecer um número inicial e
#um intervalo. Em seguida, faça uma contagem regressiva
#do número inicial até zero, decrementando pelo intervalo especificado.

num1 = int(input("Digite um número: "))
num = 0

for i in range (num1, num -1, -1):
    print(i)