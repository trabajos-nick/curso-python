
#codigo optimizado:
frase= input("Dime una frase y te calculo cuanto tardarias si tuvieras que decirla:")

def frase_calc(frase):
    palabra_separada = len(frase.split(" "))
    resultado1 = palabra_separada/2
    resultado2 = palabra_separada * 100 // 2 * 1.3 / 100
    return (resultado1,resultado2,palabra_separada)

palabras_suyas, palabras_dalto, can_palabra = frase_calc(frase)
print(f'Dijiste {can_palabra} palabras, y tardarias {palabras_suyas} segundos en decirlo')
print(f'Dalto lo diria en {palabras_dalto} segundos')

if can_palabra > 120:
    print ("oye, deja de hablar tanto coño")


#codigo original

#palabras_separadas = frase.split(" ")
#cantidad_de_palabras = len(palabras_separadas)
#print(f'Dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirlo')
#print(f'Dalto lo diria en {cantidad_de_palabras * 100 // 2 *1.3 / 100} segundos')
#if cantidad_de_palabras > 120:
#    print("oye, deja de hablar tanto coño")

    




