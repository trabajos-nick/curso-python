#sistema de BIBLIOTECA PERSONAL 'LA TACITURNA'
#1. REGISTRO DEL LECTOR----------------------------------

usuario_nombre = input("Escribe tu nombre mi Rey: ")
usuario_edad =  int(input("Dame la edad: "))

#print (usuario_nombre)
#print(usuario_edad)


lector = {
    "nombre": (usuario_nombre),
    "edad" : (usuario_edad),
    "libros_leidos" : 0,
    "es_premium" : False
}

#2.CATALOGO DE LIBROS----------------------------
#LISTA DE LIBROS
mis_libros = list(["padre rico padre pobre", "no puedes lastimarme", "el arte de la seducción"])

datos_biblioteca = ("LA TACITURNA", 2026, "Mosquera")
generos = {'psicologia','finanzas','ciencias'} 

print(f'Biblioteca {datos_biblioteca}, | Géneros: {generos}') 

#AGREGANDO UN LIBRO A LA LISTA
libro_agg = input("Agrega un libro nuevo: " )

titulo_mod = libro_agg.upper().lower()
mis_libros.append(titulo_mod)

#3. ANALISIS DEL TITULO----------------------------------

#CONTANDO LOS LIBROS Y ORDENANDOLOS ALFABETICAMENTE
cantidad_libros = len(mis_libros)
mis_libros.sort()

#CONTANDO LAS PALABRAS DEL LIBROS
palabra_libro = len(libro_agg.split(" "))

#verificando si empieza con el
empieza_con =  libro_agg.startswith("El")

#reemplazando con guiones bajos (_)
nombre_archivo = libro_agg.replace(" ","_")


#print (f'Bienvenido/a, {usuario_nombre}! Tienes {usuario_edad} años de edad')

print (f'Titulo en minusculas: {titulo_mod}')
print(f'Cantidad de palabras: {palabra_libro}')
print(f'Palabras: {palabra_libro} - Caracteres: {len(libro_agg)}')
print(f'Empieza con "El": {empieza_con}')
print(f'Nombre de archivo: {nombre_archivo}')

#4.OPERADORES Y COMPARACIONES
#4.1.cuantos libros lleva el usuario
contador_libros_leidos =  int(input("cuantos libros leiste este año: "))
lector["libros_leidos"] = contador_libros_leidos

lectura_por_5años = contador_libros_leidos * 5
lectura_por_meses = contador_libros_leidos * 5 // 12
libros_sobrantes_por_mes = contador_libros_leidos % 60

print(f'Si leyeras con  la misma constancia durante 5 años, leerias: {lectura_por_5años} libros')
print(f'La cantidad de libros leidos a esta contancia por mes seria de: {lectura_por_meses} libros')
print(f'Le quedaron estos libros por leer este mes:  {libros_sobrantes_por_mes}')

#4.2operadores con comparacion
leyo_mas_de_12 = lector["libros_leidos"] > 12
leyo_0 = lector["libros_leidos"] == 0

#
print(f'¿Leyó más de 12 libros este año? {leyo_mas_de_12}')
#¿Leyó exactamente 0?
print(f'¿Leyó exactamente 0? {leyo_0}')

#4.2 operadores logicos
pregunta1 = (usuario_edad <= 18) & (lector["libros_leidos"] > 5)
print(f'¿Es mayor de 18 Y leyó más de 5 libros? {pregunta1}')

pregunta2 = (usuario_edad < 15) | (lector["libros_leidos"] > 20)
print(f'¿Es menor de 15 O leyó más de 20 libros? {pregunta2}')

#5 Sistema de membresia
#Nivel lector

if lector["libros_leidos"] > 20:
    print(f'Felcidades{lector["nombre"]}, eres un Lector experto')

elif lector["libros_leidos"] > 15:
    if lector["edad"] >= 18:
        lector["es_premium"] = True
        print("¡Membresia premium activada!")
    else:
        print(f"Membresia juvenil activada")
    print(f'En hora buena {lector["nombre"]}, eres un Lector habitual')

elif lector["libros_leidos"] > 10:
    print(f'En hora buena {lector["nombre"]}, eres un Lector habitual')

elif lector["libros_leidos"] > 0:
    print(f'Bueno... {lector["nombre"]}, al menos eres un Lector ocasional')

else:
    print(f"Hay que leer 🙄,te quedan {16 - lector['libros_leidos']} libros por leer, tener 18 años y tener premium si deseas activar la membresia")

#verificacion y final
print(libro_agg in mis_libros)

print(f'Nombre: {lector["nombre"]}')
print(f'Edad: {lector["edad"]}')
print(f'Libros leidos: {lector["libros_leidos"]}')
print(f'Es premium: {lector["es_premium"]}')









