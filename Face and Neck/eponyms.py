import streamlit as st

# Initialize the variable in session_state
if 'mostrar_eponimos' not in st.session_state:
    st.session_state.mostrar_eponimos = False

# Function to style the eponym titles
def style_title(title):
    return f"<span style='color:darkorange; font-weight:bold;'>{title}</span>"

# Expandable and collapsible section
with st.expander("Eponyms in Thyroid and Neck Pathology:", expanded=st.session_state.mostrar_eponimos):
    st.markdown(style_title("Graves Disease:") + " The most common cause of hyperthyroidism that produces bulging eyes, heat intolerance, nervousness, weight loss, and hair loss.", unsafe_allow_html=True)
    st.markdown(style_title("Hashimoto Thyroiditis:") + " The most common cause of hypothyroidism in the United States.", unsafe_allow_html=True)
    st.markdown(style_title("Sjögren Syndrome:") + " An autoimmune disease that affects all glands that produce moisture, leading to dysfunction of the salivary glands and severe dryness of the eyes, nose, skin, and mouth.", unsafe_allow_html=True)
    st.markdown(style_title("Stensen Duct:") + " The main duct of the parotid gland.", unsafe_allow_html=True)
    st.markdown(style_title("Wharton Duct:") + " The duct that drains the submandibular gland.", unsafe_allow_html=True)
    st.markdown(style_title("Cold Nodules:") + " The hypofunctioning thyroid nodules seen on a nuclear medicine study that have malignant potential.", unsafe_allow_html=True)
    st.markdown(style_title("Cystic Hygroma:") + " May also refer to a lymphangioma.", unsafe_allow_html=True)
    st.markdown(style_title("Exophthalmos:") + " Bulging eyes.", unsafe_allow_html=True)
    st.markdown(style_title("Hot Nodules:") + " The hyperfunctioning thyroid nodules seen on a nuclear medicine study that are almost always benign.", unsafe_allow_html=True)
    st.markdown(style_title("Pretibial Myxedema:") + " Clinical finding associated with Graves disease in which there is thickening of the skin and edema on the anterior legs.", unsafe_allow_html=True)
    st.markdown(style_title("Psammoma Bodies:") + " Round, punctate calcific deposits.", unsafe_allow_html=True)
    st.markdown(style_title("Punctate:") + " Marked with dots.", unsafe_allow_html=True)
    st.markdown(style_title("Pyramidal Lobe:") + " A normal variant of the thyroid gland in which there is a superior extension of the isthmus.", unsafe_allow_html=True)
    st.markdown(style_title("Thyroid Inferno:") + " The sonographic appearance of hypervascularity demonstrated with color Doppler imaging of the thyroid gland.", unsafe_allow_html=True)
    st.markdown(style_title("Torticollis:") + " Twisted neck.", unsafe_allow_html=True)
