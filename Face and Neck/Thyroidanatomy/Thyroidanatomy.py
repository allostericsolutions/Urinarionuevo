# File: Face and Neck/Thyroidanatomy/Thyroidanatomy.py
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

# Paths to the images within 'Face and Neck/imagenes'
image_paths = [
    "Face and Neck/imagenes/Lateral to the thyoroid.png",
    "Face and Neck/imagenes/drenaje venoso tiroides.png",
    "Face and Neck/imagenes/vasculatura toriodes.png",
    "Face and Neck/imagenes/medial thyoroid.png",
    "Face and Neck/imagenes/mosto common variant.png"
]

# Create the flash card
st.markdown(f"### {title}")
st.markdown(f"**Question:** {question}")
st.markdown(answer)

# Display the images if they exist
for image_path in image_paths:
    try:
        st.image(image_path, use_column_width=True)
    except Exception as e:
        st.warning(f"Image '{image_path}' not found. Please check the file path. Error: {e}")
