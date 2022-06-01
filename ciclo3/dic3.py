def reportarPromedio(dicReporte):
    return dicReporte["estudiante"] + " = " + str( dicReporte["promedio"] )

def generarReporteNotas(dicNotas):
    sumatorio = 0
    sumatorio += dicNotas["nota1"]
    sumatorio += dicNotas["nota2"]
    sumatorio += dicNotas["nota3"]
    sumatorio += dicNotas["nota4"]
    promedio = round(sumatorio/4,2)
    reporteNotas = {
                    "promedio":promedio,
                    "estudiante":dicNotas["estudiante"]
                   }
    return reporteNotas

dicNotas ={
            "estudiante":"beneficiario Rodriguez",
            "nota1":3.0,
            "nota2":4.0,
            "nota3":5.0,
            "nota4":3.0
            
} 
print(reportarPromedio(generarReporteNotas(dicNotas)))