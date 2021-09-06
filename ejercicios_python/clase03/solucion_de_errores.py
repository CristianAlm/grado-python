#El while se cortaba(return False) antes de poder recorrer la frase(i+=1)
#Ademas no se consideraba la A mayuscula
#A continuacion el codigo corregido

'''
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n: 
        if expresion[i] == 'a':
            #print(i)  
            return True
        elif expresion[i] == 'A':
            return True
        else:
            i += 1
        if i==n:#Devuelve False porque llego al final y no encontro la letra
            print(i,n)
            return False    
    
print(tiene_a('UNSAM 2020'))
print(tiene_a('abracadabra'))
print(tiene_a('La novela 1984 de George Orwell'))
'''

#La funcion y los bucles tenia errorews de sintaxis
#Ademas no se consideraba la A mayuscula
#A continuacion el codigo corregido

'''
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a' or expresion[i] == 'A':
            return True
        i += 1
    return False

print(tiene_a('UNSAM 2020'))
print(tiene_a('La novela 1984 de George Orwell'))
'''

#Los parametros tienen que ser String y estaban pasando un int
#
#A continuacion el codigo corregido

'''
def tiene_uno(expresion):
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


print(tiene_uno('UNSAM 2020'))
print(tiene_uno('La novela 1984 de George Orwell'))
print(tiene_uno('1984'))
'''
#La funcion le falto el return
#
#A continuacion el codigo corregido

'''
def suma(a,b):
    return  a + b

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")
'''

#No imprime como corresponde porque la "registro" esta en una linia que no corresponde, tiene que estar dentro del bucle for
#Ademas no se consideraba la A mayuscula
#A continuacion el codigo corregido

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('Clase02/Data/camion.csv')
pprint(camion)