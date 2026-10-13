from pathlib import Path

import streamlit as st

#1 set the page with st.set_page_config
st.set_page_config(
    page_title="Météo de votre mariage",
    page_icon="🌦️",
    layout="wide",
)

css = Path(__file__).with_name("style.css").read_text(encoding="utf-8")
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

with st.container(key="landing-header"):
    brand_col, nav_col = st.columns([1, 2], vertical_alignment="center")
    with brand_col:
        st.markdown("**MON MARIAGE · MÉTÉO**")
    with nav_col:
        st.markdown(
            "[Notre approche](#notre-approche)　"
            "[Comment ça marche](#comment-ca-marche)"
        )
        st.page_link("pages/Login.py", label="Connexion", icon=":material/login:")
        st.page_link("pages/Contact.py", label="Contact", icon=":material/mail:")

with st.container(key="landing-hero"):
    copy_col, image_col = st.columns([1.15, 0.85], vertical_alignment="center")
    with copy_col:
        st.markdown("**ANTICIPER SEREINEMENT, CÉLÉBRER PLEINEMENT**")
        st.title("Et si la météo faisait partie de votre histoire ?")
        st.write(
            "Explorez les tendances météo de votre lieu de mariage et préparez "
            "votre journée avec un regard éclairé par les données."
        )
        # st.page_link(
        #     "/home/matthieumouillon/projects/app-streamlit/streamlit/pages/Modele_interact.py",
        #     label="Averse_prédiction",
        #     type="primary",
        # )

    with image_col:
        with st.container(key="landing-image1"):
            st.image(
                Path(__file__).parent
                / "images"
                / "image1.png",
                width=500,
                caption="useful tools",
            )

with st.container(key="landing-intro"):
    image_col, copy_col = st.columns([0.85, 1.15], vertical_alignment="center")
    with image_col:
        with st.container(key="landing-image2"):
            st.image(
                Path(__file__).parent
                / "images"
                / "image2.jpg",
                width=500,
                caption="useful tools",
            )
    with copy_col:
        st.markdown("**NOTRE APPROCHE**")
        st.header("Des données pour mieux se projeter")
        st.write(
            "La météo ne se commande pas. En revanche, consulter les tendances "
            "historiques d’un lieu et d’une période peut aider à préparer des "
            "options adaptées, sans promettre de prédire le temps qu’il fera."
        )
        st.markdown(
            "- Des repères construits à partir de données\n"
            "- Une lecture claire des tendances\n"
            "- Des pistes concrètes pour anticiper"
        )

st.markdown('<span id="comment-ca-marche"></span>', unsafe_allow_html=True)
st.markdown("**COMMENT ÇA MARCHE**")
st.header("Une démarche simple, de la donnée à la décision")

feature_columns = st.columns(3)
features = [
    ("01", "Choisir un lieu", "Situez votre projet et sa période dans leur contexte."),
    ("02", "Lire les tendances", "Explorez les indicateurs historiques disponibles."),
    ("03", "Prévoir des options", "Préparez des solutions de repli adaptées à votre journée."),
]
for column, (number, title, description) in zip(feature_columns, features):
    with column:
        with st.container(key=f"landing-feature-{number}"):
            st.markdown(f"**{number}**")
            st.subheader(title)
            st.write(description)

st.markdown('<span id="notre-approche"></span>', unsafe_allow_html=True)
st.markdown("**EXEMPLES DE PROJETS**")
st.header("Une expérience pensée pour les futurs mariés")


case_columns = st.columns(2)
cases = [
    ("image3", "Comprendre un lieu", "Comparer les tendances météo selon les lieux envisagés."),
    ("image4", "Préparer la journée", "Transformer les repères disponibles en options pratiques."),
]
for column, (image_label, title, description) in zip(case_columns, cases):
    with column:
        with st.container(key=f"landing-case-{image_label}"):
            with st.container(key=f"landing-{image_label}"):
                st.markdown(image_label)
            st.subheader(title)
            st.write(description)

with st.container(key="landing-contact"):
    st.markdown('<span id="contact"></span>', unsafe_allow_html=True)
    st.markdown("**VOTRE PROJET**")
    st.header("Préparons votre journée avec sérénité")
    st.write(
        "Cette page est une première maquette. Les analyses et les sources "
        "de données seront précisées au fil du projet."
    )


with st.container(key="landing-footer"):
    st.markdown("**MON MARIAGE · MÉTÉO**")
    st.caption("Une maquette originale autour des données météo et du mariage.")
