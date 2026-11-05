meta = 0
maq = 0
peca = 1
producaoT = 0
contciclos = 0
estacaoquebrada = 0

meta = int(input("Digite qual a meta diaria: "))

for i in range (1, 6): 
    if producaoT >= meta:
        break

    maq = int(input(f"Digite a quantidade maxima suportada pela maquina da estação {i}: "))

    contciclosacima = 0
 
    peca = int(input("Digite a quantidade recebida: "))

    while producaoT < meta:
        contciclos += 1

        processadas = min(peca, maq)

        if processadas > maq * 0.9:
            contciclosacima += 1
        else:
            contciclosacima = 0

        if contciclosacima == 5:
            print(f"A estação {i} quebrou")
            estacaoquebrada = i
            break

        producaoT += processadas
        peca -= processadas

        if producaoT >= meta:
            break

        if peca == 0:
            peca = int(input("Quantidade de peças novas recebidas: "))

    if estacaoquebrada != 0:
        break

print(f"Produção Total: {producaoT}")
print(f"Ciclos executados: {contciclos}")

if estacaoquebrada != 0:
    print(f"A maquina {estacaoquebrada} quebrou")
else:
    print("Nenhuma máquina falhou")

    
        
meta = 0
maq = 0
peca = 0
producaoT = 0
contciclos = 0
estacaoquebrada = 0

meta = int(input("Digite qual a meta diaria: "))

for i in range(1, 6): 
    if producaoT >= meta:
        break

    print(f"\n--- ESTAÇÃO {i} ---")
    maq = int(input(f"Digite a quantidade maxima suportada pela maquina da estação {i}: "))

    contciclosacima = 0
 
    peca = int(input("Digite a quantidade recebida: "))

    while producaoT < meta:
        
        if peca == 0:
            peca = int(input("Quantidade de peças novas recebidas (ou 0 para mudar de estação): "))
            
            if peca == 0:
                break

        contciclos += 1

        processadas = min(peca, maq)

        
        if processadas > maq * 0.9:
            contciclosacima += 1
        else:
            contciclosacima = 0

        if contciclosacima == 5:
            print(f"A estação {i} quebrou")
            estacaoquebrada = i
            break

        producaoT += processadas
        peca -= processadas

    if estacaoquebrada != 0:
        break

print(f"Produção Total: {producaoT}")
print(f"Ciclos executados: {contciclos}")

if estacaoquebrada != 0:
    print(f"A maquina {estacaoquebrada} quebrou")
else:
    print("Nenhuma máquina falhou")