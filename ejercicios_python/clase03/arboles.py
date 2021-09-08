import csv
from collections import Counter
#import numpy as np

def leer_parque(nombre_archivo, parque):
    lista =[]
    with open(nombre_archivo, 'rt') as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        for fila in filas:
            registro = dict(zip(encabezados,fila))
            registro['altura_tat'] = float(registro['altura_tat'])
            if registro['espacio_ve']==parque:
                lista.append(registro)
    return lista

def especies(lista_arboles):
    lista=[]
    for arbol in lista_arboles:
        lista.append(arbol['nombre_com'])
    return set(lista)

def contar_ejemplares(lista_arboles):
    d = Counter()
    for arbol in lista_arboles:
        d[arbol['nombre_com']] += 1
    return d

def obtener_alturas(lista_arboles, especie):
    lista = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            lista.append(arbol['altura_tat'])
    return lista


gral_paz = leer_parque('Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')
len(gral_paz)

contar_ejemplares(gral_paz)

alturas_jac_gral_paz = obtener_alturas(gral_paz, ' Jacarandá')
