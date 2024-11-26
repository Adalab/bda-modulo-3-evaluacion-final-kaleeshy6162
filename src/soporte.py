# Importaciones necesarias:

from scipy import stats
import numpy as np




# Funciones:

#-------------------------------------------------------------------------------------------------------------------------

# Evalúa si los datos de una columna en un DataFrame siguen una distribución normal utilizando la prueba de Shapiro-Wilk

def normalidad(dataframe, columna):
    """
    Evalúa la normalidad de una columna de datos de un DataFrame utilizando la prueba de Shapiro-Wilk.
    Parámetros:
        dataframe (DataFrame): El DataFrame que contiene los datos.
        columna (str): El nombre de la columna en el DataFrame que se va a evaluar para la normalidad.
    Returns:
        None: Imprime un mensaje indicando si los datos siguen o no una distribución normal.
    """
    statistic, p_value = stats.shapiro(dataframe[columna])
    if p_value > 0.05:
        print(f"Para la columna {columna} los datos siguen una distribución normal.")
    else:
        print(f"Para la columna {columna} los datos no siguen una distribución normal.")


#-------------------------------------------------------------------------------------------------------------------------

# Evalua si las varianzas entre diferentes grupos (según una columna de categorías) son homogéneas utilizando la prueba de Levene.

def homogeneidad (dataframe, columna, columna_metrica):
    """
    Evalúa la homogeneidad de las varianzas entre grupos para una métrica específica en un DataFrame dado.
    Parámetros:
    - dataframe (DataFrame): El DataFrame que contiene los datos.
    - columna (str): El nombre de la columna que se utilizará para dividir los datos en grupos.
    - columna_metrica (str): El nombre de la columna que se utilizará para evaluar la homogeneidad de las varianzas.
    Returns:
    No devuelve nada directamente, pero imprime en la consola si las varianzas son homogéneas o no entre los grupos.
    Se utiliza la prueba de Levene para evaluar la homogeneidad de las varianzas. Si el valor p resultante es mayor que 0.05,
    se concluye que las varianzas son homogéneas; de lo contrario, se concluye que las varianzas no son homogéneas.
    """
    # lo primero que tenemos que hacer es crear tantos conjuntos de datos para cada una de las categorías que tenemos, Control Campaign y Test Campaign
    valores_evaluar = []
    for valor in dataframe[columna].unique():
        valores_evaluar.append(dataframe[dataframe[columna]== valor][columna_metrica])
    statistic, p_value = stats.levene(*valores_evaluar)
    if p_value > 0.05:
        print(f"Para la métrica {columna_metrica} las varianzas son homogéneas entre grupos.")
    else:
        print(f"Para la métrica {columna_metrica}, las varianzas no son homogéneas entre grupos.")



#-------------------------------------------------------------------------------------------------------------------------

def convertir_valores(valor):
    """
    Convierte los valores: 0 a 'yes', 1 a 'no', y deja el resto sin cambios
    Parámetros:
        valor: Valor a transformar (puede ser numérico o texto).
    Retorna:
        string: Valor transformado, o np.nan si ocurre un error.
    """
    try:
        valor_str = str(valor).strip()  # Convertir a cadena y eliminar espacios en blanco
        if valor_str == "0":  # Comparar como cadena
            return 'm'.title()
        elif valor_str == "1":  # Comparar como cadena
            return 'f'.title()
        else:
        
            return valor  # Si no es '0' ni '1', dejar el valor sin cambios
    except Exception as e:
        print(f"Error al procesar el valor {valor}: {e}")
        return np.nan  # Manejar errores con np.nan


#-------------------------------------------------------------------------------------------------------------------------

def corregir_y_minusculas(df, columna):
    # Verifica si la columna existe en el DataFrame
    if columna in df.columns:
        # Itera sobre las filas y corrige los valores
        corrected_values = []
        for value in df[columna]:
            if pd.notnull(value):  # Si el valor no es nulo
                corrected_values.append(str(value).strip().lower())  # Corrige y convierte a minúsculas
            else:
                corrected_values.append(value)  # Deja los valores nulos como están
        # Asigna los valores corregidos a la columna
        df[columna] = corrected_values
    else:
        raise ValueError(f"La columna {columna} no existe en el DataFrame.")
    return df



#-------------------------------------------------------------------------------------------------------------------------

def intervalo_confianza(dataframe, columna, nivel_confianza = float):
    """
    Calcula el intervalo de confianza para una columna específica en un DataFrame.

    Parámetros:
    -----------
    dataframe : DataFrame
        El DataFrame que contiene los datos de la muestra.
    columna : str
        El nombre de la columna para la cual deseas calcular el intervalo de confianza.
    nivel_confianza : float, opcional
        El nivel de confianza deseado para el intervalo de confianza (valor predeterminado es 0.95).

    Salida:
    -------
    None
        La función imprime en la consola la siguiente información:
        - La media muestral de la columna especificada.
        - El error estándar de la muestra.
        - El nivel de confianza utilizado.
        - El valor crítico calculado a partir de la distribución t de Student.
        - El intervalo de confianza calculado, que incluye el límite inferior y el límite superior.
    """

    # Calcular la media y el error estándar de la muestra
    media = dataframe[columna].mean()
    error = stats.sem(dataframe[columna].dropna())  # Eliminar NaN para evitar errores

    # calculamos los grados de libertad de la muestra. Recordad que debemos restar el total de datos que tenemos -1. 
    grados_libertad = len(df[columna].dropna()) - 1

    # Calcular el valor crítico (utilizando la distribución t de Student)
    valor_critico = stats.t.ppf((1 + nivel_confianza) / 2, df=grados_libertad)

    # Calcular el intervalo de confianza
    limite_inferior = media - valor_critico * error
    limite_superior = media + valor_critico * error

    print(f"Intervalo de Confianza para {columna}:")
    print(f"Media Muestral: {np.round(media, 2)}")
    print(f"Error Estándar: {np.round(error, 2)}")
    print(f"Nivel de Confianza: {nivel_confianza}")
    print(f"Valor Crítico: {np.round(valor_critico, 2)}")
    print(f"Intervalo de Confianza: ({np.round(limite_inferior)}, {np.round(limite_superior)})")