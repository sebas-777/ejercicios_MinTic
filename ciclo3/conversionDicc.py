# conversion de cadena a diccionario 

cadena = "hola"
diccionario = dict(zip(range(len(cadena)),cadena))
print(diccionario)


# conversion lista a diccionario

lista = ['h','o','l','a']
diccionario = dict(zip(range(len(lista)),lista))
print(diccionario)

# conversion tupla a diccionario

tupla =('h','o','l','a')
diccionario = dict(zip(range(len(tupla)),tupla))
print(diccionario)

#conversion conjunto a diccionario

conjunto = {'h','o','l','a'}
diccionario = dict(zip(range(len(conjunto)),conjunto))
print(conjunto)


# conversion