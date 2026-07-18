#acmbiar el tipo de datos de una columna
import pandas as pd
df = pd.read_csv("archivos_problemas\\datos.csv")

#convertir a string los datos de una columna
df['edad'] = df['edad'].astype(str)

#mostran el tipo de dato del primer elemenro de la columna edad
#print(type(df['edad'][0]))

#reemplazando los datos "dalto" por "maestro"
df['apellido'].replace("Nick","maestro",inplace=True)

#eliminando las filas con datos faltantes
df = df.dropna()

#eliminando las filas repetidas
df = df.drop_duplicates()

#creando un CSV con el dataframe resultante (limpio)
df.to_csv("archivos_problemas\\datos_limpios.csv")
