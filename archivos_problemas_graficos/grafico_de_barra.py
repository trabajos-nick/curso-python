import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos_problemas_graficos\\cofla_ingresos.csv")
print(df)

#creando el grefico
sns.barplot(x="fuente",y="ingresos",data=df)

#mostrando el total
total_ingresos = df['ingresos'].sum()

print(f'El total de ingresos es de: ${total_ingresos} USD')

#mostrando graficos
plt.show()