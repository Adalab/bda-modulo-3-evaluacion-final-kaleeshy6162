import pandas as pd
from src import soporte as sp
import matplotlib.pyplot as plt
import seaborn as sns

#---------------------------------------------------------------------------

# Lectura de .csv:

df1 = pd.read_csv("data/Customer Flight Activity.csv")
df2 = pd.read_csv("data/Customer Loyalty History.csv")

#---------------------------------------------------------------------------
# Analisis de los Datos Customer Flight Analysis(df1):

print(df1.head())

print("---------------------------------------------------------------------------")

# Cantidad de columnas y filas en df1.

print(f"En este DataFrame hay: {df1.shape[0]} filas y {df1.shape[1]} columnas.")

print("---------------------------------------------------------------------------")

# Info df1

print("Customer Flight Analysis Info:")
print(df1.info())

print("---------------------------------------------------------------------------")

# Resumen estadistico de columnas numericas

print("Customer Flight Analysis Resumen de Estadistica:")
print(df1.describe())

print("---------------------------------------------------------------------------")

# Identificar valores nulos

print("Valores nulos en Customer Flight Analysis:")
print(df1.isnull().sum())

print("---------------------------------------------------------------------------")

# Identificar valores duplicados

print("Valores duplicados en Customer Flight Analysis:")
print(df1.duplicated().sum())

print("---------------------------------------------------------------------------")

# Analisis de los Datos Customer Flight Analysis(df2):

print(df2.head())

print("---------------------------------------------------------------------------")

# Cantidad de columnas y filas en df1.

print(f"En este DataFrame hay: {df2.shape[0]} filas y {df2.shape[1]} columnas.")

print("---------------------------------------------------------------------------")

# Info df2.

print("Customer Loyalty History Info:")
print(df2.info())

print("---------------------------------------------------------------------------")

# Resumen estadistico de columnas numericas

print("Customer Loyalty History Resumen de Estadistica:")
print(df2.describe())

print("---------------------------------------------------------------------------")

# Identificar valores nulos

print("Valores nulos en Customer Loyalty History:")
print(df2.isnull().sum())

print("---------------------------------------------------------------------------")

# Identificar valores duplicados

print("Valores duplicados en Customer Loyalty History:")
print(df2.duplicated().sum())

print("---------------------------------------------------------------------------")

# UNION DE TABLAS: INNER JOIN 

# Utilizo INNER JOIN, combina registros de ambas tablas solo cuando existe una correspondencia exacta en la clave común (en este caso, Loyalty Number).                                               
# Te asegura que solo mantendrás clientes que aparecen en ambos conjuntos de datos.
# Ayuda a eliminar duplicados si hay registros redundantes en cualquiera de las tablas.
# Si hay filas con valores faltantes en la clave Loyalty Number, esas filas serán descartadas automáticamente.

union_df = pd.merge(df1, df2, on="Loyalty Number", how="inner")
print(union_df.head())

print("---------------------------------------------------------------------------")

# Cantidad de columnas y filas de union_df.

print(f"En este DataFrame hay: {union_df.shape[0]} filas y {union_df.shape[1]} columnas.")

print("---------------------------------------------------------------------------")

# Identificar valores nulos.

print(union_df.isna().sum())

print("---------------------------------------------------------------------------")

# Info union_df.

union_df.info()

print("---------------------------------------------------------------------------")

# Verificacion de la distribucion Normal.

