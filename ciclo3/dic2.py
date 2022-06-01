def promedioNotas2(dicNotas):
    sumatoria = 0
    sumatoria += dicNotas["nota1"]
    sumatoria += dicNotas["nota2"]
    sumatoria += dicNotas["nota3"]
    sumatoria += dicNotas["nota4"]
    promedio = round(sumatoria/4,2)
    return promedio
dicNotas = {
            "nota1":3.0,
            "nota2":4.0,
            "nota3":5.0,
            "nota4":3.0,
} 
print("El promedio es : " ,promedioNotas2(dicNotas))