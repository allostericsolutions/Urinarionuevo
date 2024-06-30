import streamlit as st

# Inicializar la variable en session_state
if 'mostrar_eponimos' not in st.session_state:
    st.session_state.mostrar_eponimos = False

# Botón para alternar la visibilidad del expander
if st.button("Eponyms"):
    st.session_state.mostrar_eponimos = not st.session_state.mostrar_eponimos

# Función para estilizar los títulos dentro del expander
def style_title(title):
    return f"<span style='color:darkorange; font-weight:bold;'>{title}</span>"

# Crear un título estilizado para el expander
expander_title = "<span style='color:gold; font-weight:bold;'>Eponyms related to Urinary Tract Conditions:</span>"

# Sección que se expande y se contrae
with st.expander(expander_title, expanded=st.session_state.mostrar_eponimos):
    st.markdown(style_title("Henoch-Schönlein purpura:") + " Is an inflammatory disorder that affects small blood vessels, causing a purple rash on the skin, abdominal and joint pain, and can also affect the kidneys.", unsafe_allow_html=True)
    st.markdown(style_title("Nutcracker syndrome:") + " Is a condition caused by compression of the left renal vein between the aorta and the superior mesenteric artery, which can lead to problems with renal blood flow.", unsafe_allow_html=True)
    st.markdown(style_title("Wilms tumor (nephroblastoma):") + " Is a type of kidney cancer that primarily affects children. It can be referred to as nephroblastoma and can be life-threatening if left untreated.", unsafe_allow_html=True)
