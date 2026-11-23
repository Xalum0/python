nombre = "Andres"
edad = 24
altura = 1.86

#ejercicios 1
print(nombre)
print(edad)
print(altura, " metros")
print(type(nombre))
print(type(edad))
print(type(altura))

#ejercicios 2
frase = "Python es divertido"

print(frase.lower())
print(len(frase))

busca = "PYTHON"
if busca.lower() in frase.lower():
    print("Si esta")
else:
    print("No esta")

print(frase[::-1])

#ejercicios 3
# es_administrador = False
es_administrador = True

if es_administrador==True:
    print("Acceso de administrador")
else:
    print("Acceso de usuario")

#ejercicios 4
precio = float(input("Precio: "))
cantidad = float(input("Cantidad:"))
importe = precio * cantidad
print("el importe total es: ", importe, "€")

#ejercicios 5
anio_nac=int(input("anio de nacimiento: "))
print("tienes", 2026 - anio_nac, "anios")

