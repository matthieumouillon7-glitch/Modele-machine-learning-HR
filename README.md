# MODELE DE MACHINE LEARNING EN RH

#**MODELE DE MACHINE LEARNING EN HR - CAS D'USAGE**
**

#**Introduction** 🤖
#Bonjour, ceci est un repository avec un modèle de **machine learning en python.**

#**Modèle** 🔢
#Le modèle utilisé est un modèle dit supervisé de régression logistique

#**Utilisation** 🛠️
#Ce modèle permet de **prédire** la possibilité qu'il **pleuve** le jour de son mariage

## Application Streamlit

L'application météo se trouve hébergée sur streamlit cloud 
la page de front est développée en stream lit
les cascing style sheet et les st.key proviennent d'un fichier CSS
Le modèle est développé en Python
L'agent est développé à partir des modèles d'open ai

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdir -p .streamlit
streamlit run streamlit/Landing.page.py
```

### API de prédiction météo

Le notebook `streamlit/Modèle/model_interaction.ipynb` entraîne le préprocesseur
et le modèle, puis les sauvegarde ensemble dans
`streamlit/Modèle/weather_artifacts.joblib`. Depuis la racine du projet, lancez
l'API avec :

```bash
uvicorn main:app --app-dir .streamlit/api --reload
```

La documentation interactive et l'essai des endpoints sont disponibles à
`http://127.0.0.1:8000/docs`. Le endpoint `POST /predict` attend les 15 variables
utilisées à l'entraînement, dont `RainToday` (0 ou 1).

Pour construire et lancer l'image Docker depuis la racine du projet :

```bash
docker build -t weather-api .
docker run --rm -p 8080:8080 weather-api
```