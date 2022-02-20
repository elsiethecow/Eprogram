import streamlit as st
from streamlit_lottie import st_lottie
import requests


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def lottie(url):
    content = load_lottieurl(url)
    st_lottie(content)

st.balloons()

st.title("love you")

if st.button("Please push me"):   

    lottie("https://assets10.lottiefiles.com/packages/lf20_n1a5ebk9.json")
    lottie("https://assets6.lottiefiles.com/packages/lf20_wzKgBd.json")
    ":crown::dog::christmas_tree:"*900
