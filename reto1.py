# Ciclo 1 Fundamentos de programación
# Reto 1
# Descripción del problema: Una entidad Bancaria o entidad financiera, requiere calcular 
# el valor de los intereses ganados y el total final de dinero para diferentes clientes, de 
# acuerdo, a una cantidad de dinero invertida en un CDT. Un CDT por su parte, es un 
# producto financiero que ofrece la posibilidad de guardar dinero durante un tiempo 
# determinado para recibir posteriormente sus intereses devengados, asimismo, ofrece 
# rendimientos a una tasa fija, asegurando una rentabilidad libre de riesgo en un tiempo 
# determinado que por lo general debe ser mayor a dos (2) meses. Si, este dinero se retira 
# antes de este periodo se aplica una penalidad del 2%.
# En ese sentido, el valor de los intereses ganados por un periodo de tiempo superior a dos 
# meses se determina a través de la siguiente formula:

# Donde: 
# cantidad = dinero ingresado en el CDT
# porcentaje_interes = 3% (0.03).
# tiempo = cantidad de tiempo
# En consecuencia, el valor total del dinero será calculado a través de la siguiente formula:
# Se debe determinar el valor total a retirar por el cliente que invirtió en el CDT al final del 
# periodo.
# Por otra parte, para un periodo de tiempo inferior o igual a dos meses se debe aplicar la 
# siguiente formula:
# Donde: 
# cantidad = dinero ingresado en el CDT
# procentajea perder = 2% (0.02)
# En consecuencia, el valor total del dinero será calculado a través de la siguiente formula:
# Para responder a este planteamiento, escriba una función que reciba como parámetros: 
# una cadena con el usuario del cliente como dato alfanumérico, el capital aportado y el 
# tiempo del CDT y, en consecuencia, retorne una cadena de caracteres que le proporcione
# al banco la información que desea obtener. 
# La cadena debe tener para el caso de las ganancias, la siguiente estructura:
# “Para el usuario {} La cantidad de dinero a recibir, según el monto inicial {} para un 
# tiempo de {} meses es: {}”
# para el caso de las pérdidas:
# “Para el usuario {} La cantidad de dinero a recibir, según el monto inicial {} para un 
# tiempo de {} meses es: {}”

# Ejemplo:
# Usuario Monto Tiempo Salida
# AB1012 1000000 3 Para el usuario AB1012 La cantidad de dinero a 
# recibir, según el monto inicial 1000000 para un tiempo 
# de 3 meses es:1007500.0
# ER3366 650000 2 Para el usuario ER3366 La cantidad de dinero a 
# recibir, según el monto inicial 6500000 para un tiempo 
# de 2 meses es: 637000
# Entradas:
# Nombre Tipo Descripción
# usuario str usuario
# capital int monto a ingresar
# tiempo int tiempo del CDT
# Salida:
# Tipo del retorno Descripción
# str Ganancias o pérdidas generadas, a manera de un texto organizado 
# “Para el usuario {} La cantidad de dinero a recibir, según el monto 
# inicial {} para un tiempo de {} meses es: {}

# def CDT(usuario,capital,tiempo):
    
#     if tiempo <= 2:
#         valor_a_perder = capital * 0.02
#         valor_total = capital - valor_a_perder
#         return "Para el usuario {} La cantidad de dinero a recibir, según el monto inicial {} para un tiempo de {} meses es: {}".format(usuario,capital,tiempo,valor_total)
#     else :
#         valor_interes = (capital*0.03*tiempo)/12
#         valor_total = capital + valor_interes
#         return"Para el usuario {} La cantidad de dinero a recibir, según el monto inicial {} para un tiempo de {} meses es: {}".format(usuario,capital,tiempo,valor_total)
    
# print(CDT("juan",1000000,3))
 
def CDT(usuario,capital,tiempo):
     
     if tiempo > 2:
          valor_interes = (capital*0.03*tiempo)/12
          valor_total = capital + valor_interes
          return"Para el usuario {} La cantidad de dinero a recibir, según el monto inicial {} para un tiempo de {} meses es: {}".format(usuario,capital,tiempo,valor_total)
     else:
         valor_a_perder = capital * 0.02
         valor_total = capital - valor_a_perder
         return"Para el usuario {} La cantidad de dinero a recibir, según el monto inicial {} para un tiempo de {} meses es: {}".format(usuario,capital,tiempo,valor_total)
 
print(CDT("juan",1000000,3))
           