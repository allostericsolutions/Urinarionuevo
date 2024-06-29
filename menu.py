import streamlit as st

st.title("Ultrasound Exam")

# Mostrar logo, contacto y sitio web antes de las pestañas
st.image("assets/logo.png")
st.write("Contacto:", open("assets/contacto.txt").read())
st.write("Sitio web:", open("assets/sitio_web.txt").read())

tab1, tab2 = st.tabs(["Learning", "Evaluation"])

with tab1:
    st.write("## Learning Mode")
    st.write("This section will provide you with information and examples about ultrasound measurements.")
    # Agrega aquí el contenido del modo de aprendizaje
    # (textos, imágenes, videos, etc.)

with tab2:
    st.write("## Evaluation Mode")
    st.write("This section will test your knowledge about ultrasound measurements.")
    # Ejecuta el módulo de evaluación
    st.run_the_script(path="evaluacion.py") 
