
# camion_commandline.py
import csv
import sys

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

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = 'unsamRemoto/ejercicios_python/Clase02/Data/camion.csv'

costo = costo_camion(nombre_archivo)
print('Costo total:', costo)
