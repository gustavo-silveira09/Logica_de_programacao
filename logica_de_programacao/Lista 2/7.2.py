canal4 = 0
canal5 = 0
canal7 = 0
canal12 = 0
pessoas = 0
canal = 1

while canal != 0:
    canal = int(input("Digite qual o canal que está assistindo: "))

    if canal == 4:
        pessoas = int(input("Digite quantas pessoas estão assistindo: "))
        canal4 += pessoas

    elif canal == 5:
        pessoas = int(input("Digite quantas pessoas estão assistindo: "))
        canal5 += pessoas

    elif canal == 7:
        pessoas = int(input("Digite quantas pessoas estão assistindo: "))
        canal7 += pessoas

    elif canal == 12:
        pessoas = int(input("Digite quantas pessoas estão assistindo: "))
        canal12 += pessoas

somaTotal = canal4 + canal5 + canal7 + canal12

if somaTotal > 0:
    media4 = (canal4 / somaTotal) * 100
    media5 = (canal5 / somaTotal) * 100
    media7 = (canal7 / somaTotal) * 100
    media12 = (canal12 / somaTotal) * 100

    print(f"A audiência do canal 4 é: {media4}%")
    print(f"A audiência do canal 5 é: {media5}%")
    print(f"A audiência do canal 7 é: {media7}%")
    print(f"A audiência do canal 12 é: {media12}%")

else:
    print("Nenhuma pessoa foi registrada.")