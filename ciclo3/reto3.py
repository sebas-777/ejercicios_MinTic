def AutoPartes(ventas:list):
    resultado ={}
    for x in range(len(ventas)):
        resultado[x] =[ventas[x]]
    return resultado

def consultaRegistro(ventas,idProductos):
    resultado2 ={}
    for i in ventas:
        if  idProductos == ventas[i][0][0]:
            resultado2[i] =ventas[i]
    
    resultado3 = ''
    if len(resultado2)==0:
        resultado3 = 'No hay registro de venta de ese producto'
    else:
        for i in resultado2:
            resultado3 += 'Producto consultado :{} Descripción {}#Parte {}Cantidad vendida {}Stock {}Comprador {}Documento {}Fecha Venta {} \n'.format(ventas[i][0][0],ventas[i][0][1],ventas[i][0][2],ventas[i][0][3],ventas[i][0][4],ventas[i][0][5],ventas[i][0][6],ventas[i][0][7])
    return print(resultado3)

a =[(2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),(2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),(2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'), 
   (3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),(9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')]


r =AutoPartes(a)
consultaRegistro(AutoPartes(a),2010)