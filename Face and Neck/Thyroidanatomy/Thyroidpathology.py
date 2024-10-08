import streamlit as st

# Initialize the variable in session_state
if 'show_eponyms' not in st.session_state:
    st.session_state.show_eponyms = False

# Function to style the eponym titles
def style_title(title):
    return f"<span style='color:darkorange; font-weight:bold;'>{title}</span>"

# Expandable and collapsible section
with st.expander("Clinical and Sonographic Findings of Thyroid Conditions", expanded=st.session_state.show_eponyms):

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

    # General Considerations
    st.markdown(style_title("General Considerations:") + " ", unsafe_allow_html=True)
    st.markdown("""
    - **Ultrasound is the most cost-effective imaging test for the thyroid.** 
    - **It is operator-dependent and uses equipment with high-resolution transducers and color Doppler.**
    - **Recommendations for thyroid ultrasound:**
        - Patients with goiter
        - Palpable nodules
        - Family history of thyroid cancer
        - History of cervical radiation in childhood
    - **Suspicious characteristics of malignancy:**
        - Solid nodules with marked hypoechogenicity
        - Taller than wide
        - Lobulated or spiculated edges
        - Presence of microcalcifications
    - **Ultrasound is essential in:**
        - Detecting nodules
        - Obtaining samples for cytopathological study
        - Pre-operative staging
        - Post-operative monitoring to detect early cervical recurrences
    - **Ultrasound is useful for:**
        - Diagnosing and monitoring benign diffuse and nodular thyroid diseases
        - Supporting minimally invasive treatments
    """, unsafe_allow_html=True)

    # Ultrasound Technique
    st.markdown(style_title("Ultrasound Technique") + " ", unsafe_allow_html=True)
    st.markdown("""
    - **Ultrasound probes:** Linear, 3.5 to 5 cm in length, with frequencies between 5 and 17 MHz.
    - **Patient position:** Supine with neck hyperextension (adjust position if needed).
    - **Gel is used:** Allows transducer movement and improves image quality.
    - **Compression is not necessary:** It can worsen image quality.
    - **Ultrasound provides:**
        - General morphology: Presence, position, size, shape, contours, borders
        - Specific morphology: Echogenicity and echotexture of the gland and nodules
        - Doppler: Information on vascularization of normal and pathological tissue
    - **Measurements:**
        - Lobes: Right and left lobes in three axes
        - Isthmus: Anteroposterior axis
        - Pyramidal lobe: Anteroposterior and transverse axes
    """, unsafe_allow_html=True)

    # Indications for Thyroid Ultrasound
    st.markdown(style_title("Indications for Thyroid Ultrasound") + " ", unsafe_allow_html=True)
    st.markdown("""
    - Goiter
    - Palpable or visible nodule
    - Dysphagia
    - Chronic cough
    - Dysphonia
    - Cervical pain
    - Family history of thyroid cancer
    - History of cervical radiation in childhood or adolescence
    - Genetic syndromes
    - Complementary examination for thyroid pathology detected in other cervical exams (Carotid Doppler, CT or MRI of the cervical spine, PET, etc.)
    """, unsafe_allow_html=True)

    # Normal and Pathological Thyroid
    st.markdown(style_title("Normal and Pathological Thyroid") + " ", unsafe_allow_html=True)
    st.markdown("""
    - **Normal thyroid:**
        - Shape: H-shaped (butterfly)
        - Lobes: Right and left lobes with predominant craniocaudal axis, smooth contours, and sharp borders.
        - Isthmus: Predominant longitudinal axis, with anteroposterior diameter not exceeding 3 mm.
        - Pyramidal lobe: Normal variant, usually dependent on the isthmus.
    - **Thyroid abnormalities:**
        - Absence: Rare, can cause neurological development problems.
        - Hemiagenesis: Rare, often with preserved function.
        - Decreased size: Often due to chronic inflammatory processes.
        - Goiter: Diffuse or nodular enlargement, a common cause of medical consultation.
    - **Echogenicity and Echotexture:**
        - Normal: Isoechoic and homogeneous.
        - Hypoechogenicity: Most common alteration in echogenicity.
        - Heterogeneity: Always indicates pathology and may be associated with altered echogenicity.
    - **Nodules:**
        - Can be solid (isoechoic, hypoechoic, or hyperechoic), cystic (anechoic or hypoechoic), or mixed.
        - Ultrasound should describe location, size, number, echogenicity, echotexture, borders, calcifications, and vascularization.
    """, unsafe_allow_html=True)

    # Sonographic Signs of Malignancy in Thyroid Nodules
    st.markdown(style_title("Sonographic Signs of Malignancy in Thyroid Nodules") + " ", unsafe_allow_html=True)
    st.markdown("""
    - **Suspicious features of malignancy:**
        - Solid nodule with marked hypoechogenicity
        - Taller than wide
        - Irregular, microlobulated, or spiculated borders
        - Microcalcifications
    - **Other features:**
        - Heterogeneity
        - Solid nature
        - Poorly defined contours
    - **Puncture recommendations:**
        - Solid nodules larger than 10 mm in diameter
        - Solid-cystic nodules larger than 20 mm
    - **The more malignancy criteria present, the higher the probability of malignancy.**
    """, unsafe_allow_html=True)

    # Fine-Needle Aspiration Biopsy (FNAB) under Ultrasound Guidance
    st.markdown(style_title("Fine-Needle Aspiration Biopsy (FNAB) under Ultrasound Guidance") + " ", unsafe_allow_html=True)
    st.markdown("""
    - Fine-needle aspiration biopsy (FNAB) is performed under ultrasound guidance.
    - Real-time ultrasound guidance improves sample quality and reduces risks.
    - It is important to check for suspicious lymph nodes.
    """, unsafe_allow_html=True)

    # Preoperative Staging Cervical Ultrasound
    st.markdown(style_title("Preoperative Staging Cervical Ultrasound") + " ", unsafe_allow_html=True)
    st.markdown("""
    - **Ultrasound is a valuable tool for pre-operative staging of thyroid cancer.**
    - It provides information about the size of the thyroid, location of the malignancy, extent of tumor invasion, suspicious lymph nodes, and other cervical masses.
    - **Doppler studies:** Help confirm tumor thrombosis in the internal jugular veins.
    """, unsafe_allow_html=True)

    # Post-Thyroidectomy Monitoring
    st.markdown(style_title("Post-Thyroidectomy Monitoring") + " ", unsafe_allow_html=True)
    st.markdown("""
    - **Post-operative monitoring:**
        - Ultrasound at 6 months or 1 year unless immediate or recent post-operative complications are suspected.
    - **Examination areas:**
        - Thyroid projection site
        - Carotid compartments
        - Submandibular regions
        - Parotid tail
    - **Looking for:**
        - Residual glandular tissue
        - Recurrence
        - Calcified granulomas in the thyroid bed
    - **Anechoic or hypoechoic nodules in the thyroid bed:** May indicate recurrence.
    - **Suspicious lymph nodes:** Puncture and measure thyroglobulin and anti-thyroglobulin antibodies.
    - **Post-thyroidectomy patients without signs of recurrence:** Regular monitoring with increasing intervals.
    """, unsafe_allow_html=True)

    # Diffuse Goiter
    st.markdown(style_title("Diffuse Goiter") + " ", unsafe_allow_html=True)
    st.markdown("""
    - **Diffuse goiter:** Usually due to non-neoplastic pathology (endemic goiter, Graves' disease, thyroiditis).
    - **Ultrasound:** Sensitive but not specific for diagnosis.
    - **Thyroid inflammation:** Typically manifests as parenchymal hypoechogenicity, homogeneous or heterogeneous, often with increased vascularization.
    - **Pseudonodules:** May be present in chronic thyroiditis, frequently hyperechoic, homogeneous, partially delineated, with peripheral vascularization, without acoustic shadow or posterior reinforcement of sound. 
    - **Lymphomatous involvement:** Presents as diffuse goiter, markedly hypoechoic, heterogeneous, hypervascular, often associated with pathological cervical lymph nodes. 
    """, unsafe_allow_html=True)

    # Ultrasound-Guided Ablation of Benign Thyroid Nodules
    st.markdown(style_title("Ultrasound-Guided Ablation of Benign Thyroid Nodules") + " ", unsafe_allow_html=True)
    st.markdown("""
    - **Minimally invasive procedures:** Increasingly used for non-malignant thyroid conditions.
    - **Cyst aspiration:** Not definitive treatment due to high recurrence rate.
    - **Ethanol ablation:** Good results for recurrent cysts, but not frequently used.
    - **Radiofrequency ablation:** Alternative for solid nodules, indicated for nodules with confirmed benignity, measuring up to 50 mm in diameter.
    """, unsafe_allow_html=True)

    # Future Perspective
    st.markdown(style_title("Future Perspective") + " ", unsafe_allow_html=True)
    st.markdown("""
    - **Ultrasound remains a challenging but valuable tool.**
    - **Minimally invasive treatments are increasingly used.**
    - **Importance of training:** Ensure adequate training for professionals performing ultrasound examinations. 
    """, unsafe_allow_html=True)
