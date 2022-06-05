frutas ={"Banana":2.3,"Kiwi":10.2,"Mango":15.3,"Patilla":5.6}

fruta = input("Digite la fruta que desea : ").title()



if fruta in frutas:
    cant =float( input("Cuantas frutas desea comprar? :"))
    print(f"la cantidad de {cant} de la fruta {fruta} tiene un costo de {frutas[fruta]*cant}")
else:
    print("no tenemos esta fruta en este momento")