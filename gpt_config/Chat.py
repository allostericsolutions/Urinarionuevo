import streamlit as st
import openai
import logging

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
    with open("prompt.txt", "r") as file:
        prompt = file.read()
    return prompt

st.write("## Waves Assistant")

user_input = st.text_input("You:", key="user_input")

if st.button("Send"):
    if user_input:
        prompt = get_prompt() + "\n" + user_input
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
