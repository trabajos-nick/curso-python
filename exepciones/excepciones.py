#creando funcion que suma numeros
def sumar_dos():
    #iniciando un bucle
    while True:
        #pidiendo numeros
        a = input("Numero 1: ")
        b = input("Numero 2: ")
        #intentando convertirlos a entero y sumarlos
        try:
            resultado = int(a) + int(b)
        #si lanzo una excepcion, pedirle que ingrese los datos
        except ValueError as e:
            print("le pedi un numero agüevado, no se haga")
            print(f"ERROR: {e}")
        #si todo salio bien el bucle
        else:
            break
        #finally se ejecuta siempre
        finally:
            print("esto se ejecuta soiempre")
    #mostrando el resultado    
    return resultado

print(sumar_dos())