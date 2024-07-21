import streamlit as st

# Initialize the variable in session_state
if 'mostrar_eponimos' not in st.session_state:
    st.session_state.mostrar_eponimos = False

# Function to style the eponym titles
def style_title(title):
    return f"<span style='color:darkorange; font-weight:bold;'>{title}</span>"

# Expandable and collapsible section
with st.expander("Clinical and Sonographic Findings of Thyroid Conditions", expanded=st.session_state.mostrar_eponimos):

    # Goiter
    st.markdown(style_title("Goiter:") + " ", unsafe_allow_html=True)
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

    # Graves Disease
    st.markdown(style_title("Graves Disease:") + " ", unsafe_allow_html=True)
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

    # Hashimoto Thyroiditis
    st.markdown(style_title("Hashimoto Thyroiditis:") + " ", unsafe_allow_html=True)
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
    st.markdown(style_title("Benign Thyroid Nodules:") + " ", unsafe_allow_html=True)
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
    st.markdown(style_title("Malignant Thyroid Nodules:") + " ", unsafe_allow_html=True)
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
