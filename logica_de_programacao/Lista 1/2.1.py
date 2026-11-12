#2-	Fazer um programa que calcule a tabuada de qualquer número,
#e o limite de cálculo deve ser definido pelo usuário:

num = int(input("Digite o número: "))
tabuada = int(input("Digite até qual número deseja ir na tabuada: "))

for i in range(tabuada):
    print(f"{num} x {i + 1} = {num * (i + 1)}")