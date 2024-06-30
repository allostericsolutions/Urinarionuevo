import streamlit as st

st.write("#### The Urinary Tract")
# Agrega aquí el contenido de "The Urinary Tract"
# (textos, imágenes, videos, etc.)

# Variable para controlar la visibilidad de la sección de eponimos
mostrar_eponimos = False

# Botón para mostrar la sección de eponimos
if st.button("Show Eponyms"):
    mostrar_eponimos = not mostrar_eponimos

# Sección que se expande y se contrae 
with st.expander("Eponyms related to Urinary Tract Conditions:", expanded=mostrar_eponimos):
    st.write("**Henoch-Schönlein purpura:**  Is an inflammatory disorder that affects small blood vessels, causing a purple rash on the skin, abdominal and joint pain, and can also affect the kidneys.")
    st.write("**Nutcracker syndrome:**  Is a condition caused by compression of the left renal vein between the aorta and the superior mesenteric artery, which can lead to problems with renal blood flow.")
    st.write("**Wilms tumor (nephroblastoma):**  Is a type of kidney cancer that primarily affects children. It can be referred to as nephroblastoma and can be life-threatening if left untreated.")
