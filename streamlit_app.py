import streamlit as st
from data_agent import DataAnalysisAgent
import os

st.title("AI Data Analysis Agent")

api_key = st.sidebar.text_input("Enter OpenAI API Key", type="password")

if api_key:
    if 'agent' not in st.session_state:
        st.session_state.agent=DataAnalysisAgent(api_key)

    uploaded_file=st.file_uploader("Upload a CSV file", type="csv")
    if uploaded_file:
        uploaded_file.to_csv("temp_data.csv")
        response=st.session_state.agent.chat("Load the CSV file temp_data.csv")
        st.write(response)

    user_input = st.text_input("Ask your questions")
    if user_input:
        response= st.session_state.agent.chat(user_input)
        st.write(response)