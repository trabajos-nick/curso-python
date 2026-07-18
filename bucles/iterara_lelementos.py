animales= ["perro", "gato", "loro", "cocodrilo"]
numeros = [10,54,23,60]

'''
#recorriendo la lista animales
for animal in animales:
    print(f'Ahora la variable animal es igual a: {animal}') 

#recorriendo la lista numeros y multiplicando cada valos pro 10
for numero in numeros:
    resultado = numero * 10
    print(resultado)
'''
#iterando dos listas del mismo tamaño al mismo tiempo
for numero,animal in zip(animales,numeros):
    print(f'recorriendo lista 1: {numero}')
    print(f'recorriendo lista 2: {animal}')

#forma no optima de recorrer una lista
for num in range(len(numeros)): #no funciona en conjuntos
    print(numeros[num])

#forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'el indice es: {indice} y el valor es: {valor}')

#usando for/else
for numero in numeros:
    print(f'ejecutando el ultimo bucle, valor actual: {numero}')
else:
    print("el bucle termino")

#todo lo anterior funciona exactamente igual para tuplas y conjuntos