import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field
from pathlib import Path


app = FastAPI()


class WeatherInput(BaseModel):
    MinTemp: float
    MaxTemp: float
    Rainfall: float
    Evaporation: float
    Sunshine: float
    WindGustSpeed: float
    WindSpeed9am: float
    Humidity3pm: float
    Pressure9am: float
    Pressure3pm: float
    Cloud9am: float
    Cloud3pm: float
    Temp9am: float
    Temp3pm: float
    RainToday: int = Field(ge=0, le=1)


# Le dossier contenant main.py est .streamlit/api. __file__ est une variable spéciale 
# fournie par Python. Elle contient le chemin du fichier qui est en train de s’exécuter. 
# Ici, c’est main.py
api_folder = Path(__file__).parent
# En remontant de deux dossiers, on revient à la racine du projet.
project_folder = api_folder.parent.parent
# Depuis la racine, on rejoint le **dossier** qui contient le modèle sauvegardé.
artifacts_path = (
    project_folder
    / "streamlit"
    / "Modèle"
    / "weather_artifacts.joblib"
)
artifacts = joblib.load(artifacts_path)
preprocessor = artifacts["preprocessor"]
model = artifacts["model"]


@app.get("/")
def read_root():
    return {"message": "Weather prediction API is running"}


@app.post("/predict")
def predict(data: WeatherInput):
    features = pd.DataFrame([data.model_dump()])
    transformed = pd.DataFrame(
        preprocessor.transform(features),
        columns=model.feature_names_in_,
    )
    prediction = int(model.predict(transformed)[0])
    probabilities = model.predict_proba(transformed)[0]
    class_probabilities = {
        str(label): float(probability)
        for label, probability in zip(model.classes_, probabilities)
    }

    return {
        "prediction": "Yes" if prediction == 1 else "No",
        "rain_probability": class_probabilities["1"],
        "class_probabilities": class_probabilities,
    }