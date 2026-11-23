# crear una lista y acceder a un valor que no existe
latencias = [1.2, 4.3, 61, 0.3]

try:
    buscar = int(input("latencia a buscar: "))
    print("valor:", latencias[buscar])
except IndexError:
    print("latencia no ubicada")

# crear un diccionario y acceder a una vlave que no existe

servidor= {
    "nombre": "alejandro",
    "ip": "172.100.18.20"
}

try:
    buscar2 = input("clave a buscar: ")
    print(servidor["buscar2"])
except KeyError:
    print("clave no ubicada")