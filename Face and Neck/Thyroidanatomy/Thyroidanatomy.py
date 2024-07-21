import streamlit as st

# Definir el contenido de la tarjeta de aprendizaje
title = "<h2 style='color: blue;'>Vascular Anatomy of the Thyroid Gland and Neck</h2>"
question = "<h4 style='color: darkorange;'>What are the primary vascular structures near the thyroid gland and their branches?</h4>"
answer = """
<b><u>Primary Vascular Structures:</u></b>
<ul>
    <li><b>Common Carotid Artery:</b> The most medial vessel, located lateral to the thyroid gland.</li>
    <li><b>Internal Jugular Vein:</b> Also located lateral to the thyroid gland.</li>
</ul>

<b><u>Branches of the Common Carotid Artery:</u></b>
<ul>
    <li><b>Internal Carotid Artery:</b> Branches from the common carotid arteries above the thyroid gland.</li>
    <li><b>External Carotid Artery:</b> Branches from the common carotid arteries above the thyroid gland.</li>
</ul>

<b><u>Thyroid Arteries:</u></b>
<ul>
    <li><b>Superior Thyroid Artery:</b> The first branch of the external carotid artery.</li>
    <li><b>Inferior Thyroid Artery:</b> A branch of the thyrocervical trunk of the subclavian artery.</li>
</ul>

<b><u>Thyroid Veins:</u></b>
<ul>
    <li>These veins drain into the internal jugular vein.</li>
    <li>Jugular veins are positioned superior and lateral to the common carotid arteries.</li>
</ul>

<b><u>Summary:</u></b>
<p>The common carotid artery is the main medial vessel, branching into internal and external carotid arteries. The superior thyroid artery branches from the external carotid, while the inferior thyroid artery comes from the thyrocervical trunk of the subclavian artery. Corresponding thyroid veins drain into the internal jugular veins, which are situated superiorly and laterally to the common carotid arteries.</p>
"""

# Detalles de la imagen
image_details = [
    {"path": "Face and Neck/imagenes/Lateral to the thyoroid.png", "description": "Lateral view of the thyroid"},
    {"path": "Face and Neck/imagenes/drenaje venoso tiroides .png", "description": "Venous drainage of the thyroid"},
    {"path": "Face and Neck/imagenes/vasculatura toriodes.png", "description": "Thyroid vasculature"},
    {"path": "Face and Neck/imagenes/medial thyoroid.png", "description": "Medial view of the thyroid"},
    {"path": "Face and Neck/imagenes/mosto common variant .png", "description": "Most common variant of thyroid anatomy"}
]

# Crear la tarjeta de aprendizaje
with st.expander(title, expanded=False):
    st.markdown(question, unsafe_allow_html=True)
    st.markdown(answer, unsafe_allow_html=True)

    # Mostrar las imágenes con descripciones si existen
    for image_detail in image_details:
        try:
            st.markdown(f"<b>{image_detail['description']}</b>", unsafe_allow_html=True)
            st.image(image_detail["path"], use_column_width=True)
        except Exception as e:
            st.warning(f"Image '{image_detail['path']}' not found. Please check the file path. Error: {e}")
