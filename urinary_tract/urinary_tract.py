import streamlit as st

# Inicializar la variable en session_state
if 'mostrar_eponimos' not in st.session_state:
    st.session_state.mostrar_eponimos = False

# Función para estilizar los títulos
def style_expander_title(title):
    return f"<span style='color:gold; font-weight:bold;'>{title}</span>"

# Crear un título estilizado para el expander
expander_title = style_expander_title("Eponyms related to Urinary Tract Conditions")

# Sección que se expande y se contrae
with st.expander(expander_title, expanded=st.session_state.mostrar_eponimos):
    st.write("**Henoch-Schönlein purpura:** Is an inflammatory disorder that affects small blood vessels, causing a purple rash on the skin, abdominal and joint pain, and can also affect the kidneys.")
    st.write("**Nutcracker syndrome:** Is a condition caused by compression of the left renal vein between the aorta and the superior mesenteric artery, which can lead to problems with renal blood flow.")
    st.write("**Wilms tumor (nephroblastoma):** Is a type of kidney cancer that primarily affects children. It can be referred to as nephroblastoma and can be life-threatening if left untreated.")
