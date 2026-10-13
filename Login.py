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

st.title("Connexion")

if not st.user.is_logged_in:
    st.write("Connectez-vous avec votre compte pour créer votre profil.")
    if st.button("Se connecter avec votre compte", type="primary"):
        st.login("google")
    st.stop()

if st.button("Se déconnecter"):
    st.logout()
    st.stop()

issuer = st.user.get("iss", "")
subject = st.user.get("sub", "")
if not issuer or not subject:
    st.error(
        "Google n'a pas fourni les identifiants OIDC nécessaires. "
        "Vérifiez les revendications configurées pour l'application."
    )
    st.stop()

email = st.user.get("email") or st.user.get("preferred_username", "")
with st.form("profile"):
    st.subheader("Votre profil")
    first_name = st.text_input("Prénom", value=st.user.get("given_name", ""))
    last_name = st.text_input("Nom", value=st.user.get("family_name", ""))
    profile_email = st.text_input("E-mail", value=email)
    phone = st.text_input("Téléphone")
    submitted = st.form_submit_button("Enregistrer le profil", type="primary")

if submitted:
    if not first_name.strip() or not last_name.strip():
        st.error("Veuillez renseigner votre prénom et votre nom.")
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
            MERGE INTO USER_PROFILES AS target
            USING (
                SELECT
                    %s AS OIDC_ISSUER,
                    %s AS OIDC_SUBJECT,
                    %s AS FIRST_NAME,
                    %s AS LAST_NAME,
                    %s AS EMAIL,
                    %s AS PHONE
            ) AS source
            ON target.OIDC_ISSUER = source.OIDC_ISSUER
                AND target.OIDC_SUBJECT = source.OIDC_SUBJECT
            WHEN MATCHED THEN UPDATE SET
                FIRST_NAME = source.FIRST_NAME,
                LAST_NAME = source.LAST_NAME,
                EMAIL = source.EMAIL,
                PHONE = source.PHONE,
                UPDATED_AT = CURRENT_TIMESTAMP()
            WHEN NOT MATCHED THEN INSERT (
                OIDC_ISSUER,
                OIDC_SUBJECT,
                FIRST_NAME,
                LAST_NAME,
                EMAIL,
                PHONE
            ) VALUES (
                source.OIDC_ISSUER,
                source.OIDC_SUBJECT,
                source.FIRST_NAME,
                source.LAST_NAME,
                source.EMAIL,
                source.PHONE
            )
            """,
            (
                issuer,
                subject,
                first_name.strip(),
                last_name.strip(),
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
