
#importando un modulo dese una carpeta externa
import sys

sys.path.append("C:\\Users\\Nick\\Desktop\\curso de python nick\\modulos")

import modulo_calc as calcular

print(calcular)

#importando un modulo desde la misma carpeta
import modulo_ejercicio as mayoria_edad

print(mayoria_edad)

#intentando modificar variables de los modulos ya creados

from edad import edad, edad2 as respuesta_graciosa

edad_a = edad(mayoria_edad)
edad_b = respuesta_graciosa(edad)

print(edad_a)
print(edad_b)
