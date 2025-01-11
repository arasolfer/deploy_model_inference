import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from src.data.data_preprocessor import preprocess_data
from src.model.model_loader import load_model
import pandas as pd
import joblib

def main():
    # ruta del modelo y scaler 
    model_path = "models/trained_model_2025-01-11.joblib"
    scaler_path = "models/scaler.pkl"
    
    # cargar el modelo
    model = load_model(model_path)
    
    # cargar el escalador
    if not scaler_path or not joblib.os.path.exists(scaler_path):
        raise FileNotFoundError(f"No se encontró el archivo del escalador: {scaler_path}")
    scaler = joblib.load(scaler_path)
    
    # datos de entrada
    input_data = {
        "Pregnancies":6,
        "Glucose":148,
        "BloodPressure":72,
        "SkinThickness":35,
        "Insulin":90,
        "BMI":33.6,
        "DiabetesPedigreeFunction":0.627,
        "Age":50
    }
    
    # convertir los datos a DataFrame
    df_input = pd.DataFrame([input_data])
    
    # aplicar el preprocesamiento y escalamiento de datos
    df_input = preprocess_data(df_input, scaler)
    
    # realizar la predicción
    try: 
        prediction = model.predict(df_input)
        print(f"Predictions: {prediction}")
    except Exception as e:
        print(f"Error running inference: {e}")
        sys.exit(1)
    
    # mostrar el resultado
    outcome = "Diagnostico de diabetes positivo" if prediction[0] == 1 else "Diagnostico de diabetes negativo"
    print(f"Resultado de la predicción: {outcome}")


if __name__ == "__main__":
    main()