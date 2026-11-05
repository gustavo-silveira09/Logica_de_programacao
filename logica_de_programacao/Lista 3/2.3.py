homem = 0
mulher = 0

for i in range(56):

    nome = input("Digite o seu nome:")

    sexo = int(input("Selecione o seu sexo:\n1 - Masculino\n2 - Feminino\n"))
    
    if sexo == 1:
        homem += 1
        print(f"{nome} é homem.")

    elif sexo == 2:
        mulher += 1
        print(f"{nome} é mulher.")

print("--- LISTA DE HOMENS E MULHERES ---")
print(f"Homens = {homem}.")
print(f"Mulheres = {mulher}.")

