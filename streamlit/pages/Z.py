import streamlit as st
from pathlib import Path
from openai import OpenAI, OpenAIError

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
st.write("Posez une question sur la préparation météo de votre mariage.")

# MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation', 'Sunshine',
#        'WindGustDir', 'WindGustSpeed', 'WindDir9am', 'WindDir3pm',
#        'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am', 'Humidity3pm',
#        'Pressure9am', 'Pressure3pm', 'Cloud9am', 'Cloud3pm', 'Temp9am',
#        'Temp3pm', 'RainToday', 'RISK_MM', 'RainTomorrow'

import streamlit as st

start_number, end_number = st.select_slider(
    "Choisir la plage de température minimale (°C) pour votre mariage",
    
    MinTemp=(0, 20),
        
)
st.write("Choisir", start_number, "and", end_number)

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