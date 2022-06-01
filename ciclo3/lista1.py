# creamos una lista de listas

lista =[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

print(lista)

# Cuando pasamos a la función print el primer elemento de la lista:
print(lista[0])

# Si queremos acceder al primer entero almacenado en la lista
# contenida en la primera componente de la lista principal:

print(lista[0][0])

# Acceder a todos los elementos de la primera componente de una
# lista compuesta por listas:

for x in range(len(lista[0])):
    print(lista[0][x])