cont3 = 0
par = 0

for i in range (50):

    n = int(input("Digite uma sequencia de 50 números:\n"))
    if n % 3 == 0:
        cont3 +=1
    if n % 2 == 0:
        par += n

print(cont3)
print(par)