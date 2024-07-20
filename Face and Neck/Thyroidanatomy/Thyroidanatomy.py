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

# Path to the image within 'Face and Neck/Thyroidanatomy/imagenes'
image_path = "Face and Neck/Thyroidanatomy/imagenes/thyroid_image1.png"

# Create the flash card
st.markdown(f"### {title}")
st.markdown(f"**Question:** {question}")
st.markdown(answer)

# Display the image if it exists
try:
    st.image(image_path, caption="Anatomy Illustration", use_column_width=True)
except Exception as e:
    st.warning(f"Image not found. Please check the file path. Error: {e}")
