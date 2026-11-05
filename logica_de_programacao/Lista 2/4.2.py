
pontos2 = 0
pontos1 = 0
rodada = 1

while (pontos1 < 21 and pontos2 < 21) or abs(pontos1 - pontos2) < 2:

    jogador = int(input(f"Rodada {rodada} - Quem fez o ponto? (1 ou 2): "))

    if jogador == 1:
        pontos1 += 1

    elif jogador == 2:
        pontos2 += 1

    else:
        print("Jogador inválido!")
        continue

    print(f"--- Placar atual: J1 [{pontos1}] x [{pontos2}] J2 ---")

    rodada += 1

if pontos1 > pontos2:
    print("O vencedor foi o Jogador 1!""")

else:
    print("O vencedor foi o Jogador 2!")