#creando mi propia excepcion personalizada
class MiExcepcion(Exception):
    def __init__(sef,err):
        print(f"Impresionante, cometiste el siguiente error: {err}")

#Lanzando mi propia excepcion
#raise MiExcepcion("Jjajajajaja, pelotudo")

#manejandola
try:
    raise MiExcepcion("Jjajajajaja, pelotudo")
except:
    print("como vas a cometer esa cagada")