
with open('archivos\\texto_de_nick.txt', 'a', encoding="UTF-8") as archivo:
    #usando un bucle para egregar varias lineas
    for i in range(5):
        archivo.write(f'linea {i+1} agregada\n')

        contenido = archivo.read(i)
