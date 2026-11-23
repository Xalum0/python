import os

# Se invoca dejando los paréntesis vacíos
directorio_actual = os.getcwd()

print(f"El script se está ejecutando desde: {directorio_actual}")

import os

# Definimos el argumento: el nombre de la carpeta que queremos crear
carpeta_backup = "/var/backups/diarios"

# Invocación pasando el parámetro (obligatorio)
os.mkdir(carpeta_backup)

print(f"Directorio creado correctamente en: {carpeta_backup}")