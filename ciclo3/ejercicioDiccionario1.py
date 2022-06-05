nombre = input("Cual es su nombre :") 
edad = input(" Cual es su edad :") 
direccion = input("Cual es su direccion :")
telefono = input(" Cual es su telefono :")

dictDatosUsuarios = {"nombre": nombre,"edad": edad,"telefono":telefono,"direccion":direccion,} 

print("La persona", dictDatosUsuarios["nombre"],"tiene",dictDatosUsuarios["edad"]," años, vive en ", dictDatosUsuarios["direccion"],"y su numero es", dictDatosUsuarios["telefono"])