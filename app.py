from dotenv import load_dotenv
load_dotenv()#loading environ variables

import streamlit as st 
import os 
import google.generativeai as genai


#configure gemini pro  model andget response 

genai.configure(api_key="GOOGLE_API_KEY")
model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(prompt):
    response = model.generate_content(prompt)
    return response.text

#insitialize our streamlit app 

st.set_page_config(page_title = "Q&A DEMO")

st.header("Gemini LLM Application")

input=st.text_input("INPUT :",key="Input")
submit=st.button("Ask ANY THING TO ME ")

if submit:
    response=get_gemini_response(input)
    st.write(response)
    