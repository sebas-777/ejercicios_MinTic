from sqlite3 import TimestampFromTicks


tareas =  {                                                     
    
"t1":{
    "descripcion":" Ir a Mercar ",
    "estado": "Pendiente",
    "tiempo": 60,
},
"t2":{
    "descripcion":" Cocinar ",
    "estado": "Pendiente",
    "tiempo": 30,
},
"t3":{
    "descripcion":" Hacer Ejercicio ",
    "estado": "Pendiente",
    "tiempo": 45,
}
    
}


def menuPrincipal():
    print( " ----Aplicacion CRUD para Tareas Pendientes ----")
    print( " ----1. Crear Tarea :  ----")
    print( " ----2. Consultar Tareas : ----")
    print( " ----3. Actualizar Tareas :  -----")
    print( " ----4. Eliminar Tarea : -----")   
    print( " ----5. Salir ----")
    opcion =input(" Ingrese una opcion : ")
    return opcion


def crearTarea():
    cod =input("Por favor ingrese el codigo de la tarea: ")
    claves = tareas.keys()
    if cod in claves:
        print(" la clave ya existe, por intente con otra clave.")
        return
    descrip =input("Por favor ingrese el descripcion de la tarea: ")
    tiempo =int( input("Por favor ingrese el tiempo de la tarea: ") )
    tareas[cod] = {
        "descrpcion":descrip,
        "estado":"Pendiente",
        "tiempo":tiempo
    }
    print("La tarea se creo exitosamente!")
    
def consultarTareas():
    for(codTarea,tarea) in tareas.items():
        print("-----------------------------")
        print("el codigo de la tarea: " + codTarea)
        print(" la descripcion de la trea es : " + tarea["descripcion"])
        print(" el estado de la tareas es : " + tarea["estado"])
        print(" el tiempo de la tarea es  : " + str (tarea["tiempo"]) + "minutos") 
    print("------------------------------") 
    print("Retornado a la menu principal: ") 
    
        
def actualizarTarea():
    codigo =input(" Por favor ingrese el codigo de la tarea que desea actualizar :")
    claves = tareas.keys()
    if codigo not in claves:
        print("el codigo no se encuentra no existe")
        return
    nuevaDescrip = input("por favor ingrese  la nueva descripcion  de la tarea :")
    nuevoEstado = input(" por favor ingrese el nuevo estado de la tarea :")
    nuevoTiempo = int( input(" por favor ingrese el nuevo tiempo de la tarea :") )
    tareas[codigo] = {
         "descripcion": nuevaDescrip,
         "estado": nuevoEstado,
         "tiempo": nuevoTiempo,
    }
    print(" la tarea con codigo " + codigo + " ha sido actualizado")
    
    
def eliminarTarea():
    codigo =input(" Por favor ingrese el codigo de la tarea que desea Eliminar:")
    claves = tareas.keys()
    if codigo not in claves:
        print("el codigo no se encuentra no existe")
        return
    tareas.pop(codigo)
    print(" la tarea con codigo " + codigo + " ha sido eliminada")
    