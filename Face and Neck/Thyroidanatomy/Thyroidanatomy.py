import streamlit as st

# Define the content of the flash card
title = "Vascular Anatomy of the Thyroid Gland and Neck"
question = "What are the primary vascular structures near the thyroid gland and their branches?"
answer = """
**Primary Vascular Structures:**
- **Common Carotid Artery:** The most medial vessel, located lateral to the thyroid gland.
- **Internal Jugular Vein:** Also located lateral to the thyroid gland.

**Branches of the Common Carotid Artery:**
- **Internal Carotid Artery:** Branches from the common carotid arteries above the thyroid gland.
- **External Carotid Artery:** Branches from the common carotid arteries above the thyroid gland.

**Thyroid Arteries:**
- **Superior Thyroid Artery:** The first branch of the external carotid artery.
- **Inferior Thyroid Artery:** A branch of the thyrocervical trunk of the subclavian artery.

**Thyroid Veins:**
- These veins drain into the internal jugular vein.
- Jugular veins are positioned superior and lateral to the common carotid arteries.

**Summary:**
The common carotid artery is the main medial vessel, branching into internal and external carotid arteries. The superior thyroid artery branches from the external carotid, while the inferior thyroid artery comes from the thyrocervical trunk of the subclavian artery. Corresponding thyroid veins drain into the internal jugular veins, which are situated superiorly and laterally to the common carotid arteries.
"""

# Image details
image_details = [
    {"path": "Face and Neck/imagenes/Lateral to the thyoroid.png", "description": "Lateral view of the thyroid"},
    {"path": "Face and Neck/imagenes/drenaje venoso tiroides .png", "description": "Venous drainage of the thyroid"},
    {"path": "Face and Neck/imagenes/vasculatura toriodes.png", "description": "Thyroid vasculature"},
    {"path": "Face and Neck/imagenes/medial thyoroid.png", "description": "Medial view of the thyroid"},
    {"path": "Face and Neck/imagenes/mosto common variant .png", "description": "Most common variant of thyroid anatomy"}
]

# Create the flash card
with st.expander(f"<h3 style='color: orange;'>{title}</h3>", expanded=False):
    st.markdown(f"<h4 style='color: orange;'>Question: {question}</h4>", unsafe_allow_html=True)
    st.markdown(f"<div style='color: white;'>{answer}</div>", unsafe_allow_html=True)

    # Display the images with descriptions if they exist
    for image_detail in image_details:
        try:
            st.markdown(f"<b style='color: white;'>{image_detail['description']}</b>", unsafe_allow_html=True)
            st.image(image_detail["path"], use_column_width=True)
        except Exception as e:
            st.warning(f"Image '{image_detail['path']}' not found. Please check the file path. Error: {e}")
