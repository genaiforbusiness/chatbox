import streamlit as st
import google.generativeai as genai
import os

# Configure the Gemini API
@st.cache_resource
def load_client() -> genai.Client:
    """Load Google Gen AI Client."""
    API_KEY = os.environ.get("GEMINI_API_KEY")

    if not API_KEY:
        st.error(
            "🚨 Configuration Error: Please set `GEMINI_API_KEY`."
        )
        st.stop()

    return genai.Client(
        api_key=API_KEY,
    )
    
client = load_client()

st.title("My First GenAI App")

# Text input
prompt = st.text_input("Enter a prompt:")

# Button
if st.button("Generate"): 
    if prompt:
        try:
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(prompt)
            st.write(response.text)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a prompt.")