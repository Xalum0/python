from servidores import SERVIDORES, LISTAUNO;

#Ej01
def mostrar_inventario(lista):
    """Muestra la información básica de los servidores recibidos."""
    print(f"{'ID':<5} {'NOMBRE':<13} {'ROL':<16} {'ESTADO':<12} {'CPU':<5} {'RAM':<5}")
    print("-"*70)
    for servidor in lista:
       print(f"{servidor["id"]:<5} {servidor["nombre"]:<13} {servidor["rol"]:<16} {servidor["estado"]:<12} {servidor["cpu"]:<5} {servidor["ram"]:<5}") 

#Ej02
def buscar_por_id(servidor, iden):
    """Devuelve el diccionario correspondiente o None si no existe."""
    for servidor in SERVIDORES:
        if iden == servidor["id"]:
            return servidor
    return None

#Ej03
def filtrar_por_estado(servidores, estado):
    """Devuelve una lista con los servidores del estado indicado."""
    lista = []

    for servidor in SERVIDORES:
        if servidor["estado"] == estado:
            lista.append(servidor)

    return lista

def filtrar_por_rol(servidores, rol):
    """Devuelve una lista con los servidores del rol indicado."""
    lista = []

    for servidor in SERVIDORES:
        if servidor["rol"] == rol:
            lista.append(servidor)

    return lista


#EJ04
def calcular_resumen(servidores):
    """Devuelve un diccionario con las estadísticas globales."""
    total = len(servidores)

    encendidos = filtrar_por_estado(servidores, "encendido")
    num_encendidos = len(encendidos)
    num_apagados = total - num_encendidos

    if total == 0:
        disponibilidad = 0.0
    else:
        disponibilidad = num_encendidos / total * 100

    resumen = {
        "total": total,
        "encendidos": num_encendidos,
        "apagados": num_apagados,
        "disponibilidad": disponibilidad
    }
    return resumen

def mostrar_resumen(servidores):
    """Presenta las estadísticas de forma legible."""    
    resumen = calcular_resumen(servidores)
    print("Total:", resumen["total"])
    print("Encendidos:", resumen["encendidos"])
    print("Apagados:", resumen["apagados"])
    print("Disponibilidad: %.2f%%" % resumen["disponibilidad"])

#EJ05
def calcular_resumen(servidores):
    """Devuelve un diccionario con las estadísticas globales."""
    total = len(servidores)

    encendidos = filtrar_por_estado(servidores, "encendido")
    num_encendidos = len(encendidos)
    num_apagados = total - num_encendidos

    if total == 0:
        disponibilidad = 0.0
    else:
        disponibilidad = num_encendidos / total * 100

    if num_encendidos == 0:
        cpu_media = 0.0
        ram_media = 0.0
    else:
        suma_cpu = 0
        suma_ram = 0 
        for servidor in encendidos:
            suma_cpu = suma_cpu + servidor["cpu"]
            suma_ram = suma_ram + servidor["ram"]
        cpu_media = suma_cpu / num_encendidos
        ram_media = suma_ram / num_encendidos

    resumen = {
        "total": total,
        "encendidos": num_encendidos,
        "apagados": num_apagados,
        "disponibilidad": disponibilidad,
        "cpu_media": cpu_media,
        "ram_media": ram_media
    }
    return resumen

def mostrar_resumen(servidores):
    """Presenta las estadísticas de forma legible."""
    resumen = calcular_resumen(servidores)
    print("Total:", resumen["total"])
    print("Encendidos:", resumen["encendidos"])
    print("Apagados:", resumen["apagados"])
    print("Disponibilidad: %.2f%%" % resumen["disponibilidad"])
    print("CPU media (encendidos): %.2f%%" % resumen["cpu_media"])
    print("RAM media (encendidos): %.2f%%" % resumen["ram_media"])

#EJ06
def mostrar_servicios(servidor):
    """Muestra los servicios y su estado en un servidor."""
    if servidor is None:
        print("No existe un servidor con ese ID.")
        return

    print("Servicios de", servidor["nombre"], ":")
    for nombre, estado in servidor["servicios"].items():
        print("-", nombre, ":", estado)

