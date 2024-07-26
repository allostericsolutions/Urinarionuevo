import streamlit as st

# Verificar los parámetros de consulta y actualizar la página actual
query_params = st.experimental_get_query_params()
if "pagina" in query_params:
    st.session_state.pagina_actual = query_params["pagina"][0]
else:
    st.session_state.pagina_actual = "Content"

st.title("Abdomen ARDMS")

# Mostrar logo, contacto y sitio web antes de las pestañas
st.image(
    "https://storage.googleapis.com/allostericsolutionsr/Allosteric_Solutions.png",
    width=400,
)
st.write("Contacto:", "franciscocuriel@allostericsolutions.com")
st.write("Sitio web:", "www.allostericsolutions.com")

st.write("### ARDMS for Abdominal Ultrasound")

# Opciones de página
pagina = st.radio("Select:", ["Content", "Evaluation"])
if pagina != st.session_state.pagina_actual:
    st.session_state.pagina_actual = pagina
    st.experimental_set_query_params(pagina=pagina)

def evaluation_mode():
    st.write("## Evaluation Mode")
    st.markdown("[Acceder a Evaluation Mode](https://chatbot-prueba-5yilucptxsrkggrlgfn5yt.streamlit.app/)", unsafe_allow_html=True)

# Mostrar contenido según la página seleccionada
if st.session_state.pagina_actual == "Content":
    # Opciones de subtema
    subtema = st.radio(
        "Select a Subtopic:",
        [
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
            "The Musculoskeletal Imaging, Breast, and Superficial Structures",
        ],
    )

    # Mostrar el contenido del subtema
    if subtema == "Abdominal Sonography Overview":
        st.write("#### Abdominal Sonography Overview")
        # Ejecuta el módulo de "Abdominal Sonography Overview"
        exec(open("Abdominal Sonography Overview/abdominaloverview.py").read())
        exec(open("Abdominal Sonography Overview/signs.py").read())
    elif subtema == "The Liver":
        st.write("#### The Liver")
        exec(open("The liver/Eponyms.py").read())
        exec(open("The liver/Tumors.py").read())
    elif subtema == "The Gallbladder":
        st.write("#### The Gallbladder")
        exec(open("The Gallbladder/signs.py").read())
    elif subtema == "The Bile Ducts":
        st.write("#### The Bile Ducts")
        exec(open("Biles Ducts/eponyms.py").read())
    elif subtema == "The Pancreas":
        st.write("#### The Pancreas")
        exec(open("pancreas/eponyms.py").read())
        exec(open("pancreas/signs.py").read())
    elif subtema == "The Spleen":
        st.write("#### The Spleen")
        # Agrega aquí el contenido de "The Spleen"
    elif subtema == "The Urinary Tract":
        st.write("#### The Urinary Tract")
        exec(open("urinary_tract/urinary_tract.py").read())
        exec(open("urinary_tract/anatomy_physiology.py").read())
    elif subtema == "The Adrenal Glands":
        st.write("#### The Adrenal Glands")
        # Agrega aquí el contenido de "The Adrenal Glands"
    elif subtema == "Abdominal Vasculature":
        st.write("#### Abdominal Vasculature")
        exec(open("Abdominalvasculature/eponyms.py").read())
    elif subtema == "Gastrointestinal Tract and Abdominal Wall":
        st.write("#### Gastrointestinal Tract and Abdominal Wall")
        # Agrega aquí el contenido de "Gastrointestinal Tract and Abdominal Wall"
    elif subtema == "Noncardiac Chest and Retroperitoneum":
        st.write("#### Noncardiac Chest and Retroperitoneum")
        # Agrega aquí el contenido de "Noncardiac Chest and Retroperitoneum"
    elif subtema == "The Face and Neck":
        st.write("#### The Face and Neck")
        exec(open("Face and Neck/eponyms.py").read())
        exec(open("Face and Neck/Thyroid.py").read())
        exec(open("Face and Neck/Thyroidanatomy/Thyroidanatomy.py").read())
        exec(open("Face and Neck/Thyroidanatomy/Thyroidpathology.py").read())
        exec(open("Face and Neck/Thyroidanatomy/imagenes.py").read())
    elif subtema == "The Male Pelvis":
        st.write("#### The Male Pelvis")
        # Agrega aquí el contenido de "The Male Pelvis"
    elif subtema == "The Musculoskeletal Imaging, Breast, and Superficial Structures":
        st.write(
            "#### The Musculoskeletal Imaging, Breast, and Superficial Structures"
        )
        # Agrega aquí el contenido de "The Musculoskeletal Imaging, Breast, and Superficial Structures"

# Bloque para la sección "Evaluation"
if st.session_state.pagina_actual == "Evaluation":
    evaluation_mode()
