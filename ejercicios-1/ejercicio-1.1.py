curso_min = 2.5
curso_max = 7
curso_prom = 4
curso_dalto = 1.5

#Duracion de crudos
crudo_promedio = 5
crudo_dalto = 3.5

#Optimizacion del codigo:

#funcion de diferencia de duracion (A)
def dif_porcent(curso_dalto, min, max, prom):
    r1 = round(100 - curso_dalto / min * 100)
    r2 = round(100 - curso_dalto * 1000 / max / 10)
    r3 = round(100 - curso_dalto / prom * 100)
    return(r1, r2, r3)

diferencia_min, diferencia_max, diferencia_prom = dif_porcent(curso_dalto,curso_min,curso_max,curso_prom)

#funcion del tiempo removido (B)
def tim_remov(curso, crudo):
    c1 = round(100 - curso * 1000 // crudo / 10)
    return c1

vacio_prom = tim_remov(curso_prom, crudo_promedio)
vacio_dalto = tim_remov(curso_dalto, crudo_dalto)

#Mostrando las diferencias de duracion (A)
print("El curso de Dalto dura:")
print(f' - un {diferencia_min}% menos que el mas rapido')
print(f' - un {diferencia_max}% menos que el mas lento')
print(f' - un {diferencia_prom}% menos que el curso promedio')

#Mostrando la cantidad de espacios vacios que se remueven (B)
print(f'Un curso promedio elimina un {vacio_prom}% de tiempo vacio')
print(f'Este curso eliminó el {vacio_dalto}% de tiempo vacio')


#Mostrando diferencias si los cursos duraran 10 horas
print(f'ver 10 horas de este curso equivale a ver {round(curso_prom * 100 // curso_dalto / 10)} horas de otros cursos')
print(f'ver 10 horas otros cursos equivale a ver {round(curso_dalto * 100 // curso_prom / 10)} este curso')