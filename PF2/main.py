import funciones as f 
from productos import LISTA_dummy, PRODUCTOS_EJEMPLO


lista = f.obtener_productos() # usando la API
# lista =  LISTA_dummy        # si no usa la API

# print(lista)

# f.mostrar_productos(PRODUCTOS_EJEMPLO)
# texto = input("texto a buscar: ")
# encontrados = f.buscar_por_titulo(lista, texto)
# f.mostrar_productos(encontrados)

cat = "laptops"
prec = None
dis = True
res = f.filtrar_productos(lista, cat, prec, dis)
f.mostrar_productos(res)

