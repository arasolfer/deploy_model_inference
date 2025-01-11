import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib

def preprocess_data(df: pd.DataFrame, scaler: StandardScaler) -> pd.DataFrame:
    """
    Realiza el preprocesamiento de los datos de entradas:
    - Imputa valores faltantes y reemplaza valores extremos en las variables numéricas.
    - Escala las variables numéricas utilizando el escalador proporcionado.

    Args:
        df (pd.DataFrame): Datos a procesar.
        scaler (StandardScaler): El escalador previamente entrenado.

    Returns:
        pd.DataFrame: Datos procesados y escalados.
    """
    # Imputación y limpieza de valores
    df['BloodPressure'] = df['BloodPressure'].replace(
        0, df[df['BloodPressure'] > 0]['BloodPressure'].mean()
    )
    df['Glucose'] = df['Glucose'].replace(
        0, df[df['Glucose'] > 0]['Glucose'].mean()
    )
    df['SkinThickness'] = df['SkinThickness'].replace(
        0, df[df['SkinThickness'] > 0]['SkinThickness'].mean()
    )

    # Limpiar valores de skin thickness
    mean_skin_thickness = df[df['SkinThickness'] <= 90]['SkinThickness'].mean()
    df.loc[df['SkinThickness'] > 90, 'SkinThickness'] = mean_skin_thickness
    mean_skin_thickness = df[df['SkinThickness'] >= 10]['SkinThickness'].mean()
    df.loc[df['SkinThickness'] < 10, 'SkinThickness'] = mean_skin_thickness

    df['Insulin'] = df['Insulin'].replace(
        0, df[df['Insulin'] > 0]['Insulin'].median()
    )
    df['BMI'] = df['BMI'].replace(
        0, df[df['BMI'] > 0]['BMI'].mean()
    )

    # Limpiar valores de BMI
    mean_bmi2 = df[df['BMI'] <= 60]['BMI'].mean()
    df.loc[df['BMI'] > 60, 'BMI'] = mean_bmi2
    
    # Escalamiento de las variables numéricas
    numeric_cols = ["BloodPressure", "Glucose", "SkinThickness", "Insulin", "BMI"]
    df[numeric_cols] = scaler.transform(df[numeric_cols])
    
    return df
