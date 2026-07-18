#importando un modulo y asignandole el nombre "m_saludar"
#import mudulo_saludar as m_saludar

#desde ese modulo, importamos dos funciones y les cambiamos el nombre
from modulo_saludar import saludar,saludar2 as saludar_como_coscu

#creamos las variables con los saludos
saludo = saludar("Nick")
saludo_raro = saludar_como_coscu("Frank")

#mostrando los resultados
print(saludo)
print(saludo_raro)

#para ver las propiedades y metodos de el namespace
#print(dir(m_saludar))

#accedemos al nombre este modulo
print(__name__)

#accedemos al nombre del modulo llevado
#print(m_saludar.__name__)

