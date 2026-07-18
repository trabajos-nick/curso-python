numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,20]

#creando una funcion lambda para multiplicar por dos
multiplicar_por_dos = lambda x : x*2 #labda, crea funciones anonimas

#creando funcion comun que diga si es par o no
#def es_par(num):
#    if (num%2==1)
#        return True
    
#usando filter con un a funcion comun
#numeros_pares = filter(es_par,numeros)

#creando lo mismo que antes pero con lamda
numeros_pares = filter(lambda numero:numero%2 == 0,numeros)
print(list(numeros_pares))