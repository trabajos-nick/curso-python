diccionario = {
    "nombre": "Juan",
    "apellido": "Pérez",
    "subs": 999999
}

#nos devuelve un objeto dict_item
claves = diccionario.keys()

#obteniendo un elemento con get() si no encuentra nada el programa continua
valor_de_jdie = diccionario.get("hbhb", "El programa continua") 

#eliminando todo del diccionario
#diccionario.clear()

#eliminanado un objeto del dicccionario
diccionario.pop("nombre")

#obteniendo un elemento dic_items iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)