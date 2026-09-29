import streamlit as st
import os
import google.generativeai as genai

# API Key fix
try:
    api_key = st.secrets["GEMINI_API_KEY"]
except:
    api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

st.set_page_config(page_title="LegalEase AI", page_icon="⚖️")
st.title("⚖️ LegalEase AI - Legal Document Simplifier")
st.write("Upload your legal document and get simple explanation!")

uploaded = st.file_uploader("Upload Document", type=["txt", "pdf"])
query = st.text_input("What do you want to know?")

if st.button("Simplify"):
    if uploaded and query:
        text = uploaded.read().decode('utf-8', errors='ignore')[:4000]
        # NEW MODEL - 100% work aagum
        model = genai.GenerativeModel("gemini-2.0-flash")
        prompt = f"Explain this legal doc in simple English: {text}. Question: {query}"
        response = model.generate_content(prompt)
        st.success(response.text)
    else:
        st.warning("File and question rendu kudunga da!")
