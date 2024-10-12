# importamos las librerias de scikit- learm
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Cargamos los  datos de nuestros datos estudiantes 
df = pd.read_csv('datos_estudiantes.csv')

X = df[['horas_estudio', 'asistencia']]
y = df['nota_final']

# Dividir datos en entrenamiento y test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenarmos el modelo
model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, y_train)

# Predicción y evaluación
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)

print(f'Precicion del modelo: {mse}')


