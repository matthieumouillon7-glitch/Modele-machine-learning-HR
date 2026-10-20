import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date
from pathlib import Path

app = FastAPI()

api_folder = Path(__file__).parent
project_folder = api_folder.parent.parent
artifacts_path = project_folder / "streamlit" / "Modèle" / "weather_artifacts.joblib"

artifacts = joblib.load(artifacts_path)
model = artifacts["model"]  # ✅ SEULEMENT ce qui existe

class PredictionInput(BaseModel):
    nom_usuel: str
    ds: date

@app.post("/predict")
def predict(data: PredictionInput):
    future = pd.DataFrame({"ds": [pd.Timestamp(data.ds)]})
    forecast = model.predict(future).iloc[0]
    return {
        "nom_usuel": data.nom_usuel,  # ✅ Minuscules
        "ds": data.ds.isoformat(),
        "yhat": float(forecast["yhat"]),
        "yhat_lower": float(forecast["yhat_lower"]),
        "yhat_upper": float(forecast["yhat_upper"]),
    }
    
# NOTES
# docker rm -f weather-api-container
# docker build -t weather-api .
# docker run -p 8080:8080 -d --name weather-api-container weather-api
# -t Tag : Nom de l'image
# -p Port ex 8080:8080
#-d #Detached : Mode arrière-plan
  