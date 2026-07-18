#falto el profe y los pibes van a armar la clase

#funcion para obtener el aistente y al profesosr segun la edad.
def obtener_compañeros(cantidad_compañeros):

    #creando la lista con los compañeros
    compañeros = []

    #ejecutando un for para pedir informacion de cada compañero
    for i in range(cantidad_compañeros):
        nombre = input("ingrese el nombre del compañero: ")
        edad = int(input("ingresa la edad del compañero: ")) 
        compañero = (nombre,edad)

        #agregando la informacion a la lista
        compañeros.append(compañeros)

    #ordenandolos de menor a mayor segun la edad
    compañeros.sort(key=lambda x:x[1])

    #compañeros [x] devuelve una tupla con (nombre,edad) y despues accedemos al nombre para definir al asistente y al profesor
    asistente =compañeros[0][0]
    profesor = compañeros[-1][0]

    #retornamos una tupla
    return asistente,profesor

#desempaquetamos lo que nos retorna la funcion
asistente,profesor = obtener_compañeros(5)

#mostrando el resultado
print(f"El asistente es: {profesor} y su asistente es {asistente}")





