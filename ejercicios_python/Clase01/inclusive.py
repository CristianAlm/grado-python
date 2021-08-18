frase = 'todos somos programadores y no lo somos'
palabras = frase.split()
traduccion = []
for palabra in palabras:
    if palabra[-1] == 'o':
        palabraCambiada = palabra[:-1] + 'e' #igual a palabra hasta el lugar -1 mas la 'e'
    elif len(palabra)>1 and palabra[-2] == 'o': #primero verifico si la palabra tiene mas de un caracter
        palabraCambiada = palabra[:-2] + 'e' + palabra[-1]
    else:
        palabraCambiada = palabra
    #print(palabra,palabraCambiada)
    traduccion.append(palabraCambiada)

frase_t = ' '.join(traduccion)
print(frase)
print(frase_t)