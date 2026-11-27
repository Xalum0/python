import requests

# URL de la API
URL_PRODUCTOS = "https://dummyjson.com/products"

def obtener_productos(limite=100, skip=0):
    """Consulta DummyJSON y devuelve la lista 'products'.

    Propaga RequestException si falla HTTP o la conexión y ValueError si
    la respuesta no contiene la estructura esperada.
    """
    if not isinstance(limite, int) or isinstance(limite, bool) or limite <= 0:
        raise ValueError("El límite debe ser un entero positivo")

    respuesta = requests.get(
        URL_PRODUCTOS,
        params={"limit": limite, "skip": skip},
        timeout=10,
    )
    respuesta.raise_for_status()  #  Si error (400 a 599), excepción HTTPError; si ok devuelve None.
    datos = respuesta.json()

    if not isinstance(datos, dict) or not isinstance(datos.get("products"), list):
        raise ValueError("Respuesta inesperada: falta la lista 'products'")

    return datos["products"]

def mostrar_productos(productos):
    """Imprime un listado compacto sin alterar los datos."""
    if productos:
        print(f"{'ID':<5} {'PRODUCTO':<48} {'CATEGORIA':<20} {'PRECIO':<12} {'STOCK':<5}")
        print("-"*95)
        for x in productos:
            print(f"{x["id"]:<5} {x["title"]:<48} {x["category"]:<20} {x["price"]:<12.2f} {x["stock"]:>5}") 
    else:
        print("lista vacia")    

def buscar_por_titulo(productos, texto):
    texto = texto.lower().strip()
    res = []

    for p in productos:
        if texto in p['title'].lower():
            res.append(p)
    return res

def filtrar_productos(productos, categoria=None, precio_max=None, solo_disponibles=False):
    if categoria != None:
        categoria = categoria.strip()
    
    lista = []

    for p in productos:
        if (categoria == None or p['category'] == categoria) and (precio_max == None or p['price'] < precio_max) and (p['stock'] > 0 or solo_disponibles == False):
            lista.append(p)

    return lista    

def calcular_estadisticas(p):
    total = len(p)
    suma = 0
    stk = 0
    maxi = None
    precio_medio = 0
    cat = {}

    if total != 0:
        for producto in p:
            suma += producto['price']
            stk += producto['stock']
            if (maxi == None or maxi['price'] < producto['price']):
                maxi = producto

            categoria = producto['category']
            cat[categoria] = cat.get(categoria, 0) + 1

        precio_medio = suma / total    
    
    res = {
        "total": total,
        "precio medio": precio_medio,
        "stock": stk,
        "mas_caro": maxi,
        "por_categoria": cat
    }

    return res   
