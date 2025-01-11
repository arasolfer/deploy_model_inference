import joblib 

def load_model(model_path:str) -> object:
    
    """
    Carga el modelo desde un path especificado
    
    Args:
        model_path (str): Path donde se encuentra guardado el archivo generado por el modelo.
        
    Returns:
        El modelo cargado
    """
    
    try:
        model = joblib.load(model_path)
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        raise e 