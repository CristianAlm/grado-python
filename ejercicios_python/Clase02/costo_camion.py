#con funcion
import csv

def costo_camion(nombre_archivo):
    f = open(nombre_archivo, 'rt')
    total=0

    rows = csv.reader(f)
    headers = next(rows)
    headers
    ['nombre', 'cajones', 'precio']
    for row in rows:
        print(row)
        cajon=float(row[1])
        precio=float(row[2])
        total += cajon*precio
        
    f.close()
    return float(total)

costo = costo_camion('unsamRemoto/ejercicios_python/Clase02/Data/camion.csv')
print('Costo total:', float(costo))




