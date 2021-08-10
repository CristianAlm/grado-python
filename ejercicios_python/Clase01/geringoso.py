cadena = 'Geringoso'
capadepenapa = ''

for letra in cadena:
    if letra=="a":
        capadepenapa=capadepenapa+letra+"pa"
    elif letra=="e":
        capadepenapa=capadepenapa+letra+"pe"
    elif letra=="i":
        capadepenapa=capadepenapa+letra+"pi"
    elif letra=="o":
        capadepenapa=capadepenapa+letra+"po"
    elif letra=="u":
        capadepenapa=capadepenapa+letra+"pu"
    else:
        capadepenapa=capadepenapa+letra
print(capadepenapa)