# retorno si el numero es mayor o menor a cero

def validarNumero(a):
    if a > 0:
        mensaje ="El numero es Mayor a 0"
    else :
        mensaje = " El numero es Menor a 0"
        
    return mensaje



print( validarNumero(0))