'''
#creando una funcion de 3 parametro
def frase(nombre, apellido,adjetivo):
    return f'Hola {nombre} {apellido}, estas muy {adjetivo}'

#utilizando keywords arguments
frase_resultante = frase(nombre="Nick",apellido="Duran",adjetivo="Sexy")
'''
#creando la misma funcion con un parametro opcional y un valor por defecto
def frase(nombre, apellido,adjetivo = "Tonto"):
    return f'Hola {nombre} {apellido}, estas muy {adjetivo}'

frase_resultante = frase("Nick","Duran","Smarrt😎")
print(frase_resultante)