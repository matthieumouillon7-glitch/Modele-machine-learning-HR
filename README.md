# MODELE DE MACHINE LEARNING EN RH

#**MODELE DE MACHINE LEARNING EN HR - CAS D'USAGE**
**

#**Introduction** 🤖
#Bonjour, ceci est un repository avec un modèle de **machine learning en python.**

#**Modèle** 🔢
#Le modèle utilisé est un modèle dit supervisé de régression linéaire

#**Utilisation** 🛠️
#Ce modèle permet de **prédire** la possibilité d'une **absence** pour une personne donnée, en fonction de son âge, de son équipe d'appartenance et de son ancienneté à partir des données passées. Pour cela il vous suffit de l'importer et de modifier les paramètres

## Application Streamlit

L'application météo se trouve dans `streamlit/`. Pour la lancer en local :

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdir -p .streamlit
```

Créez `.streamlit/secrets.toml` à la racine du projet avec les identifiants
OAuth Google, Snowflake et la clé OpenAI (ce fichier est ignoré par Git).
Pour le chat, ajoutez notamment :

```toml
OPENAI_API_KEY = "votre-cle-api"
```

Puis lancez :

```bash
streamlit run streamlit/Landing.page.py
```

Dans les identifiants OAuth de Google, configurez l'URI de redirection
locale `http://localhost:8501/oauth2callback`. Remplacez-la par l'URL publique
de l'application lors du déploiement.

Avant le premier enregistrement de profil, exécutez
`streamlit/sql/create_user_profiles.sql` dans Snowflake. Le rôle de l'application
doit pouvoir utiliser le warehouse et lire, insérer et mettre à jour
`SF_TUTS.PUBLIC.USER_PROFILES`. Il est préférable d'utiliser un rôle applicatif
dédié plutôt qu'un rôle d'administration.
