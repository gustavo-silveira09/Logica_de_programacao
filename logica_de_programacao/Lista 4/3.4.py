desgaste = 0
i = 0

while desgaste < 500:

    i += 1

    if  i <= 70:
        desgaste += 7


    elif i > 70:
        desgaste += 10

print("Maquina quebrou") 
print(f"Desgaste final: {desgaste}")
print(F"Ciclos: {i}")