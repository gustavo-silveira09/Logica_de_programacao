vTotal = 0
setor1 = 0
setor2 = 0
somaS1 = 0
somaS2 = 0
somaS = 0
salario = 0
mediaS2 = 0
mediaS1 = 0
for in range (15):

    setor = int(input("Digite o código do setor:\n 1 - Administrativo\n2 - Operacional\n"))
    salario = float(input("Digite o seu salário: ")) 
        
    if setor == 1:
        setor1 += 1
        somaS1 += salario
        
    elif setor ==2:
        setor2 += 1
        somaS2 += salario

mediaS1 = somaS1/setor1
mediaS2 = somaS2/setor2
somaS = somaS1 + somaS2

print(f"Média salarial do setor Administrativo: R$ {mediaS1:.2f}")
print(f"Média salarial do setor Operacional: R$ {mediaS2:.2f}")
print(f"Total de salários pagos pela empresa: R$ {somaS:.2f}")
print(f"Quantidade de funcionários no Administrativo: {setor1}")
print(f"Quantidade de funcionários no Operacional: {setor2}")
