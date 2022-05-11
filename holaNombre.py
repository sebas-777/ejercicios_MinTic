# Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.


def holaNombre(nombre):
    return "¡hola {}!".format(nombre)

print(  holaNombre("juan") )