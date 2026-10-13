import streamlit as st
from pathlib import Path

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

st.title("Assistant météo")
st.write("Vous avez choisi l'option manuelle - définissez les paramètres.")

# MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation', 'Sunshine',
#        'WindGustDir', 'WindGustSpeed', 'WindDir9am', 'WindDir3pm',
#        'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am', 'Humidity3pm',
#        'Pressure9am', 'Pressure3pm', 'Cloud9am', 'Cloud3pm', 'Temp9am',
#        'Temp3pm', 'RainToday', 'RISK_MM', 'RainTomorrow'

import streamlit as st

start, end = st.select_slider(
    "Choisir la plage de température minimale (°C) pour votre mariage",
    options=range(0, 21),
    value=(0, 20),
)

st.write("Plage choisie :", start, "à", end, "°C")

start, end = st.select_slider(
    "Choisir les précipitations",
    options=range(0, 100),
    value=(0, 20),
)

st.write("Plage choisie :", start, "à", end, "°C")

start, end = st.select_slider(
    "Evaporation",
    options=range(0, 100),
    value=(0, 20),
)

st.write("Plage choisie :", start, "à", end, "°C")

start, end = st.select_slider(
    "Ensoleillement",
    options=range(0, 100),
    value=(0, 20),
)

st.write("Plage choisie :", start, "à", end, "°C")

start, end = st.select_slider(
    "Direction du vent (rotation)",
    options=range(0, 100),
    value=(0, 20),
)
st.write("Plage choisie :", start, "à", end, "°C")


start, end = st.select_slider(
    "WindGustDir9",
    options=range(0, 100),
    value=(0, 20),
)
st.write("Plage choisie :", start, "à", end, "°C")

start, end = st.select_slider(
    "WindGustDir3",
    options=range(0, 100),
    value=(0, 20),
)
st.write("Plage choisie :", start, "à", end, "°C")

start, end = st.select_slider(
    "WindSpeed9",
    options=range(0, 100),
    value=(0, 20),
)
st.write("Plage choisie :", start, "à", end, "°C")

start, end = st.select_slider(
    "WindSpeed3",
    options=range(0, 100),
    value=(0, 20),
)
st.write("Plage choisie :", start, "à", end, "°C")

start, end = st.select_slider(
    "Pressure9",
    options=range(0, 100),
    value=(0, 20),
)
st.write("Plage choisie :", start, "à", end, "°C")

start, end = st.select_slider(
    "Pressure3",
    options=range(0, 100),
    value=(0, 20),
)
st.write("Plage choisie :", start, "à", end, "°C")

start, end = st.select_slider(
    "Cloud9",
    options=range(0, 100),
    value=(0, 20),
)
st.write("Plage choisie :", start, "à", end, "°C")

start, end = st.select_slider(
    "Cloud3",
    options=range(0, 100),
    value=(0, 20),
)
st.write("Plage choisie :", start, "à", end, "°C")

start, end = st.select_slider(
    "Temp9",
    options=range(0, 100),
    value=(0, 20),
)
st.write("Plage choisie :", start, "à", end, "°C")

start, end = st.select_slider(
    "Temp3",
    options=range(0, 100),
    value=(0, 20),
)
st.write("Plage choisie :", start, "à", end, "°C")

start, end = st.select_slider(
    "Rain_Today",
    options=range(0, 100),
    value=(0, 20),
)
st.write("Plage choisie :", start, "à", end, "°C")

# MaxTemp=(20, 40),
#     Rainfall=(0, 100),
#     Evaporation=(0, 10),
#     Sunshine=(0, 15),
#     WindGustDir=(0, 360),
#     WindGustSpeed=(0, 100),
#     WindDir9am=(0, 360),
#     WindDir3pm=(0, 360),
#     WindSpeed9am=(0, 100),
#     WindSpeed3pm=(0, 100),
#     pressure9am=(950, 1050),
#     Pressure3pm=(950, 1050),
#     Cloud9am=(0, 8),
#     Cloud3pm=(0, 8),
#     Temp9am=(0, 40),
#     Temp3pm=(0, 40),
#     RainToday=(0, 1)  