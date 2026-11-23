import os
#E01

#E02



# tmp = os.listdir("/tmp")
# ind = 0

# for x in tmp:
#     ind += 1
#     print( ind, "-", x)

#E03

car = input("introduce el nombre de la carpeta a crear: ")

os.mkdir("/tmp/"+car)
