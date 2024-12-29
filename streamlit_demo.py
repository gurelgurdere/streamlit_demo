import os
from langchain_openai import ChatOpenAI
import streamlit as st

st.title("Ask Anything")

with st.sidebar:
    st.title("Provide Your API Key")
    OPENAI_API_KEY = st.text_input("OpenAI API Key", type="password")

if not OPENAI_API_KEY:
    st.info("Enter your OpenAI Key to Continue")
    st.stop()

llm = ChatOpenAI(model="gpt-4o", api_key=OPENAI_API_KEY)
question = st.text_input("Enter the question:")

if question:
    try:
        response = llm.invoke(question)
        st.write(response.content)
    except Exception as e:
        st.error(f"An error occurred: {e}")



