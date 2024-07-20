import streamlit as st

# Initialize the variable in session_state
if 'mostrar_signos_tiroides' not in st.session_state:
    st.session_state.mostrar_signos_tiroides = False

# Function to style the sign titles
def style_title(title):
    return f"<span style='color:darkorange; font-weight:bold;'>{title}</span>"

# Expandable and collapsible section
with st.expander("Thyroid Ultrasound Signs:", expanded=st.session_state.mostrar_signos_tiroides):
    st.markdown(style_title("Thyroid Inferno:") + " Refers to the hypervascularity seen within the thyroid gland on color Doppler imaging, often associated with Graves disease.", unsafe_allow_html=True)
    st.markdown(style_title("Comet-tail Artifact:") + " Seen within colloid cysts as a hyperechoic focus or foci that produce a comet-tail effect.", unsafe_allow_html=True)
    st.markdown(style_title("Psammoma Bodies:") + " Round, punctate calcific deposits seen sonographically as punctate, hyperechoic foci without acoustic shadowing.", unsafe_allow_html=True)
    st.markdown(style_title("Eggshell Calcification:") + " Peripheral calcifications of a thyroid nodule appearing like an eggshell, often benign.", unsafe_allow_html=True)
    st.markdown(style_title("Spongiform Appearance:") + " Multiple tiny cystic spaces within a nodule, indicating benignity.", unsafe_allow_html=True)
    st.markdown(style_title("Halo Sign:") + " A hypoechoic ring around a thyroid nodule, suggestive of a benign follicular adenoma.", unsafe_allow_html=True)
    st.markdown(style_title("Microcalcifications:") + " Tiny calcifications within a thyroid nodule, raising suspicion for malignancy, commonly associated with papillary thyroid carcinoma.", unsafe_allow_html=True)
    st.markdown(style_title("Taller-than-Wide Shape:") + " A nodule that is taller than it is wide on transverse measurement, more common in malignant nodules.", unsafe_allow_html=True)
    st.markdown(style_title("Anterior Cervical 'Sandstorm' Sign:") + " Appearance of a sandstorm in Graves disease due to high vascularity.", unsafe_allow_html=True)
    st.markdown(style_title("Hypoechoic Halo:") + " An unusually hypoechoic area around a thyroid nodule, often seen in malignant nodules.", unsafe_allow_html=True)
    st.markdown(style_title("Perinodular Flow:") + " Blood flow observed around the periphery of a nodule, typically benign.", unsafe_allow_html=True)
    st.markdown(style_title("Intralesional Vascularity:") + " Significant blood flow within a nodule, possibly indicating malignancy.", unsafe_allow_html=True)
