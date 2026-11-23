# importes
from servidores import SERVIDORES;
import funciones as f 

# EJ01

# print(f.mostrar_inventario(SERVIDORES))

# # EJ02

# iden = int(input("introduce la id a buscar: "))

# f.buscar_por_id(SERVIDORES, iden)

# # EJ03
# reses = input("introduce el estado a buscar: ")
# busca_estado = f.filtrar_por_estado(SERVIDORES, reses)
# f.mostrar_inventario(busca_estado)

# rerol = input("introduce el rol a buscar: ")
# busca_rol = f.filtrar_por_rol(SERVIDORES, rerol)
# f.mostrar_inventario(busca_rol)

# EJ04

# res = f.mostrar_resumen(SERVIDORES)
# print(res)

# EJ06

# f.mostrar_servicios_empresa(SERVIDORES)
# print(f.contar_servicios_inactivos(SERVIDORES))

#Ej07
# id = int(input("introduce id: "))
# try:
#     f.cambiar_estado(SERVIDORES, id, "encendido")
# except IdInvalida:
#     print(" >> id no valida") 

# try:
#     f.cambiar_estado(SERVIDORES, id, "up")
# except ValueError as e:
#     print(" >> Valor no valido") 
#EJ08

f.menu(SERVIDORES)