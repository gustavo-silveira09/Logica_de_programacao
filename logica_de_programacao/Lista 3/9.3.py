media = 0
nota7 = 0
notaT = 0

for in range (35):

    nome = str(input("Digite o seu nome: "))
    notas = float(input("Digite sua nota: "))

    notaT += notas
    if notas > 7:
        nota7 += 1

media = notaT/nome

print(f"Teve {nota7} acima de 7 na turma.")
print(f"A média da turma é {media}")