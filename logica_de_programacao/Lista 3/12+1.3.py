temp = 0
totalD = 0
maiorT = 0
percentual = 0
cont = 0

while temp != 999:
    temp = float(input("Digite a temperatura: "))
    
    if temp == 999:
        break
        
    totalD += 1
    
    if temp < -50 or temp > 150:
        continue
        
    if (temp >= 20 and temp <= 80) and (temp % 5 == 0) and (temp % 10 != 0):
        cont += 1
          
        if temp > maiorT:
            maiorT = temp

print("Quantidade válida:", cont)

if cont > 0:
    print("Maior temperatura válida:", maiorT)
    percentual = (cont / totalD) * 100
    print(f"Percentual válido: {percentual:.1f}%")
else:
    print("Nenhuma temperatura válida foi digitada.")