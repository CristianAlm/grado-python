frutas = ['banana', 'manzana', 'mandarina']

def agregar(prueba):
    local=[]
    capadepenapa=''
    for palabra in prueba:
        for letra in palabra:
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
        local.append(capadepenapa)
        capadepenapa =''

    dictgeringoso = dict(zip(prueba,local))
    return dictgeringoso
    
modificada = agregar(frutas)
print(modificada)
