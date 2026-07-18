import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos_problemas_graficos\\pedos.csv")
print(df)

#creando el grefico
sns.lineplot(x="fecha",y="pedos",data=df)

#creando el punto en el momento de mas pedos
plt.plot("03-12",20,"o")

#mostrando graficos
plt.show()