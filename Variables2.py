# Variables2.py

# Variables, asignación (=) y tipos (int, float, str...) 

saldo_total = 254.55  # float
email = 'ana@local.com'  # str
print( "saldo_total")
print( saldo_total )
    # print(email)   # error indentación

# Tipos
print("tipo de email: ", type(email)  )
print("tipo de saldo_total: ", type(saldo_total)  )
edad = 43
print("tipo de edad", type(edad), edad*2)

# Variables pueden cambiar de tipo aun asi no es recomendable
email = 4
print( "Tipo email: ", type(email)  )

print("El email es ", email, " y el saldo es \n", saldo_total, "\n")