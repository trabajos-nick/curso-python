#abrumos el archivo with open
with open("archivos\\texto_de_nick.txt") as archivo:

    #leemos el archivo
    contenido = archivo.read()

    #mostramos elarchivo
    print(contenido)

#no es necesario cerrarlo al usar with open