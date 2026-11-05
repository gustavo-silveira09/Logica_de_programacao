i = 0

for y in range (80):

    num = int(input("Digite um número: "))

    if num >= 10 and num <= 150:
        i+=1
        
print(f"{i}, quantidades de números entre 10 e 150")