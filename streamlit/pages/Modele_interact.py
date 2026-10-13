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

if "OPENAI_API_KEY" not in st.secrets:
    st.error(
        "Clé OpenAI introuvable. Ajoutez OPENAI_API_KEY dans "
        ".streamlit/secrets.toml à la racine du projet."
    )
    st.stop()

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Écrivez votre question…"):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("L’assistant prépare sa réponse…"):
            try:
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "Tu es un assistant chaleureux et clair qui aide "
                                "à préparer la météo d'un mariage. Présente les "
                                "données météo comme des tendances historiques, "
                                "pas comme des prévisions garanties."
                            ),
                        },
                        *st.session_state.messages,
                    ],
                )
            except OpenAIError as error:
                st.error(f"Impossible d’obtenir une réponse d’OpenAI : {error}")
            else:
                answer = response.choices[0].message.content
                if answer:
                    st.markdown(answer)
                    st.session_state.messages.append(
                        {"role": "assistant", "content": answer}
                    )
                else:
                    st.error("Le modèle a renvoyé une réponse vide.")
