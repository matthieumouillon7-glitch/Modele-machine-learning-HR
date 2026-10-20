import logging
from pathlib import Path
import snowflake.connector
import streamlit as st
from snowflake.connector.errors import Error as SnowflakeError

st.set_page_config(page_title="Connexion", page_icon="🌦️", layout="wide")

css = Path(__file__).resolve().parents[1].joinpath("style.css").read_text(
    encoding="utf-8"
)
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

st.title("Inscription")

with st.form("profile"):
    st.subheader("Vos coordonnées")
    company_name = st.text_input("Entreprise")
    name = st.text_input("Nom")
    first_name = st.text_input("Prénom")
    profile_email = st.text_input("E-mail")
    phone = st.text_input("Téléphone")
    submitted = st.form_submit_button("Enregistrer le profil", type="primary")

if submitted:
    if not company_name.strip() or not first_name.strip() or not name.strip():
        st.error("Veuillez renseigner l'entreprise, votre prénom et votre nom.")
        st.stop()
    if "@" not in profile_email or not phone.strip():
        st.error("Veuillez renseigner un e-mail valide et un numéro de téléphone.")
        st.stop()

    snowflake_settings = st.secrets.get("snowflake")
    if not snowflake_settings:
        st.error("La section [snowflake] manque dans .streamlit/secrets.toml.")
        st.stop()

    required_settings = (
        "account",
        "user",
        "password",
        "role",
        "warehouse",
        "database",
        "schema",
    )
    missing_settings = [
        key for key in required_settings if not snowflake_settings.get(key)
    ]
    if missing_settings:
        st.error(
            "Configuration Snowflake incomplète : "
            + ", ".join(missing_settings)
        )
        st.stop()

    connection = None
    cursor = None
    try:
        connection = snowflake.connector.connect(
            account=snowflake_settings["account"],
            user=snowflake_settings["user"],
            password=snowflake_settings["password"],
            role=snowflake_settings["role"],
            warehouse=snowflake_settings["warehouse"],
            database=snowflake_settings["database"],
            schema=snowflake_settings["schema"],
        )
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO APP_DB.REGISTRATION.REGISTER (
                COMPANY_NAME,
                NAME,
                FIRST_NAME,
                EMAIL,
                TELEPHONE
            ) VALUES (%s, %s, %s, %s, %s)
            """,
            (
                company_name.strip(),
                name.strip(),
                first_name.strip(),
                profile_email.strip(),
                phone.strip(),
            ),
        )
    except SnowflakeError:
        logging.exception("Impossible d'enregistrer le profil dans Snowflake.")
        st.error(
            "L'enregistrement dans Snowflake a échoué. "
            "Vérifiez les paramètres et les droits du rôle applicatif."
        )
    else:
        st.success("Votre profil a été enregistré.")
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()
