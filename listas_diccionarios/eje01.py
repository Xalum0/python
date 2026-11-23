servidor = {
    "nombre": "web01",
    "ip": "192.168.1.20",
    "servicios": ["ssh", "http", "https"]
}

print("nombre:", servidor["nombre"])
print("ip:", servidor["ip"])
print("servicios:", servidor["servicios"])

for x in servidor["servicios"]:
    print("-", x)

print("primer servicio:", servidor["servicios"][0])

servidor["servicios"].append("DNS")
print(servidor["servicios"])