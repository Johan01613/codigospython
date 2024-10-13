import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar datos
df = pd.read_csv('datos_estudiantes.csv')

# Crear una etiqueta binaria para aprobación
df['aprobado'] = (df['nota_final'] >= 3.0).astype(int)

# Características y etiqueta
X = df[['horas_estudio', 'asistencia']]
y = df['aprobado']

# Dividir datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar el modelo
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Predicción y evaluación
y_pred = model.predict(X_test)

# Generar matriz de confusión
conf_matrix = confusion_matrix(y_test, y_pred)

# Calcular la precisión
accuracy = accuracy_score(y_test, y_pred)

print(f'Precisión del modelo: {accuracy}')
print('Matriz de Confusión:')
print(conf_matrix)

# Visualizar la matriz de confusión
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicho')
plt.ylabel('Verdadero')
plt.title('Matriz de Confusión')
plt.show()