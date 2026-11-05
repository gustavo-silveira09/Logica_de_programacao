posi = 0
nega = 0
par = "0" 
impar = "0"
num = 1
somaP = 0
somaN = 0
somaParcial = 0

while num != 0:

    num = int(input("Digite números: \n "))
        
    if num > 0:
        somaP = somaP + num

    else:
        somaN = somaN + num

    if num % 2 == 0 and num != 0:
        par += str(num) + " "

    elif num != 0: 
        impar += str(num) + " "

somaParcial = somaP + somaN 

print(f"Números positivos = {somaP}")
print(f"Números negativos = {somaN}")
print(f"Números Pares = {par}")
print(f"Números impar = {impar}")
print(f"Soma parcial = {somaParcial}")

