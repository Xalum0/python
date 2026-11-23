import os
try:
    os.mkdir("/root/nueva_carpeta")
except PermissionError:
    print("no tiene permisos")