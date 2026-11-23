from utiles import *

latencias_web = [1.5, 2.3, 4.8, 8.6]
latencias_ftp = [1.5, 4.2, 5.8, 8.5]

suma_web = calcula_suma(latencias_web)
suma_ftp = calcula_suma(latencias_ftp)

print("suma latencias web: ", suma_web)
print("suma latencias ftp: ", suma_ftp)

print("suma latencias web: ", calcula_suma(latencias_web))
print("suma latencias ftp: ", calcula_suma(latencias_ftp))

media_web = calcula_media(latencias_web)
media_ftp = calcula_media(latencias_ftp)




