#creando diccionarios con dict()
diccionario = dict(nombre="Nick", apellido="dalto")


#LAS LISTAS NO PUEDEN SER CLAVES y usamos frozenset para meter conjunto
diccionario = {frozenset(["dalto","rancio"]): "jajas"}

#creando diccionarios con fromKeys() valor por defect: none
diccionario = dict.fromkeys(["nombre","apellido"])

#creando diccionarios con fromKeys() cambiando el valor por defecto 
diccionario = dict.fromkeys(["nombre","apellido"], "No se")

print(diccionario)