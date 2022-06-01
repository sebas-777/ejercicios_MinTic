def promedioNotas2(dicNotas):
    sumatoria = 0
    sumatoria +=dicNotas["nota1"]
    sumatoria +=dicNotas["nota2"]
    sumatoria +=dicNotas["nota3"]   
    sumatoria +=dicNotas["nota4"]
    promedio = round(sumatoria/4,2)
    return promedio


dicNotas = {} 
dicNotas["nota1"] = 3.0
dicNotas["nota2"] = 2.0
dicNotas["nota3"] = 4.0 
dicNotas["nota4"] = 5.0
print("El promedio es : ",promedioNotas2(dicNotas))     
