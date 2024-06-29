import streamlit as st

st.title("Ultrasound Exam")

# Mostrar la imagen del logo desde la URL
st.image("https://storage.googleapis.com/allostericsolutionsr/Allosteric_Solutions.png") 

# Mostrar el contacto y el sitio web
st.write("Contacto:", "www.allostericsolutions.com")
st.write("Sitio web:", "franciscocuriel@allostericsolutions.com")

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
