
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Floating Character", layout="centered")
st.title("🛸 Floating Animated Character")

components.html("""
<style>
@keyframes float {
  0% { transform: translateY(0); }
  50% { transform: translateY(-20px); }
  100% { transform: translateY(0); }
}
.robot {
  position: relative;
  animation: float 3s ease-in-out infinite;
  width: 150px;
}
</style>

<div style="text-align:center;">
  <img class="robot" src="https://media.giphy.com/media/12XDYvMJNcmLgQ/giphy.gif"/>
  <p>👋 I'm flying! Ask me anything!</p>
</div>
""", height=300)
