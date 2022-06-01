def suma(a,b):
    return " la suma es :" + str(a+b)

def resta(a,b):
    return " la resta es :" + str(a-b)


def invocarFuncion(funcion, a,b):
    msn = funcion(a,b)
    print(msn)
    return