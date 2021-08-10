cadena = input('Ingrese la palbra')
buscar = input('Ingrese la letra a buscar')
contador = 0
print(cadena)

for letra in cadena:
    if letra ==buscar:
        contador = contador +1
print('La cantidad de la letra ', buscar, ' en la palabra ', cadena,' es ', contador)