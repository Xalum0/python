#Ejercicio 1
servidor = {
    "nombre": "web",
    "ip": "10.10.10.10",
    "puerto": 80
    "activo": True
}
print (servidor["nombre"])
print (servidor["ip"])
if servidor["activo"]:
    print("esta activo")
else:
    print("no esta activo")

#Ejercicio 2
usuario = {
    "nombre": "Ana",
    "edad": 21,
    "activo": True
}
print("Nombre del usuario", usuario["nombre"])
print("Edad del usuario", usuario["edad"])
print(usuario["activo"])

#Ejercicio 3
usuario["edad"] = 22
usuario["email"] = "ana@correo.com"
print("usuario")

#Ejercicio 4
equipo = {
    "hostname": "server01",
    "ip": "192.168.1.10",
    "so": "Linux"
}
clave1= input("introduce clave a buscar: ")
if clave1 in servidor:
    print(servidor[clave1])
else
    print(f"clave {clave1} no existe")

#Ejercicio 5
puertos = {
    "ssh": 22,
    "http": 80,
    "https": 443
}

for clave, valor in puertos.items():
    print(" - ", clave, "=>", valor)

#Ejercicios 6
persona = {
    "nombre": "Luis",
    "ciudad": "Cádiz"
}
print(persona.get("nombre"))
print(persona.get("telefono","No disponible"))

