import streamlit as st
import openai
import logging
import os
from gpt_config.openai_setup import initialize_openai  # Importa la función de inicialización

# Configurar logging
logging.basicConfig(level=logging.INFO)

# Inicializar OpenAI API Key
initialize_openai()

# Leer el contenido del prompt de configuración
def get_prompt():
    try:
        prompt_path = "gpt_config/prompt.text"  # Asegúrate de que es 'prompt.text'
        if not os.path.exists(prompt_path):
            st.error(f"File not found: {prompt_path}")
            st.stop()

        with open(prompt_path, "r") as file:
            prompt = file.read()
        return prompt
    except Exception as e:
        st.error(f"Error reading prompt file: {str(e)}")
        st.stop()

st.write("## Waves Assistant")

user_input = st.text_input("You:", key="user_input")

if st.button("Send"):
    if user_input:
        prompt = get_prompt() + "\n" + user_input
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": user_input}
                ],
                max_tokens=150,
                temperature=0.7,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )

            st.text_area("Waves Assistant:", value=response['choices'][0]['message']['content'].strip(), height=200, max_chars=None, key="assistant_response")
        except Exception as e:
            st.error(f"Error generating response: {str(e)}")
