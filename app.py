import streamlit as st

st.title("🚀 AI Sales Script Generator")

# User Inputs
industry = st.text_input("What industry are you targeting?")
product = st.text_input("What are you selling?")

if st.button("Generate Script"):
    # This is where your OpenAI API logic will go later
    # For now, it's a placeholder to test the UI
    script = f"Hello! Since you are in {industry}, you need {product} to save time..."
    st.success(script)
    st.info("Next step: Connect your OpenAI API key to make this 'smart'!")
