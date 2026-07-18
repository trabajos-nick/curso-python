'''
#creando una funcion simple
def saludar():
    print("Hola Nick, trabajando duro?")

#ejecutando la funcion simple
saludar()
'''

#creando una funcion con parametro 
def saludar(nombre,sexo):
    sexo = sexo.lower()
    if(sexo == "mujer"):
        adjetivo = "reina"
    elif(sexo == "hombre"):
        adjetivo = "Titan"
    else:
        adjetivo = 'master'
    print(f'Hola {nombre}, mi {adjetivo} ¿como estas?')

saludar("Camila","Mujer")
saludar("Nick", "Hombre")
saludar("Andres","no binario")

#crear una funcion que nos retorne valores
def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña,num

#desempaquetando la funcion
contraseña,primer_numero = crear_contraseña_random(560)

#mostrando los resultados obtenidos y los datos utilizados
print(f'Tu contraseña nueva es: {contraseña}')
print(f"El numero utilizado para crearla fue: {primer_numero}")
