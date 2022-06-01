def promedioNotas(nota1,nota2,nota3,nota4):
    promedio = round((nota1 + nota2 + nota3 + nota4) / 4,2)
    return promedio
print("El promedio es: ",promedioNotas(3.0,3.0,3.0,3.0))