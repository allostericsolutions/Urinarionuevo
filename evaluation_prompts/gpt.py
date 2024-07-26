import openai
import streamlit as st
import logging
import random

# Configure logging
logging.basicConfig(level=logging.INFO)

# Retrieve and validate API key
OPENAI_API_KEY = st.secrets.get("OPENAI_API_KEY", None)
if not OPENAI_API_KEY:
    st.error("Please add your OpenAI API key to the Streamlit secrets.toml file.")
    st.stop()

# Assign OpenAI API Key
openai.api_key = OPENAI_API_KEY
client = openai.OpenAI()

# Streamlit Page Configuration
st.set_page_config(
    page_title="Ultrasound Quiz",
    page_icon="📚",  # Book icon
    layout="wide",
    initial_sidebar_state="auto"
)

st.title("Ultrasound Quiz: Peritoneum and Retroperitoneum")

# Listas de órganos
peritoneales = [
    "Gallbladder", "Liver", "Ovaries", "Spleen", "Stomach", "Appendix", 
    "Transverse colon", "First part of the duodenum", "Jejunum", "Ileum", 
    "Sigmoid colon" 
]
retroperitoneales = [
    "Abdominal lymph nodes", "Adrenal glands", "Aorta", "Ascending and descending colon",
    "Most of the duodenum", "IVC", "Kidneys", "Pancreas", "Prostate gland",
    "Ureters", "Urinary bladder", "Uterus"
]

def generar_pregunta(organo):
    """Genera una pregunta sobre si el órgano es peritoneal o retroperitoneal."""
    return f"Is the {organo} peritoneal or retroperitoneal?"

def comprobar_respuesta(organo, respuesta):
    """Comprueba si la respuesta es correcta."""
    es_peritoneal = organo in peritoneales

    if es_peritoneal:
        return respuesta.lower() == "peritoneal"
    else:
        return respuesta.lower() == "retroperitoneal"

def obtener_explicacion(organo, es_peritoneal, respuesta_correcta):
    """Obtiene una breve explicación de GPT-3.5-turbo."""
    if es_peritoneal:
        correcto = "peritoneal"
    else:
        correcto = "retroperitoneal"

    prompt = f"""
    Explain briefly why {organo} is {'peritoneal' if es_peritoneal else 'retroperitoneal'}.
    """
    if respuesta_correcta.lower() != correcto.lower():
        prompt += f" Also, explain why '{respuesta_correcta}' is not correct."

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000,  # Aumento a 1000 tokens
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()

def main():
    """Main function to run the Streamlit app."""
    if "organo" not in st.session_state:
        st.session_state.organo = random.choice(peritoneales + retroperitoneales)
        st.session_state.feedback = ""
        st.session_state.explicacion = ""
        st.session_state.examen_realizado = False
        st.session_state.correcto = False

    pregunta = generar_pregunta(st.session_state.organo)
    st.subheader(pregunta)  # Mostrar la pregunta

    if not st.session_state.examen_realizado:
        respuesta = st.radio(
            label="Select the answer:",
            options=["Retroperitoneal", "Peritoneal"],
            key="respuesta"
        )

        if st.button("Check"):
            st.session_state.correcto = comprobar_respuesta(st.session_state.organo, respuesta)
            st.session_state.feedback = "Correct!" if st.session_state.correcto else "Incorrect"
            st.session_state.explicacion = obtener_explicacion(st.session_state.organo, st.session_state.organo in peritoneales, respuesta)
            st.session_state.examen_realizado = True
    
    # Mostrar el feedback y la explicación si la pregunta ha sido respondida
    if st.session_state.examen_realizado:
        st.markdown(f"### {st.session_state.feedback}")
        
        # Colorear la explicación dependiendo si la respuesta fue correcta o incorrecta
        color = "green" if st.session_state.correcto else "red"
        st.markdown(f"<p style='color:{color};font-size:16px;'>Explanation: {st.session_state.explicacion}</p>", unsafe_allow_html=True)

        if st.button("Next Question", key="next_button"):
            st.session_state.organo = random.choice(peritoneales + retroperitoneales)
            st.session_state.feedback = ""
            st.session_state.explicacion = ""
            st.session_state.examen_realizado = False
            st.session_state.correcto = False

if __name__ == "__main__":
    main()
