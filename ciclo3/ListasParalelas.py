nombres = []
edades = []

for x in range(5):
    nom = input(" Por favor ingrese el nombre de las personas : ")
    nombres.append(nom)
    ed = int( input("Ingrese la edad de dicha persona : "))
    edades.append(ed)
    
print("Nombre de las personas mayores de edad :")

for x in range(5):
    if edades[x]>=18:
        print(nombres[x])