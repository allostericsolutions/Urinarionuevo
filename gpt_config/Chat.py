import streamlit as st
import openai
import logging
import os  # Asegúrate de haber importado este módulo

# Configure logging
logging.basicConfig(level=logging.INFO)

# Retrieve and validate API key
OPENAI_API_KEY = st.secrets.get("OPENAI_API_KEY", None)
if not OPENAI_API_KEY:
    st.error("Please add your OpenAI API key to the Streamlit secrets.toml file.")
    st.stop()

# Assign OpenAI API Key
openai.api_key = OPENAI_API_KEY

# Leer el contenido del prompt de configuración
def get_prompt():
    try:
        prompt_path = "gpt_config/prompt.text"  # Ruta corregida
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
            response = openai.Completion.create(
                engine="gpt-4",
                prompt=prompt,
                max_tokens=150,
                temperature=0.7,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )

            st.text_area("Waves Assistant:", value=response.choices[0].text.strip(), height=200, max_chars=None, key="assistant_response")
        except Exception as e:
            st.error(f"Error generating response: {str(e)}")
