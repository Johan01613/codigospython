# importamos las librerias de scikit- learm
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Cargar datos
df = pd.read_csv('datos_estudiantes.csv')

# Seleccionar características para el clustering
X = df[['horas_estudio', 'asistencia']]

# Aplicar KMeans
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

# Asignar clusters
df['cluster'] = kmeans.labels_

# Visualizar los clusters
plt.scatter(df['horas_estudio'], df['asistencia'], c=df['cluster'], cmap='viridis')
plt.xlabel('Horas de Estudio')
plt.ylabel('Asistencia')
plt.title('Clustering de Estudiantes')
plt.show()
