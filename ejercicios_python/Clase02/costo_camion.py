#con funcion
import csv
'''

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

'''
def costo_camion(nombre_archivo):
    '''Computa el precio total del camion (cajones * precio) de un archivo'''
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

costo = costo_camion('unsamRemoto/ejercicios_python/Clase02/Data/camion.csv')
print('Costo total:', float(costo))



