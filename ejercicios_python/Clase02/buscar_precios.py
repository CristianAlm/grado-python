def buscar_precio(nombre_archivo, fruta):

    f = open(nombre_archivo, 'rt')

    for line in f:
        row=line.split(',')
        if row[0] == fruta:
            print('El precio de ', fruta, 'es ', row[1], '$')
            break
    else:
        print('No se encuentra')
    
    f.close()

usuario = input('Ingrese la fruta: ')
precio = buscar_precio('unsamRemoto/ejercicios_python/Clase02/Data/precios.csv', usuario)
