

cant =int(input("Digite la cantidad de dulces : "))
tipo = int(input("Digite el tipo de dulce :  "))

dulceria = {"cant":cant,"tipo":tipo,"precio":0}

if dulceria["tipo"] ==1:
    dulceria["precio"] = 3 
    monto = dulceria["cant"]*dulceria["precio"]
    if dulceria["cant"] <=5:
        monto -=0.5 # monto = monto - 0.5 
    elif dulceria["cant"] <=10:
        descuento = monto * 0.07 
        monto -= descuento # monto = monto - descuento

elif dulceria["tipo"] == 2:
    dulceria["precio"] = 4  
    monto = dulceria["cant"]* dulceria["precio"]
    if dulceria["cant"] > 7:
        descuento = monto * 0.05 
        monto -= descuento # monto = monto - descuento
elif dulceria["tipo"] == 3:
    dulceria["precio"] = 5   
    monto = dulceria["cant"]* dulceria["precio"]
    if dulceria["cant"] > 4:
        descuento = monto * 0.15 
        monto -= descuento # monto = monto - descuento
        
else:
    print("Tipo de dulce no disponible") 
    
print(f" el tipo de dulce {dulceria['tipo']}, tiene  un costo unitario de {dulceria['precio']}, usted lleva {dulceria['cant']}, por un total de {monto}")