
import streamlit as st

st.set_page_config(page_title="Ask ROA W AMMAR", layout="wide")

st.title("💬 Ask ROA W AMMAR")
st.markdown("### 🤖 I'm ready to help you — just ask me anything!")

# Two columns: robot + input fields
col1, col2 = st.columns([1, 2])

with col1:
    st.image("https://media.giphy.com/media/12XDYvMJNcmLgQ/giphy.gif", caption="👈 Type here!", width=200)

with col2:
    child_name = st.text_input("🙋 What's your name?")
    question = st.text_input("❓ What do you want to ask me?")

if st.button("✨ Go!"):
    if not child_name or not question:
        st.warning("Please enter your name and a question.")
    else:
        st.success(f"🤖 Nice to meet you, {child_name}! I'm thinking about your question...")
