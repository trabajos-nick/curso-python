#forma no optima de sumar valores
#def suma(lista):
#   numeros_sumados = 0
#   for numero in lista:
#       numeros_sumados = numeros_sumados + numero
#   return numeros_sumados

#resultado = suma([5,3,5,9,8,7,6])

#forma optima de utilizar valores
def suma_total(numeros):
    return sum([*numeros])

resultado2 = suma_total([5,3,5,9,8,7,6])

print(resultado2)

#lo mismo que arriba per utilizando el ´operador * como argumento (*args)
def suma(nombre,*numeros):
    return f"{nombre}, la suma de tus numeros es: {sum(numeros)}"

resultado = suma("Nick",5,3,5,9,8,7,6)


