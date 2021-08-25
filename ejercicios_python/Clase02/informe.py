import csv

def leer_precios(nombre_archivo):
    with open(nombre_archivo, 'rt') as archivo:
        rows = csv.reader(archivo)
        preciosLocales = []

        for row in rows:
            try:
                datos = {
                    'nombre': row[0],
                    'precio': float(row[1]),
                }
                #print(datos)
                preciosLocales.append(datos)
            except:
                print('Faltan datos en la línea', row, 'del archivo.')
        return preciosLocales

def leer_camion(nombre_archivo):
    with open(nombre_archivo, 'rt') as archivo:
        rows = csv.reader(archivo)
        headers = next(rows)
        camion = []

        for row in rows:
            lote = {
                'nombre': row[0],
                'precio': float(row[2]),
                'cajones': int(row[1])}
            #print(lote)
            camion.append(lote)
        return camion

def calcularBalance(camion, descarga):
    
    balanceLocal =0

    def costo_camion(nombre_archivo):
        total = 0.0
        with open(nombre_archivo, 'rt') as f:
            rows = csv.reader(f)
            headers = next(rows)
            for i, row in enumerate(rows):
                try:
                    ncajones = int(row[1])
                    precio = float(row[2])
                    total += ncajones * precio
                except ValueError:
                    print('Faltan datos en la línea', i, 'del archivo.')
        return total

    def obtenerPrecio(camion, descarga):
        totalVenta =0
        precioCajon=0
        nombreFrutaVenta = ''
        with open(camion, 'rt') as archivo:

            rows = csv.reader(archivo)
            headers = next(rows)
            for i, row in enumerate(rows):
                try:
                    nombre = row[0]
                    #print(nombre , i)
                except:
                    print('Faltan datos en la línea', i, 'del archivo.')
                
                if nombre:
                    f = open(descarga, 'rt')

                    for line in f:
                        rowCamion=line.split(',')
                        try:
                            nombreFrutaVenta = rowCamion[0]
                            #print(nombreFrutaVenta, line)
                        except ValueError:
                            print('Faltan datos en la línea', i, 'del archivo.')
                        
                        if nombre == nombreFrutaVenta:
                            precioCajon = float(row[1])*float(rowCamion[1])
                            totalVenta += precioCajon

                    f.close()
        return totalVenta


    precioVta = obtenerPrecio(camion, descarga)
    print('El precio de Venta es', float(precioVta))
    costo = costo_camion(camion)
    print('Costo total:', float(costo))

    balanceLocal = precioVta - costo
    
    return balanceLocal

#info = leer_camion('unsamRemoto/ejercicios_python/Clase02/Data/camion.csv')#Lo que re
#print(info)
#precios = leer_precios('unsamRemoto/ejercicios_python/Clase02/Data/precios.csv')
#print(precios)

balance = calcularBalance('unsamRemoto/ejercicios_python/Clase02/Data/camion.csv', 'unsamRemoto/ejercicios_python/Clase02/Data/precios.csv')
print('El resultado de la operacion es ', balance)
