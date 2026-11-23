# funciones.py

def imprime_linea():
    print("-"*25)

imprime_linea()

latencias_web = [1.5, 2.3, 4.8, 8.6]
latencias_ftp = [1.5, 4.2, 5.8, 8.5]

def calcula_media (lista):
    suma = 0
    for x in lista:
        suma += x
    return suma/len(lista) 

print("latencia web promedio", calcula_media(latencias_web))
print("latencia ftp promedio", calcula_media(latencias_ftp))

media_web = calcula_media(latencias_web)
media_ftp = calcula_media(latencias_ftp)

if media_web > media_ftp:
    print("latencia web es mayor")
elif media_web < media_ftp:
    print("latencia ftp es mayor")
else:
    print("las latencias son equivalentes")

