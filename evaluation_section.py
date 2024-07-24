import streamlit as st
import openai  # Importar la librería OpenAI
from evaluation_prompts.gpt import call_gpt, prompt

def evaluation_mode():
    st.write("## Evaluation Mode")
    exec(open('Abdominal Sonography Overview/evaluation.py').read())

    headers = {
        "authorization": st.secrets["auth_token"],
        "content-type": "application/json"
    }

    # Usar las funciones de GPT
    gpt_response = call_gpt(prompt)
    st.write("### GPT Response")
    st.write(gpt_response)
