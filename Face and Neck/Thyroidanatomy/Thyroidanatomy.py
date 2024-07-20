import streamlit as st

# Función para estilizar el título
def style_title(title):
    return f"<span style='color:darkorange; font-weight:bold;'>{title}</span>"

# Contenido de la flash card (Pregunta y Respuesta)
title = "Vascular Anatomy of the Thyroid Gland and Neck"
question = "What are the primary vascular structures near the thyroid gland and their branches?"
answer = """
- **Primary Vascular Structures:**
  - **Common Carotid Artery:** The most medial vessel, located lateral to the thyroid gland.
  - **Internal Jugular Vein:** Also located lateral to the thyroid gland.

- **Branches of the Common Carotid Artery:**
  - **Internal Carotid Artery:** Branches from the common carotid arteries above the thyroid gland.
  - **External Carotid Artery:** Branches from the common carotid arteries above the thyroid gland.

- **Thyroid Arteries:**
  - **Superior Thyroid Artery:** The first branch of the external carotid artery.
  - **Inferior Thyroid Artery:** A branch of the thyrocervical trunk of the subclavian artery.

- **Thyroid Veins:**
  - These veins drain into the internal jugular vein.
  - Jugular veins are positioned superior and lateral to the common carotid arteries.

**Summary:**
The common carotid artery is the main medial vessel, branching into internal and external carotid arteries. The superior thyroid artery branches from the external carotid, while the inferior thyroid artery comes from the thyrocervical trunk of the subclavian artery. Corresponding thyroid veins drain into the internal jugular veins, which are situated superiorly and laterally to the common carotid arteries.
"""

# Ruta a la imagen dentro de la carpeta 'Face and Neck/Thyroid_Anatomy/images'
image_path = "Face and Neck/Thyroid_Anatomy/images/thyroid_image1.png"

# Crear la flash card con expanders
with st.expander(style_title(title) + " (Q&A)", expanded=True):
    st.markdown(style_title("Question") + ": " + question, unsafe_allow_html=True)
    with st.expander("Show Answer"):
        st.markdown(answer, unsafe_allow_html=True)
        # Mostrar la imagen si existe
        try:
            st.image(image_path, caption="Anatomy Illustration", use_column_width=True)
        except Exception as e:
            st.warning(f"Image not found. Please check the file path. Error: {e}")
