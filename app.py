import streamlit as st
import google.generativeai as genai

# This pulls your key securely from Streamlit's "Secrets" setting
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    st.error("Please add your GEMINI_API_KEY to Streamlit Secrets!")

model = genai.GenerativeModel('gemini-2.0-flash')
st.title("🚀 Free AI Sales Script Generator")

industry = st.text_input("What industry are you targeting?")
product = st.text_input("What are you selling?")

if st.button("Generate Script"):
    if industry and product:
        with st.spinner('Writing your script...'):
            prompt = f"Write a professional, high-converting cold email for {product} targeting the {industry} industry."
            response = model.generate_content(prompt)
            st.success("Here is your sales script:")
            st.write(response.text)
    else:
        st.warning("Please enter both the industry and the product.")
