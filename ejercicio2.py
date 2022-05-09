print('Empezo el programa , para detrminar si un numero es positivo , par o impar')
print('Ingrese el numero para el analisis')
numero = int( input() )

if numero >  0:
    print('numero es positivos')
    if numero%2 == 0:
        print('numero es par ')
    else:
        print('numero es impar')
        
else:   
    print('numero es negativo')

print('fin del programa')