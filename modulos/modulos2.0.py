#si el modulo estuviera dentro de una carpeta
#import funciones_buenas.saludar as m_saludar

import sys

sys.path.append("C:\\Users\\Nick\\Desktop\\curso de python nick\\funciones_buenas")
print(sys.path) 

import saludar as modulo_saludo

print(modulo_saludo.saludar("Nick"))