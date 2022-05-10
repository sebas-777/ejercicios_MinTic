# calcular horas dormidas en un año

def promedioHD(horasDormidas):
    horasDdor = horasDormidas * 365
    horasTotalA = 365 * 24
    return (horasDdor / horasTotalA) * 100
   
  


print( promedioHD(8))