import streamlit as st

st.title("Ultrasound Exam")

# Mostrar logo, contacto y sitio web antes de las pestañas
st.image("https://storage.googleapis.com/allostericsolutionsr/Allosteric_Solutions.png") 
st.write("Contacto:", "www.allostericsolutions.com")
st.write("Sitio web:", "franciscocuriel@allostericsolutions.com")

tab1, tab2 = st.tabs(["Learning", "Evaluation"])

with tab1:
    st.write("## Learning Mode")
    st.write("This section will provide you with information and examples about ultrasound measurements.")

    # Selecciona el tema principal
    tema_principal = st.selectbox("Select a Topic:", ["ARDMS for Abdominal Ultrasound", "ARDMS for SPI"])

    if tema_principal == "ARDMS for Abdominal Ultrasound":
        st.write("### ARDMS for Abdominal Ultrasound")

        # Selecciona el subtema
        subtema = st.selectbox("Select a Subtopic:", [
            "Abdominal Sonography Overview",
            "The Liver",
            "The Gallbladder",
            "The Bile Ducts",
            "The Pancreas",
            "The Spleen",
            "The Urinary Tract",
            "The Adrenal Glands",
            "Abdominal Vasculature",
            "Gastrointestinal Tract and Abdominal Wall",
            "Noncardiac Chest and Retroperitoneum",
            "The Face and Neck",
            "The Male Pelvis",
            "The Musculoskeletal Imaging, Breast, and Superficial Structures"
        ])

        # Mostrar el contenido del subtema
        if subtema == "Abdominal Sonography Overview":
            st.write("#### Abdominal Sonography Overview")
            # Agrega aquí el contenido de "Abdominal Sonography Overview"
            # (textos, imágenes, videos, etc.)
        elif subtema == "The Liver":
            st.write("#### The Liver")
            # Agrega aquí el contenido de "The Liver"
            # (textos, imágenes, videos, etc.)
        elif subtema == "The Gallbladder":
            st.write("#### The Gallbladder")
            # Agrega aquí el contenido de "The Gallbladder"
            # (textos, imágenes, videos, etc.)
        elif subtema == "The Bile Ducts":
            st.write("#### The Bile Ducts")
            # Agrega aquí el contenido de "The Bile Ducts"
            # (textos, imágenes, videos, etc.)
        elif subtema == "The Pancreas":
            st.write("#### The Pancreas")
            # Agrega aquí el contenido de "The Pancreas"
            # (textos, imágenes, videos, etc.)
        elif subtema == "The Spleen":
            st.write("#### The Spleen")
            # Agrega aquí el contenido de "The Spleen"
            # (textos, imágenes, videos, etc.)
        elif subtema == "The Urinary Tract":
            st.write("#### The Urinary Tract")
            # Agrega aquí el contenido de "The Urinary Tract"
            # (textos, imágenes, videos, etc.)
        elif subtema == "The Adrenal Glands":
            st.write("#### The Adrenal Glands")
            # Agrega aquí el contenido de "The Adrenal Glands"
            # (textos, imágenes, videos, etc.)
        elif subtema == "Abdominal Vasculature":
            st.write("#### Abdominal Vasculature")
            # Agrega aquí el contenido de "Abdominal Vasculature"
            # (textos, imágenes, videos, etc.)
        elif subtema == "Gastrointestinal Tract and Abdominal Wall":
            st.write("#### Gastrointestinal Tract and Abdominal Wall")
            # Agrega aquí el contenido de "Gastrointestinal Tract and Abdominal Wall"
            # (textos, imágenes, videos, etc.)
        elif subtema == "Noncardiac Chest and Retroperitoneum":
            st.write("#### Noncardiac Chest and Retroperitoneum")
            # Agrega aquí el contenido de "Noncardiac Chest and Retroperitoneum"
            # (textos, imágenes, videos, etc.)
        elif subtema == "The Face and Neck":
            st.write("#### The Face and Neck")
            # Agrega aquí el contenido de "The Face and Neck"
            # (textos, imágenes, videos, etc.)
        elif subtema == "The Male Pelvis":
            st.write("#### The Male Pelvis")
            # Agrega aquí el contenido de "The Male Pelvis"
            # (textos, imágenes, videos, etc.)
        elif subtema == "The Musculoskeletal Imaging, Breast, and Superficial Structures":
            st.write("#### The Musculoskeletal Imaging, Breast, and Superficial Structures")
            # Agrega aquí el contenido de "The Musculoskeletal Imaging, Breast, and Superficial Structures"
            # (textos, imágenes, videos, etc.)

    elif tema_principal == "ARDMS for SPI":
        st.write("### ARDMS for SPI")
        # Agrega aquí el contenido de "ARDMS for SPI"
        # (textos, imágenes, videos, etc.) 

with tab2:
    st.write("## Evaluation Mode")
    st.write("This section will test your knowledge about ultrasound measurements.")

    # Ejecuta el módulo de evaluación
    st.run_the_script(path="evaluacion.py") 
