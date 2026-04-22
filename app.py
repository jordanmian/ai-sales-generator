import streamlit as st
import google.generativeai as genai
from google.oauth2 import service_account

# 1. Access the Service Account info from Secrets
if "gcp_service_account" in st.secrets:
    info = st.secrets["gcp_service_account"]
    
    # 2. Create credentials from the info
    creds = service_account.Credentials.from_service_account_info(info)
    
    # 3. Configure the library with these credentials
    genai.configure(credentials=creds)
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("Service Account info not found in Secrets!")

st.title("🚀 AI Sales Script Generator")

industry = st.text_input("Target Industry")
product = st.text_input("What are you selling?")

if st.button("Generate Script"):
    if industry and product:
        with st.spinner('Writing...'):
            prompt = f"Write a professional sales email for {product} in the {industry} industry."
            response = model.generate_content(prompt)
            st.success(response.text)
    else:
        st.warning("Please fill in both fields.")
