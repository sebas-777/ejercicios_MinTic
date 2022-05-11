# retornar un mensaje (STR) que diga :el volumen es :xxx

def mensajeVolumenSolido(ancho,alto,profundo):
    volumen =ancho * alto * profundo
    resultado = " el volumen es : "+ str( volumen)
    return resultado


print(mensajeVolumenSolido(10000,20000,89000))