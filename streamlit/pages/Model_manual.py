from pathlib import Path

import requests
import streamlit as st


st.set_page_config(
    page_title="Prédire la pluie",
    page_icon="🌦️",
    layout="wide",
)

css_path = Path(__file__).resolve().parents[1] / "style.css"
st.markdown(
    f"<style>{css_path.read_text(encoding='utf-8')}</style>",
    unsafe_allow_html=True,
)

API_URL = "https://hr-weather-api-27658788732.europe-west1.run.app/predict"

st.title("Estimer le risque de pluie")
st.write(
    "Renseignez les conditions météo d'une journée pour estimer la probabilité "
    "de pluie le lendemain."
)
st.caption(
    "Cette estimation est issue d'un modèle expérimental et ne constitue pas "
    "une prévision météorologique officielle."
)

with st.form("weather_prediction"):
    st.subheader("pluviométrie estimée")
    temp_col1, temp_col2 = st.columns(2)
    with temp_col1:
        min_temp = st.number_input(
            "Température minimale (°C)", value=8.0, step=0.1
        )
        temp_9am = st.number_input("Température à 9 h (°C)", value=14.4, step=0.1)
    with temp_col2:
        max_temp = st.number_input(
            "Température maximale (°C)", value=24.3, step=0.1
        )
        temp_3pm = st.number_input(
            "Température à 15 h (°C)", value=23.6, step=0.1
        )

    st.subheader("Pluie et ensoleillement")
    weather_col1, weather_col2 = st.columns(2)
    with weather_col1:
        rainfall = st.number_input("Précipitations (mm)", min_value=0.0, value=0.0)
        sunshine = st.number_input(
            "Ensoleillement (heures)", min_value=0.0, max_value=24.0, value=6.3
        )
        rain_today_label = st.selectbox("A-t-il plu aujourd'hui ?", ["Non", "Oui"])
    with weather_col2:
        evaporation = st.number_input(
            "Évaporation (mm)", min_value=0.0, value=3.4
        )
        cloud_9am = st.number_input(
            "Nébulosité à 9 h (octas, de 0 à 8)",
            min_value=0,
            max_value=8,
            value=7,
        )
        cloud_3pm = st.number_input(
            "Nébulosité à 15 h (octas, de 0 à 8)",
            min_value=0,
            max_value=8,
            value=7,
        )

    st.subheader("Vent, humidité et pression")
    wind_col1, wind_col2 = st.columns(2)
    with wind_col1:
        wind_gust_speed = st.number_input(
            "Rafales de vent (km/h)", min_value=0.0, value=30.0
        )
        humidity_3pm = st.number_input(
            "Humidité à 15 h (%)",
            min_value=0.0,
            max_value=100.0,
            value=29.0,
        )
    with wind_col2:
        wind_speed_9am = st.number_input(
            "Vitesse du vent à 9 h (km/h)", min_value=0.0, value=6.0
        )
        pressure_9am = st.number_input(
            "Pression à 9 h (hPa)", min_value=0.0, value=1019.7
        )
        pressure_3pm = st.number_input(
            "Pression à 15 h (hPa)", min_value=0.0, value=1015.0
        )

    submitted = st.form_submit_button("Calculer l'estimation", type="primary")

if submitted:
    payload = {
        "MinTemp": min_temp,
        "MaxTemp": max_temp,
        "Rainfall": rainfall,
        "Evaporation": evaporation,
        "Sunshine": sunshine,
        "WindGustSpeed": wind_gust_speed,
        "WindSpeed9am": wind_speed_9am,
        "Humidity3pm": humidity_3pm,
        "Pressure9am": pressure_9am,
        "Pressure3pm": pressure_3pm,
        "Cloud9am": cloud_9am,
        "Cloud3pm": cloud_3pm,
        "Temp9am": temp_9am,
        "Temp3pm": temp_3pm,
        "RainToday": int(rain_today_label == "Oui"),
    }

    try:
        response = requests.post(API_URL, json=payload, timeout=20)
        response.raise_for_status()
        result = response.json()
    except requests.exceptions.RequestException as error:
        st.error(f"Impossible de contacter l'API météo : {error}")
    else:
        st.subheader("Résultat")
        st.metric("Risque estimé de pluie demain", f"{result['rain_probability']:.1%}")
        st.write(
            "La classe prédite par le modèle est : "
            f"**{'Pluie' if result['prediction'] == 'Yes' else 'Pas de pluie'}**."
        )
