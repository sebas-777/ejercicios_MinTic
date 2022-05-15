# import math -> me importa TODA LA LIBERIA

import math

# para importar una sola parte de la libreria 

from math import factorial
from math import sin
from math  import sqrt 
from math import pi as PI

# print( math.e )

# print( math.cos (1.6))

# print( math.factorial (5)) 

# resultado = sin(PI/ 2)
# print(resultado)
# resultado = sqrt(3*PI)
# print(resultado)

def sumarnumero(numero1,numero2):
    suma = numero1 + numero2
    mensajeResultado = " la suma es " + str( suma )
    return mensajeResultado


# escribir una funcion que retorne una cadena de caracteres 
# retorne el numero es mayor a cero y es : xxx si a >= 0
# retorne el  numero es menor a cero y es : xxxx si a < 0

def tipoDeNumero ( a ):
    
    if a >= 0:
        mensaje = " el numero es mayor a 0"  
    else:
        mensaje = " el numero es menor a 0" 
    return mensaje

# resultado = tipoDeNumero(852147878) 

# print(tipoDeNumero (10000))
    
    
 
 
# print( " ingresar un numero por favor :")

# numeroTexto = int (input() )

# resultado = tipoDeNumero( numeroTexto)


# print( resultado)

# funcion factorial

def factorial(numero):
    if numero < 2 :
      mensaje = "el factorial de {} es 1 : ".format(numero)
    else :
        fact = 1
        for num in range(2,numero + 1):
            fact *= num
            mensaje ="el  factorial de {} es {}".format(numero,fact)
    return mensaje