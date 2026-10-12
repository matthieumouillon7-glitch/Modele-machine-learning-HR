from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Contact",
    page_icon="🌦️",
    layout="wide",
)

css = Path(__file__).resolve().parents[1].joinpath("style.css").read_text(
    encoding="utf-8"
)
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

st.title("Contact")
st.write(
    "Parlez-nous de votre projet : remplissez le formulaire ci-dessous "
    "et nous vous recontacterons."
)

components.html(
    """
    <div id="hubspot-form"></div>
    <script src="https://js-eu1.hsforms.net/forms/embed/v2.js"></script>
    <script>
      hbspt.forms.create({
        portalId: "146425616",
        formId: "dde1c90b-bb9f-4858-bef8-1544774179c9",
        region: "eu1",
        target: "#hubspot-form"
      });
    </script>
    """,
    height=850,
    scrolling=True,
)
