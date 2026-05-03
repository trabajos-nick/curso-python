#creando una lista con list
lista = list([34,32,32,32,3,23,2])

#vuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)

#agregando un elemento a la lista
lista.append(65)

#agregando un elemento a la lista en un indice especifico
lista.insert(2, 56)

#Agregando varios elementos a la lista
lista.extend([False,2023])

#eliminando un eleemnto de la lista por el indice
lista.pop(3) #-1 para eliminar el ultimo, -2 para eliminar el penultimo y asi,susesivamnete...

#removiendo un elemento de la lista por su valor
lista.remove(2)

#eliminando todos los valore de la lista
#lista.clear

#ordenando la lista de forma ascendente (si usamos el parametro reverse=True lo ordena en reversa)
lista.sort()

#invierte los elementos de una lsta
lista.reverse()

#verificando si un elemento se encuentra en la lista
elemento_encontrado = lista.index(False)

print (set(["asdasd","sddfsdfs"]))