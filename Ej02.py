#ejercicios 1
edad= int(input("cuantos anios tienes: "))

if edad < 18:
    print("Es menor de edad")
else:
    print("Es mayor de edad")

#ejercicios 2
numero= int(input("introduce numero: "))

if numero < 0:
    print("El numero es negativo")
elif numero > 0:
    print("El numero es positivo")
else:
    print("El numero es cero")

#ejercicios 3

edad= int(input("cuantos anios tienes: "))
ingreso= int(input("cuantos ingresos tienes: "))
if edad >= 18 and ingreso > 0:
    print("Puede entrar")
else:
    print("No puede entrar")

#ejercicios 4

num1= float(input("Indidca el primer numero"))
num2= float(input("Indidca el segundo numero"))

if num1 < num2:
    print(num2, "es mayor")
elif num1 > num2:
    print(num2, "es mayor")
else:
    print("son equivalentes")

