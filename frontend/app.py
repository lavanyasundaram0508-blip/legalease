import streamlit as st
import google.generativeai as genai
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
st.title("LegalEase AI")
f = st.file_uploader("Upload", type=["txt","pdf"])
q = st.text_input("What to know?")
if st.button("Simplify"):
    if f and q:
        t = f.read().decode('utf-8', errors='ignore')[:4000]
        m = genai.GenerativeModel("gemini-flash-latest")
        r = m.generate_content(f"Simplify: {t} Question: {q}")
        st.success(r.text)
