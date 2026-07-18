import pandas as pd

#usando la funcion "read_csv" para leer el archivo
df = pd.read_csv("archivos\\datos.csv")
df2 = pd.read_csv("archivos\\datos.csv")

nombres = df["nombre"]
#cadena = "0123456789"

#usando slicing para cceder a una cadena numerica
#print(cadena[2:7])
df_ordenado_ascendente = df.sort_values("edad")

#ordenandolo de forma descendente
df_ordenado_descendente = df.sort_values("edad", ascending=False)

#concatenando los 2 dataframes
df_concatenando = pd.concat([df,df2])

#accediendo a lars primeras 2 filas con  head()
primer_fila = df.head(2)

#accedienfo a las ultimas 2 filas com tail()
ultima_fila = df.tail(2)

#accediendo a la cantidad de dilas y columnas con shape
filas_totales,columnas_totales = df.shape

#obteniendo data estadistica del dataframe:
df_info = df.describe()

#accediendo a la edad de la fila 2
elemento_especifico_loc = df.loc[2,"edad"]

#accediendo a la edad de la dila 2 con iloc
elemento_especifico_loc = df.iloc[2,2]

#accediendo a todas las filas de una columna
apellido = df.iloc[:,1]

#accediendo a la fila 3 con loc
fila_3 = df.loc[2,:]

#accediendo a la fila 3 con iloc
fila_3 = df.iloc[2,:]

#accediendo a filas con edad mayor que 40
mayor_que_30 = df.loc[df["edad"]<30,:]

print(mayor_que_30)


