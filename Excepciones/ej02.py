try:
    edad = int(input("Edad: "))
    print("Edad:", edad)

except ValueError:
    print("Debe introducir un número entero")
    