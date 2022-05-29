from interfaz import *


print("Iniciando Programa")
opcion = None
while opcion != "5":
    opcion = menuPrincipal()
    if opcion == "1":
        crearTarea()
    elif opcion == "2":
        consultarTareas()
    elif opcion == "3":
        actualizarTarea()
    elif opcion == "4":
        eliminarTarea()
        print("Fin del programa")