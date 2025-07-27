
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Clickable Robot", layout="centered")
st.title("🖱️ Click the Robot's Hand")

components.html("""
<style>
#robot {
  position: relative;
}
#hand {
  position: absolute;
  top: 120px;
  left: 80px;
  width: 50px;
  height: 50px;
  background: transparent;
  cursor: pointer;
}
</style>

<div id="robot">
  <img src="https://media.giphy.com/media/5xtDarzp5at2qwSTlUk/giphy.gif" width="200"/>
  <div id="hand" onclick="alert('👋 Robot says hi!')"></div>
</div>
""", height=250)
