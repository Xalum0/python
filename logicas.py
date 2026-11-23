# logicas.py

# lógica o booleana
# True o False, nada de todo mayuscula o minuscula
autorizado = True    # el otro valor posible True
print( type(autorizado)  )
# == es de copmparar 
if autorizado==True:  # autorizado==True <=> autorizado 
    print("Puede pasar")
    print("segunda instrucción, aqui iría el codigo, , bla")
else:
    print("No puede pasar")
print("tras if")

edad= input("Edad: ")
print(edad, type(edad))
edad= int(edad)
print(edad, type(edad))

# if edad==21:  # autorizado==True <=> autorizado 
#     print("Tiene 21")
# else:
#     print("No tiene 21")
# print("tras if")

if 21<edad and edad<25:  #
    print("Tiene entre 22 y 24")
else:
    print("Tiene otra edad")
print("tras if")

print(edad +1)
print(edad -1)
print(edad *2)
print(edad /2)
print(edad **2)

saldo=100000
edad=16

if (edad>18 or saldo>50000):
    print("Puede apostar")

