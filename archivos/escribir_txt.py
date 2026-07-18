#sobreescribe o rcrea el archivo "txt" que mencionemos, con el permiso de "w" si no encuentra el archivo, lo crea
with open('archivos\\texto_de_nick.txt', 'w', encoding="UTF-8") as archivo:
    #sobreescribiendo el archivo
    #archivo.write("Jajajajajaj te asustasteee")

    #agregando 2 lineas con writelines
    archivo.writelines(["Hola cagon como tas\n", "penelope \n"])

    #agregando otras 2 lineas
    archivo.writelines(["me gusta la polla\n", "penelope"])