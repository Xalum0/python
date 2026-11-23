# variables.py
login = "acoltro308"
password = "12354"
peso = 96.2
jubilado = False

print("tipo de login", type(login), "\n", login) 
print("tipo de peso", type(peso), peso)

res = type(jubilado)

print(res)

if peso > 100:
    print("sobrepeso")
else:
    print("saludable")

print ("Después del if")    

if peso < 40:
    print("desnutricion")
else:
    if peso > 100:
        print("sobrepeso")
    else:
        print("saludable")
        
