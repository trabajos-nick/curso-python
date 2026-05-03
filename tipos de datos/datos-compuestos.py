#creando una lista (se puede modificar)
lista = ["nick duran", "calisthenick", True, 1.85]

#creando una tupla (no se puede modificar)
tupla = ("nick duran", "calisthenick", True, 1.85)

#esto es valido
#lista[3] = "maquio"

#esto no
#tupla[3] = "maquio"

#creando un conjunto (set) (no se ccade a elementos por indice, no almacena datos suplicado)

conjunto = {"nick duran", "calisthenick",True, 1.85, "nick duran"}
#print(conjunto)

#print(conjunto[3]) -> no puede acceder al elemento

#creando un diccionario (dict) [estructura es clave : valor (key : value)]
diccionario = {
    'nombre' : 'Lucas',
    'canal' : 'calisthenick',
    'esta_ansioso': True,
    'altura' : 1.84,
    'dato_duplicado': "calisthenick"
}

print(diccionario["altura"])
print(lista[3])
