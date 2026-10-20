"""User manual for the Meteo-France/Prophet model and chart examples."""

from datetime import date
from pathlib import Path
import joblib
import pandas as pd
import streamlit as st
import httpx


# Page configuration
st.set_page_config(
    page_title="Manuel du modèle météo",
    page_icon="🌦️",
    layout="wide",
)

# Load CSS
css_path = Path(__file__).parent / "style.css"
if css_path.exists():
    st.markdown(
        f"<style>{css_path.read_text(encoding='utf-8')}</style>",
        unsafe_allow_html=True,
    )

# Data paths
DATA_PATH = (
    Path(__file__).parent
    / "Modèle"
    / "Data"
    / "Q_75_previous-1950-2024_RR-T-Vent.csv"
)
ARTIFACT_PATH = (
    Path(__file__).parent / "Modèle" / "weather_artifacts.joblib"
)


@st.cache_resource
def load_model():
    """Load the model artifact."""
    if ARTIFACT_PATH.exists():
        artifacts = joblib.load(ARTIFACT_PATH)
        return artifacts["model"]
    return None


@st.cache_data
def load_station_names() -> list[str]:
    """Return station names from the notebook's NOM_USUEL column."""
    if not DATA_PATH.exists():
        return []

    stations = pd.read_csv(
        DATA_PATH,
        sep=";",
        usecols=["NOM_USUEL"],
        encoding="utf-8-sig",
    )["NOM_USUEL"].dropna()
    return sorted(stations.astype(str).str.strip().unique().tolist())


def show_prediction_manual() -> None:
    st.header("1. Choisir une station et consulter une prédiction")
    st.markdown(
        "Cette partie reprend le cheminement du notebook "
        "`model_meteofrance.ipynb` : la série est filtrée avec `NOM_USUEL`, "
        "puis Prophet produit une prévision pour la date choisie."
    )

    stations = load_station_names()
    if not stations:
        st.error(f"La liste des stations est introuvable : `{DATA_PATH}`")
        return

    selected_station = st.selectbox(
        "Station (`NOM_USUEL`)",
        stations,
        index=(
            stations.index("PARIS-MONTSOURIS")
            if "PARIS-MONTSOURIS" in stations
            else 0
        ),
    )
    selected_date = st.date_input(
        "Date à prévoir",
        value=date(date.today().year + 1, 1, 1),
        min_value=date.today(),
        format="DD/MM/YYYY",
    )

    st.caption(
        "La station sélectionnée est conservée dans le résultat sous `NOM_USUEL`. "
        "Le fichier d'artifact actuel contient le modèle entraîné dans le notebook."
    )

    if st.button("Calculer la prédiction", type="primary"):
        try:
            response = httpx.post(
                "http://localhost:8080/predict",
                json={"nom_usuel": selected_station, "ds": selected_date.isoformat()}
            )
            if response.status_code == 200:
                result = response.json()
                st.subheader("Résultat")
                value_col, low_col, high_col = st.columns(3)
                value_col.metric("Prévision", f"{result['yhat']:.2f} mm")
                low_col.metric("Borne basse", f"{result['yhat_lower']:.2f} mm")
                high_col.metric("Borne haute", f"{result['yhat_upper']:.2f} mm")
            else:
                st.error(f"Erreur: {response.text}")
        except Exception as e:
            st.error(f"Connexion échouée: {str(e)}")


# Load model (optional, can be used for local predictions)
model = load_model()

# Show the interface
show_prediction_manual()
