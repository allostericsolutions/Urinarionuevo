import streamlit as st

# Función para estilizar el título de las secciones
def style_title(title):
    return f"<span style='color:darkorange; font-weight:bold;'>{title}</span>"

# Crear la categoría principal
with st.expander("Clinical and Sonographic Findings of Thyroid Conditions", expanded=False):
    
    # Findings of a Goiter
    with st.expander(style_title("Goiter"), expanded=False):
        st.markdown("#### Clinical Findings")
        st.markdown("""
        - Palpable (and possibly visually) enlarged thyroid gland
        - Dyspnea (difficulty breathing)
        - Dysphagia (difficulty swallowing)
        - Feeling of tightening in the throat
        - Coughing
        - Hoarseness
        """, unsafe_allow_html=True)

        st.markdown("#### Sonographic Findings")
        st.markdown("""
        - Enlarged thyroid gland (isthmus that exceeds 1 cm in the anteroposterior plane)
        - Diffusely heterogeneous echotexture
        - Multiple nodules with cystic and solid components
        """, unsafe_allow_html=True)
    
    # Findings of Graves Disease
    with st.expander(style_title("Graves Disease"), expanded=False):
        st.markdown("#### Clinical Findings")
        st.markdown("""
        - Bulging eyes (exophthalmos)
        - Heat intolerance
        - Nervousness
        - Weight loss (with increased appetite)
        - Hair loss
        - Tachycardia, palpitations, high-output heart failure
        - Muscle wasting
        - Fine tremors
        - Oligomenorrhea (infrequent menstrual periods)
        - Pretibial myxedema
        """, unsafe_allow_html=True)

        st.markdown("#### Sonographic Findings")
        st.markdown("""
        - Enlarged gland
        - Heterogeneous or diffusely hypoechoic echotexture
        - Thyroid inferno (increased blood flow on Doppler)
        """, unsafe_allow_html=True)
    
    # Findings of Hashimoto Thyroiditis
    with st.expander(style_title("Hashimoto Thyroiditis"), expanded=False):
        st.markdown("#### Clinical Findings")
        st.markdown("""
        - Depression
        - Increased cold sensitivity
        - Elevated blood cholesterol levels
        - Slight weight gain may occur
        - Puffy face and puffiness under the eyes
        - Menorrhagia (heavy menstrual bleeding)
        - Pallor (pale skin)
        """, unsafe_allow_html=True)

        st.markdown("#### Sonographic Findings")
        st.markdown("""
        - Mild enlargement of the thyroid gland (initially)
        - Heterogeneous echotexture
        - Multiple, ill-defined hypoechoic regions separated by fibrous hyperechoic tissue
        - Hypervascular gland
        """, unsafe_allow_html=True)

    # Benign Thyroid Nodules
    with st.expander(style_title("Benign Thyroid Nodules"), expanded=False):
        st.markdown("Thyroid nodules are exceedingly common, with up to 68% of all adults having sonographically identifiable thyroid nodules.")
        
        st.markdown("#### Types of Benign Nodules")
        st.markdown("""
        - Follicular adenomas: Small, round, and may be anechoic, isoechoic, or hyperechoic.
        - Nodular hyperplasia: The most common cause of thyroid nodules.
        - Hyperplastic nodules: Often multiple and with varying appearances.
        """)

        st.markdown("#### Sonographic Features")
        st.markdown("""
        - Extensive cystic components
        - Cysts <5 mm
        - Hyperechoic mass
        - “Eggshell” calcifications
        - Spongiform composition
        - Wider-than-tall shape
        - “Hot” nodule (nuclear medicine finding)
        """)

    # Malignant Thyroid Nodules
    with st.expander(style_title("Malignant Thyroid Nodules"), expanded=False):
        st.markdown("Papillary carcinoma is the most common form of thyroid cancer, though other forms include follicular carcinoma, medullary carcinoma, anaplastic carcinoma, lymphoma, and metastases.")
        
        st.markdown("#### Sonographic Features of Malignant Nodules")
        st.markdown("""
        - Hypoechoic mass
        - Taller-than-wide shape
        - Mass with internal microcalcifications (psammoma bodies)
        - Solitary mass
        - Marked vascularity within the central part of the nodule
        - Interrupted peripheral calcification
        - Extracapsular invasion
        - Lobulated margins
        - Enlargement of the cervical lymph nodes (metastasis)
        - “Cold” nodule (nuclear medicine finding)
        """)

# Ejecutar la aplicación Streamlit
if __name__ == "__main__":
    st.run()
