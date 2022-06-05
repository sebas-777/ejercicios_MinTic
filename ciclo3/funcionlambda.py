suma = lambda val1 , val2 : val1 + val2
operacion = lambda operacion, val1 = 0  , val2 = 0 : operacion(val1, val2)

resultado = operacion (suma,10 ,20)

print(resultado)