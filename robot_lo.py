
from streamlit_lottie import st_lottie
import streamlit as st
import requests

st.set_page_config(page_title="Lottie Robot", layout="centered")
st.title("🤖 Floating Robot with Lottie")

def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url = "https://lottie.host/6a77bd8e-2177-4f3a-8f6d-364a43e88c67/xPSjU1AL2K.json"
robot = load_lottie_url(lottie_url)

if robot:
    st_lottie(robot, height=300, key="robot_floating")
else:
    st.error("Failed to load robot animation.")
