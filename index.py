import pandas as pd
import random

# Generar datos de los estudiantes 
nombres = ['Juan', 'Ana', 'Carlos', 'Sofia', 'Diego', 'Luisa', 'Pablo', 'Marta', 'Andrés', 'Laura', 
           'Rosa', 'Miguel', 'Clara', 'Felipe', 'Lucía', 'Raúl', 'Elena', 'José', 'María', 'Tomás',
           'Javier', 'Natalia', 'Andrés', 'Victoria', 'Gabriel', 'Paula', 'Fernando', 'Isabel', 'Luis', 'Catalina']
nombres = nombres * 4  # Aumentamos la lista para que tenga 100 estudiantes

# Asegurarnos de que la longitud sea 100 estudiantes en todos los datos 
nombres = nombres[:100]

datos = {
    'nombre': nombres,
    'edad': [random.randint(18, 25) for _ in range(100)],
    'horas_estudio': [random.randint(5, 20) for _ in range(100)],
    'asistencia': [random.randint(70, 100) for _ in range(100)],
    'nota_final': [round(random.uniform(2.0, 5.0), 2) for _ in range(100)]
}

df = pd.DataFrame(datos)

# Guardardamos el DataFrame en un archivo CSV para los datos
df.to_csv('datos_estudiantes.csv', index=False)

print(df)