def mostrar_servicios_empresa(servidores):
    """Muestra los servicios y su estado de todos los servidores."""
    for servidor in servidores:
        mostrar_servicios(servidor)
        print()

def contar_servicios_inactivos(servidores):
    """Cuenta servicios inactivos en servidores encendidos. y lo devuelve como resultado"""

    contador = 0
    for servidor in servidores:
        if servidor["estado"] == "encendido":
            for estado in servidor["servicios"].values():
                if estado == "inactivo":
                    contador = contador + 1
    return contador

#EJ07
def cambiar_estado(servidores, identificador, nuevo_estado):
    """Simula un cambio entre 'encendido' y 'apagado'."""
    if nuevo_estado != "encendido" and nuevo_estado != "apagado":
        raise ValueError("Estado de servidor no válido.")

    servidor = buscar_por_id(servidores, identificador)
    if servidor == None:
        raise ValueError("No existe un servidor con ese ID.") 

    servidor["estado"] = nuevo_estado

def cambiar_servicio(servidores, identificador, nombre_servicio, nuevo_estado):
    """Simula un cambio entre 'activo' e 'inactivo'."""
    if nuevo_estado != "activo" and nuevo_estado != "inactivo":
        raise ValueError("Estado de servicio no válido.")

    servidor = buscar_por_id(servidores, identificador)
    if servidor is None:
        raise ValueError("No existe un servidor con ese ID.")

    if servidor["estado"] == "apagado":
        raise ValueError("El servidor está apagado.")

    if nombre_servicio not in servidor["servicios"]:
        raise ValueError("Ese servicio no existe en el servidor.")

    servidor["servicios"][nombre_servicio] = nuevo_estado

#EJ08
def mostrar_menu():
    print()
    print("=== CONSOLA DE INVENTARIO LINUX ===")
    print("1. Ver inventario")
    print("2. Buscar servidor por ID")
    print("3. Filtrar por rol")
    print("4. Resumen de la infraestructura")
    print("5. Ver servicios de un servidor")
    print("6. Cambiar estado de un servidor")
    print("7. Cambiar estado de un servicio")
    print("0. Salir")

def menu(servidores):
    opcion = 9

    while opcion != 0:
        mostrar_menu()
        opcion = int(input("Elige una opción: "))

        if opcion == 1:

            mostrar_inventario(servidores)
        elif opcion == 2:

            try:
                identificador = int(input("ID del servidor: "))
                servidor = buscar_por_id(servidores, identificador)
                if servidor is None:
                    print("No existe un servidor con ese ID.")
                else:
                    mostrar_inventario([servidor])
            except ValueError:
                print("El ID tiene que ser un número.")
        elif opcion == 3:
        
            rol = input("Rol: ")
            mostrar_inventario(filtrar_por_rol(servidores, rol))
        elif opcion == 4:
        
            mostrar_resumen(servidores)
        elif opcion == 5:
        
            try:
                identificador = int(input("ID del servidor: "))
                servidor = buscar_por_id(servidores, identificador)
                mostrar_servicios(servidor)
            except ValueError:
                print("El ID tiene que ser un número.")
        elif opcion == 6:
        
            try:
                identificador = int(input("ID del servidor: "))
                nuevo_estado = input("Nuevo estado (encendido/apagado): ")
                cambiar_estado(servidores, identificador, nuevo_estado)
                print("Estado cambiado.")
            except ValueError as error:
                print("Error:", error)
        elif opcion == 7:
        
            try:
                identificador = int(input("ID del servidor: "))
                nombre_servicio = input("Nombre del servicio: ")
                nuevo_estado = input("Nuevo estado (activo/inactivo): ")
                cambiar_servicio(servidores, identificador, nombre_servicio, nuevo_estado)
                print("Servicio cambiado.")
            except ValueError as error:
                print("Error:", error)
        elif opcion == 0:
        
            print("Saliendo. Los cambios no se guardan al cerrar el programa.")
        else:
        
            print("Opción no válida.")

if __name__ == '__main__':
    main()

