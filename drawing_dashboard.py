import streamlit as st
from drawing import generate_drawing_with_stability
import base64
from io import BytesIO
from PIL import Image

def render_drawing_dashboard():
    if "unlock_tabs" not in st.session_state:
        st.session_state.unlock_tabs = False

    st.title("🎨 Drawing Dashboard")

    if not st.session_state.unlock_tabs:
        code_input = st.text_input("🔒 Enter Dad's secret code to access drawing dashboard:", type="password")
        if code_input == "dad123":
            st.session_state.unlock_tabs = True
            st.success("✅ Access granted!")
            st.stop()
        else:
            st.warning("🔐 Please enter the correct password to view this section.")
            return

    prompt = st.text_input("🖌️ Enter a drawing prompt (e.g. 'a rocket flying through space'):")

    if st.button("🎨 Generate Drawing"):
        if prompt.strip() == "":
            st.warning("Please enter a prompt first.")
        else:
            with st.spinner("Generating drawing..."):
                image_bytes = generate_drawing_with_stability(prompt)
                if image_bytes:
                    st.image(image_bytes, caption=f"🎨 Drawing for: {prompt}")
                    img = Image.open(BytesIO(image_bytes))
                    buffered = BytesIO()
                    img.save(buffered, format="PNG")
                    img_base64 = base64.b64encode(buffered.getvalue()).decode()
                    href = f'<a href="data:image/png;base64,{img_base64}" download="drawing.png">📥 Download drawing</a>'
                    st.markdown(href, unsafe_allow_html=True)
                else:
                    st.error("Failed to generate image. Please check your API key or try again later.")