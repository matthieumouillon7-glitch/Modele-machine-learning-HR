import streamlit as st
import pandas as pd
import httpx
from datetime import date, timedelta  # ← Ajout de timedelta
import plotly.express as px

# 1. Sélection
selected_station = st.selectbox("Station", ["PARIS-MONTSOURIS"])
selected_date = st.date_input(
    "Sélectionnez une date",
    value=date.today() + timedelta(days=365)  # ✅ Correction syntaxe
)

# 2. Appel API et graphique
from datetime import timedelta

if st.button("Générer le graphique"):
    try:
        # 1. Créer 30 dates consécutives
        future_dates = [selected_date + timedelta(days=i) for i in range(30)]

        # 2. Prédire pour chaque date
        results = []
        for d in future_dates:
            response = httpx.post(
                "http://localhost:8080/predict",
                json={"nom_usuel": selected_station, "ds": d.isoformat()}
            )
            if response.status_code == 200:
                results.append(response.json())

        # 3. Créer DataFrame
        chart_data = pd.DataFrame(results).rename(columns={
            "ds": "Date du mariage",
            "yhat": "Prévision centrale (mm)",
            "yhat_lower": "Borne basse (mm)",
            "yhat_upper": "Borne haute (mm)"
            })
    

        # 4. Afficher
        fig = px.line(
            chart_data,
            x="Date du mariage",
            y=["Prévision centrale (mm)", "Borne basse (mm)", "Borne haute (mm)"],
            title="Prévision sur 30 jours"
           )
        st.plotly_chart(fig)

    except Exception as e:
        st.error(f"Erreur: {str(e)}")