import re

texto = '''hola papi. esta es la cadena 1145531. como estais?
esta es la segunda  linea de texto 2.
y la tercera es la vencida 3'''

#Haciendo una bisqueda simple
#resultado = re.findall("la", texto)

#\d -> busca digitos numericos del 0 al 9
#resultado = re.findall(r"\d",texto)

#\D -> busca TODO MENOS digitos numericos del 0 al 9 
#resultado = re.findall(r"\D",texto)

#\w -> busca caracteres  alfanumericos [a-z A-Z 0-9 _] 
#resultado = re.findall(r"\w",texto)

#\W -> busca TODO MENOS caracteres  alfanumericos [a-z A-Z 0-9 _] 
#resultado = re.findall(r"\W",texto)

#\s -> busca espacios en blanco -> espacios, tabs, saltos de linea etc
#resultado = re.findall(r"\s",texto)

#\S -> busca TODO MENOs espacios en blanco -> espacios, tabs, saltos de linea etc
#resultado = re.findall(r"\S",texto)

#. ->busca TODO MENOS saltos en linea
#resultado = re.findall(r".",texto)

#\n ->busca saltos en linea
#resultado = re.findall(r"\n",texto)

#\ -> cancelar caracteres especiales, cancelando la funcion del punto y buscando puntos
#resultado = re.findall(r"\.",texto)

#armando una cadena que busque un nnumero seguido de un texto, seguido de un punto y un espacio
#resultado = re.findall(f'\d\.\s' ,texto)

#^ -> busca el comienzo de una linea
#flags=re.M activa la multilia
#resultado = re.findall(f'^esta',texto,flags=re.M)

#$ -> busca el final de una linea
#resultado = re.findall(f'3$',texto,flags=re.M)

#{n} -> busca n cantidad de veces el valor de la izquierda
#resultado = re.findall(r'\d{3}',texto)

#{n,m} -> al menos n, como maximo m
resultado = re.findall(r'\d{2,4}',texto)

# | -> busca una cosa o la otra
resultado = re.findall(r'\d{2,4}|Hola',texto)


print(resultado)