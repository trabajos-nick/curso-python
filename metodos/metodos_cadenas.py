cadena1 = "Hola perrota"
cadena2 = "Hola,Terian,Hp"

#convierte a mayuscula
mayus = cadena1.upper()

#convierte a minuscula
minus = cadena1.lower()

#primera en mayuscula
capt = cadena1.capitalize()

#buscamos una cadena en otra cadena, si no coincidencias hay devuelve -1
busqueda_find =cadena2.find("a")

#buscamos una cadena en otra cadena, si no coincidencias hay devuelve una excepción
busqueda_find =cadena2.index("a")

#si es numerico, devuelve true si no, false
es_numerico = cadena1.isnumeric()

#si es alfanumerico, devuelve true, de lo contrario false
es_alfanumerico = cadena2.isalpha()

#buscamos una cadena en otra cadena, devuelve la cantidad de veces que coincida
contar_coincidencias = cadena2.count("Terian")

#contamos los caracteres de una cadena (es una funcion no eun metoso)
contar_caracteres = len(cadena1)

#verificamos su una cadena empieza con otra cedena dada, si es as devuelve true
empieza_con = cadena1.startswith("H")

#verificamos su una cadena termina con otra cedena dada, si es as devuelve true
termina_con = cadena1.endswith("Hola")

#reemplaza un pedazo de la cadena dada, por otra dada
cadena_nueva = cadena2.replace(","," ")

#separara cadenas con la cadena que le damos(DEVULEVE MATRIZ, OSEA LISTA)
cadena_separada = cadena2.split(",")

print (cadena_separada[2])
