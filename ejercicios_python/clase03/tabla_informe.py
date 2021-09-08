import csv

headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
espacios = ('-----', '-----', '-----', '-----')

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

def hacer_informe(camion, precios):

    lista =[]   

    for dic_camion in camion:
        product=dic_camion['nombre']
        for dic_venta in precios:
            if dic_venta['nombre']==product:
                tupla=(dic_camion['nombre'] ,dic_camion['cajones'], dic_camion['precio'],float(dic_venta['precio'])-float(dic_camion['precio']))
                lista.append(tupla)
                #lista.append(f"{dic_camion['nombre']:>10s} {dic_camion['cajones']:>10d} {dic_camion['precio']:>10.2f} {float(dic_venta['precio'])-float(dic_camion['precio']):>10.2f}")
                #print(lista)
    return lista
        

camion = leer_camion('Clase02/Data/camion.csv')
precios = leer_precios('Clase02/Data/precios.csv')

informe = hacer_informe(camion, precios)

for header in headers:
    print(f'{header:>10s}', end = "")
print('\n')
print ('---------- ---------- ---------- ----------')
for r in informe:
    print('%10s %10d %10.2f %10.2f' % r)

