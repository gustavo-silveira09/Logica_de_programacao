vestu = 0
naoPere = 0
pere = 0
higiene = 0
limpeza = 0
prod = 1
while prod != 0:

    prod = int(input("Digite o codigo do produto:"))

    if prod == 1:
        naoPere += 1

    elif prod >= 2 and prod <= 4:
        pere += 1
       
    elif prod > 4 and prod < 7:
        vestu += 1

    elif prod == 7:
        higiene += 1
        
    elif prod > 7 and prod < 16:
        limpeza += 1
        
    else:
        print ("Código inválido")

print("\n --- PRODUTOS CADASTRADOS ---\n")
print(f"Alimento não-perecível = {naoPere}\n")
print(f"Alimento perecível = {pere}\n")
print(f"Vestuário = {vestu}\n")
print(f"Higiene pessoal = {higiene}\n")
print(f"Limpeza e utensílios domésticos = {limpeza}\n")