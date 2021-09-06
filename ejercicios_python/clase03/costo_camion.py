# costo_camion.py
import csv

f = open('Clase03/Data/fecha_camion.csv')

def costo_camion(nombre_archivo):
    muestraLocal=[]
    filas = csv.reader(nombre_archivo)
    encabezados = next(filas)
    fila = filas

    for n_fila, fila in enumerate(filas, start=1):
        try:
            record =  dict(zip(encabezados, fila))
            print(record)
        except ValueError:
            print(f'Fila {n_fila}: No pude interpretar: {fila}')
    return muestraLocal

muestra =costo_camion(f)
#print(muestra)
f.close()

