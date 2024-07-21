import streamlit as st

# Initialize the variable in session_state
if 'mostrar_eponimos' not in st.session_state:
    st.session_state.mostrar_eponimos = False

# Function to style the eponym titlesimport streamlit as st

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
    st.image("https://static.elsevier.es/multimedia/07168640/0000002900000004/v4_201810230604/S071686401830083X/v4_201810230604/es/main.assets/gr1.jpeg?xkr=ue/ImdikoIMrsJoerZ+w997EogCnBdOOD93cPFbanNd2Vt2E9KIXSbfPNY5VCUB4kpCjPTZRm5n9r2Wgu2xKnaaLdMEH3EdygauzKlTyPTyhRP+tDkOLS79kLGbGk8d1oJdnmsF+0Z5YKEobFo2Z0StElaHQ/Zxzln4bsZr6SpIGyECJo3zN5e9MhSBTLGEIyh1iHSnNaDvwSThBeYb13Dl4mQuzAF0rIOYrRbqsEElCtLgsStdEbPvnKVXxcLi47ubDcRK6hoXBs8nEcD6h2JNM9FHOQK4L++jZQDRQQi3lrJdc8vWmXUrOzxvZ7LNG", caption="Goiter: Enlarged thyroid gland with heterogeneous echotexture.") # Image URL for Goiter

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
    st.image("https://static.elsevier.es/multimedia/07168640/0000002900000004/v4_201810230604/S071686401830083X/v4_201810230604/es/main.assets/gr2.jpeg?xkr=ue/ImdikoIMrsJoerZ+w997EogCnBdOOD93cPFbanNd2Vt2E9KIXSbfPNY5VCUB4kpCjPTZRm5n9r2Wgu2xKnaaLdMEH3EdygauzKlTyPTyhRP+tDkOLS79kLGbGk8d1oJdnmsF+0Z5YKEobFo2Z0StElaHQ/Zxzln4bsZr6SpIGyECJo3zN5e9MhSBTLGEIyh1iHSnNaDvwSThBeYb13Dl4mQuzAF0rIOYrRbqsEElCtLgsStdEbPvnKVXxcLi47ubDcRK6hoXBs8nEcD6h2JNM9FHOQK4L++jZQDRQQi3lrJdc8vWmXUrOzxvZ7LNG", caption="Graves Disease: Enlarged gland with heterogeneous echotexture.") # Image URL for Graves Disease

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
    st.image("https://static.elsevier.es/multimedia/07168640/0000002900000004/v4_201810230604/S071686401830083X/v4_201810230604/es/main.assets/gr3.jpeg?xkr=ue/ImdikoIMrsJoerZ+w997EogCnBdOOD93cPFbanNd2Vt2E9KIXSbfPNY5VCUB4kpCjPTZRm5n9r2Wgu2xKnaaLdMEH3EdygauzKlTyPTyhRP+tDkOLS79kLGbGk8d1oJdnmsF+0Z5YKEobFo2Z0StElaHQ/Zxzln4bsZr6SpIGyECJo3zN5e9MhSBTLGEIyh1iHSnNaDvwSThBeYb13Dl4mQuzAF0rIOYrRbqsEElCtLgsStdEbPvnKVXxcLi47ubDcRK6hoXBs8nEcD6h2JNM9FHOQK4L++jZQDRQQi3lrJdc8vWmXUrOzxvZ7LNG", caption="Hashimoto Thyroiditis: Mild enlargement of the thyroid gland with heterogeneous echotexture.") # Image URL for Hashimoto Thyroiditis

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
    st.image("https://static.elsevier.es/multimedia/07168640/0000002900000004/v4_201810230604/S071686401830083X/v4_201810230604/es/main.assets/gr4.jpeg?xkr=ue/ImdikoIMrsJoerZ+w997EogCnBdOOD93cPFbanNd2Vt2E9KIXSbfPNY5VCUB4kpCjPTZRm5n9r2Wgu2xKnaaLdMEH3EdygauzKlTyPTyhRP+tDkOLS79kLGbGk8d1oJdnmsF+0Z5YKEobFo2Z0StElaHQ/Zxzln4bsZr6SpIGyECJo3zN5e9MhSBTLGEIyh1iHSnNaDvwSThBeYb13Dl4mQuzAF0rIOYrRbqsEElCtLgsStdEbPvnKVXxcLi47ubDcRK6hoXBs8nEcD6h2JNM9FHOQK4L++jZQDRQQi3lrJdc8vWmXUrOzxvZ7LNG", caption="Benign Thyroid Nodules: Sonographic features include cystic components, hyperechoic mass, and wider-than-tall shape.") # Image URL for Benign Thyroid Nodules

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
    st.image("https://static.elsevier.es/multimedia/07168640/0000002900000004/v4_201810230604/S071686401830083X/v4_201810230604/es/main.assets/gr5.jpeg?xkr=ue/ImdikoIMrsJoerZ+w997EogCnBdOOD93cPFbanNd2Vt2E9KIXSbfPNY5VCUB4kpCjPTZRm5n9r2Wgu2xKnaaLdMEH3EdygauzKlTyPTyhRP+tDkOLS79kLGbGk8d1oJdnmsF+0Z5YKEobFo2Z0StElaHQ/Zxzln4bsZr6SpIGyECJo3zN5e9MhSBTLGEIyh1iHSnNaDvwSThBeYb13Dl4mQuzAF0rIOYrRbqsEElCtLgsStdEbPvnKVXxcLi47ubDcRK6hoXBs8nEcD6h2JNM9FHOQK4L++jZQDRQQi3lrJdc8vWmXUrOzxvZ7LNG", caption="Malignant Thyroid Nodules: Sonographic features include hypoechoic mass, taller-than-wide shape, and microcalcifications.") # Image URL for Malignant Thyroid Nodules


    # Generalidades
    st.markdown(style_title("Generalidades:") + " ", unsafe_allow_html=True)
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

    # Técnica Ecográfica
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

    # Indicaciones de la Ecografía Tiroidea
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

    # El Tiroides Normal y Patológico
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

    st.markdown("## Imágenes:")

    st.markdown("**Figura 1:** Normal thyroid: Thyroid lobe in longitudinal section, homogeneous parenchyma, normal echogenicity, normal shape and size.")
    st.image("https://static.elsevier.es/multimedia/07168640/0000002900000004/v4_201810230604/S071686401830083X/v4_201810230604/es/main.assets/gr1.jpeg?xkr=ue/ImdikoIMrsJoerZ+w997EogCnBdOOD93cPFbanNd2Vt2E9KIXSbfPNY5VCUB4kpCjPTZRm5n9r2Wgu2xKnaaLdMEH3EdygauzKlTyPTyhRP+tDkOLS79kLGbGk8d1oJdnmsF+0Z5YKEobFo2Z0StElaHQ/Zxzln4bsZr6SpIGyECJo3zN5e9MhSBTLGEIyh1iHSnNaDvwSThBeYb13Dl4mQuzAF0rIOYrRbqsEElCtLgsStdEbPvnKVXxcLi47ubDcRK6hoXBs8nEcD6h2JNM9FHOQK4L++jZQDRQQi3lrJdc8vWmXUrOzxvZ7LNG")

    st.markdown("**Figura 2:** Normal thyroid: Thyroid in a transverse section. The isthmus of normal thickness measures 2.3mm anteroposterior diameter.")
    st.image("https://static.elsevier.es/multimedia/07168640/0000002900000004/v4_201810230604/S071686401830083X/v4_201810230604/es/main.assets/gr2.jpeg?xkr=ue/ImdikoIMrsJoerZ+w997EogCnBdOOD93cPFbanNd2Vt2E9KIXSbfPNY5VCUB4kpCjPTZRm5n9r2Wgu2xKnaaLdMEH3EdygauzKlTyPTyhRP+tDkOLS79kLGbGk8d1oJdnmsF+0Z5YKEobFo2Z0StElaHQ/Zxzln4bsZr6SpIGyECJo3zN5e9MhSBTLGEIyh1iHSnNaDvwSThBeYb13Dl4mQuzAF0rIOYrRbqsEElCtLgsStdEbPvnKVXxcLi47ubDcRK6hoXBs8nEcD6h2JNM9FHOQK4L++jZQDRQQi3lrJdc8vWmXUrOzxvZ7LNG")

    st.markdown("**Figura 3:**  Normal thyroid: Left photo: transverse section: the pyramidal lobe in right paramedian location (arrowhead). Right photo: longitudinal section: the left pre-laryngeal pyramidal lobe imperceptibly continues with the isthmus (c: cranial; i: isthmus).")
    st.image("https://static.elsevier.es/multimedia/07168640/0000002900000004/v4_201810230604/S071686401830083X/v4_201810230604/es/main.assets/gr3.jpeg?xkr=ue/ImdikoIMrsJoerZ+w997EogCnBdOOD93cPFbanNd2Vt2E9KIXSbfPNY5VCUB4kpCjPTZRm5n9r2Wgu2xKnaaLdMEH3EdygauzKlTyPTyhRP+tDkOLS79kLGbGk8d1oJdnmsF+0Z5YKEobFo2Z0StElaHQ/Zxzln4bsZr6SpIGyECJo3zN5e9MhSBTLGEIyh1iHSnNaDvwSThBeYb13Dl4mQuzAF0rIOYrRbqsEElCtLgsStdEbPvnKVXxcLi47ubDcRK6hoXBs8nEcD6h2JNM9FHOQK4L++jZQDRQQi3lrJdc8vWmXUrOzxvZ7LNG")

    st.markdown("**Figura 4:**  Hemiagenesis of the left thyroid lobe: Patient without surgical history. There is no paratracheal left glandular parenchyma. In this case, the isthmus is present.")
    st.image("https://static.elsevier.es/multimedia/07168640/0000002900000004/v4_201810230604/S071686401830083X/v4_201810230604/es/main.assets/gr4.jpeg?xkr=ue/ImdikoIMrsJoerZ+w997EogCnBdOOD93cPFbanNd2Vt2E9KIXSbfPNY5VCUB4kpCjPTZRm5n9r2Wgu2xKnaaLdMEH3EdygauzKlTyPTyhRP+tDkOLS79kLGbGk8d1oJdnmsF+0Z5YKEobFo2Z0StElaHQ/Zxzln4bsZr6SpIGyECJo3zN5e9MhSBTLGEIyh1iHSnNaDvwSThBeYb13Dl4mQuzAF0rIOYrRbqsEElCtLgsStdEbPvnKVXxcLi47ubDcRK6hoXBs8nEcD6h2JNM9FHOQK4L++jZQDRQQi3lrJdc8vWmXUrOzxvZ7LNG")

    st.markdown("**Figura 5:**  Goiter. A: Thyroid in a longitudinal section, globose increased in size, gently lobulated contours, hypoechoic parenchyma, heterogeneous, without images of nodules in its thickness. ")
    st.image("https://static.elsevier.es/multimedia/07168640/0000002900000004/v4_201810230604/S071686401830083X/v4_201810230604/es/main.assets/gr5.jpeg?xkr=ue/ImdikoIMrsJoerZ+w997EogCnBdOOD93cPFbanNd2Vt2E9KIXSbfPNY5VCUB4kpCjPTZRm5n9r2Wgu2xKnaaLdMEH3EdygauzKlTyPTyhRP+tDkOLS79kLGbGk8d1oJdnmsF+0Z5YKEobFo2Z0StElaHQ/Zxzln4bsZr6SpIGyECJo3zN5e9MhSBTLGEIyh1iHSnNaDvwSThBeYb13Dl4mQuzAF0rIOYrRbqsEElCtLgsStdEbPvnKVXxcLi47ubDcRK6hoXBs8nEcD6h2JNM9FHOQK4L++jZQDRQQi3lrJdc8vWmXUrOzxvZ7LNG")

    st.markdown("**Figura 5:**  B: Thyroid in a longitudinal section, globose increased in size, lobulated contours, hypoechoic, heterogeneous, with solid nodules of different sizes.")
    st.image("https://static.elsevier.es/multimedia/07168640/0000002900000004/v4_201810230604/S071686401830083X/v4_201810230604/es/main.assets/gr6.jpeg?xkr=ue/ImdikoIMrsJoerZ+w997EogCnBdOOD93cPFbanNd2Vt2E9KIXSbfPNY5VCUB4kpCjPTZRm5n9r2Wgu2xKnaaLdMEH3EdygauzKlTyPTyhRP+tDkOLS79kLGbGk8d1oJdnmsF+0Z5YKEobFo2Z0StElaHQ/Zxzln4bsZr6SpIGyECJo3zN5e9MhSBTLGEIyh1iHSnNaDvwSThBeYb13Dl4mQuzAF0rIOYrRbqsEElCtLgsStdEbPvnKVXxcLi47ubDcRK6hoXBs8nEcD6h2JNM9FHOQK4L++jZQDRQQi3lrJdc8vWmXUrOzxvZ7LNG")

    st.markdown("**Figura 6:** Thyroid nodules. A: On the left, a solid thyroid nodule, isoechoic (same echogenicity as the rest of the lobe) and on the right, the image of a hypoechoic nodule (darker than the rest of the surrounding normal thyroid tissue), in this case with some thick calcifications (white images of eccentric location, upper right). ")
    st.image("https://static.elsevier.es/multimedia/07168640/0000002900000004/v4_201810230604/S071686401830083X/v4_201810230604/es/main.assets/gr7.jpeg?xkr=ue/ImdikoIMrsJoerZ+w997EogCnBdOOD93cPFbanNd2Vt2E9KIXSbfPNY5VCUB4kpCjPTZRm5n9r2Wgu2xKnaaLdMEH3EdygauzKlTyPTyhRP+tDkOLS79kLGbGk8d1oJdnmsF+0Z5YKEobFo2Z0StElaHQ/Zxzln4bsZr6SpIGyECJo3zN5e9MhSBTLGEIyh1iHSnNaDvwSThBeYb13Dl4mQuzAF0rIOYrRbqsEElCtLgsStdEbPvnKVXxcLi47ubDcRK6hoXBs8nEcD6h2JNM9FHOQK4L++jZQDRQQi3lrJdc8vWmXUrOzxvZ7LNG")

    st.markdown("**Figura 6:**  B: Longitudinal ultrasound section of a thyroid nodule: solid, hyperechoic, well-defined, without calcifications.")
    st.image("https://static.elsevier.es/multimedia/07168640/0000002900000004/v4_201810230604/S071686401830083X/v4_201810230604/es/main.assets/gr8.jpeg?xkr=ue/ImdikoIMrsJoerZ+w997EogCnBdOOD93cPFbanNd2Vt2E9KIXSbfPNY5VCUB4kpCjPTZRm5n9r2Wgu2xKnaaLdMEH3EdygauzKlTyPTyhRP+tDkOLS79kLGbGk8d1oJdnmsF+0Z5YKEobFo2Z0StElaHQ/Zxzln4bsZr6SpIGyECJo3zN5e9MhSBTLGEIyh1iHSnNaDvwSThBeYb13Dl4mQuzAF0rIOYrRbqsEElCtLgsStdEbPvnKVXxcLi47ubDcRK6hoXBs8nEcD6h2JNM9FHOQK4L++jZQDRQQi3lrJdc8vWmXUrOzxvZ7LNG")

    st.markdown("**Figura 6:**  C: Cystic thyroid nodule (anechoic): ultrasound passes through the liquid structure without generating echoes and immediately dorsal to the cyst there is an ultrasound reinforcement, due to greater availability of energy to emit more echoes.")
    st.image("https://static.elsevier.es/multimedia/07168640/0000002900000004/v4_201810230604/S071686401830083X/v4_201810230604/es/main.assets/gr9.jpeg?xkr=ue/ImdikoIMrsJoerZ+w997EogCnBdOOD93cPFbanNd2Vt2E9KIXSbfPNY5VCUB4kpCjPTZRm5n9r2Wgu2xKnaaLdMEH3EdygauzKlTyPTyhRP+tDkOLS79kLGbGk8d1oJdnmsF+0Z5YKEobFo2Z0StElaHQ/Zxzln4bsZr6SpIGyECJo3zN5e9MhSBTLGEIyh1iHSnNaDvwSThBeYb13Dl4mQuzAF0rIOYrRbqsEElCtLgsStdEbPvnKVXxcLi47ubDcRK6hoXBs8nEcD6h2JNM9FHOQK4L++jZQDRQQi3lrJdc8vWmXUrOzxvZ7LNG")

    st.markdown("**Figura 6:**  D: Solid cystic thyroid nodule (or mixed), surrounded by a hypoechoic halo. The peripheral portion of the nodule is solid, isoechoic and the center is liquid (anechoic).")
    st.image("https://static.elsevier.es/multimedia/07168640/0000002900000004/v4_201810230604/S071686401830083X/v4_201810230604/es/main.assets/gr10.jpeg?xkr=ue/ImdikoIMrsJoerZ+w997EogCnBdOOD93cPFbanNd2Vt2E9KIXSbfPNY5VCUB4kpCjPTZRm5n9r2Wgu2xKnaaLdMEH3EdygauzKlTyPTyhRP+tDkOLS79kLGbGk8d1oJdnmsF+0Z5YKEobFo2Z0StElaHQ/Zxzln4bsZr6SpIGyECJo3zN5e9MhSBTLGEIyh1iHSnNaDvwSThBeYb13Dl4mQuzAF0rIOYrRbqsEElCtLgsStdEbPvnKVXxcLi47ubDcRK6hoXBs8nEcD6h2JNM9FHOQK4L++jZQDRQQi3lrJdc8vWmXUrOzxvZ7LNG")

    st.markdown("**Figura 7:**  Thyroid nodules with sonographic characteristics of malignancy. A: Solid thyroid nodule, markedly hypoechoic, also presents peripheral microcalcifications (papillary Ca). ")
    st.image("https://static.elsevier.es/multimedia/07168640/0000002900000004/v4_201810230604/S071686401830083X/v4_201810230604/es/main.assets/gr11.jpeg?xkr=ue/ImdikoIMrsJoerZ+w997EogCnBdOOD93cPFbanNd2Vt2E9KIXSbfPNY5VCUB4kpCjPTZRm5n9r2Wgu2xKnaaLdMEH3EdygauzKlTyPTyhRP+tDkOLS79kLGbGk8d1oJdnmsF+0Z5YKEobFo2Z0StElaHQ/Zxzln4bsZr6SpIGyECJo3zN5e9MhSBTLGEIyh1iHSnNaDvwSThBeYb13Dl4mQuzAF0rIOYrRbqsEElCtLgsStdEbPvnKVXxcLi47ubDcRK6hoXBs8nEcD6h2JNM9FHOQK4L++jZQDRQQi3lrJdc8vWmXUrOzxvZ7LNG")

    st.markdown("**Figura 7:**  B: Solid thyroid nodule higher than wide: anteroposterior diameter (height) greater than longitudinal diameter (width). (papillary Ca).")
    st.image("https://static.elsevier.es/multimedia/07168640/0000002900000004/v4_201810230604/S071686401830083X/v4_201810230604/es/main.assets/gr12.jpeg?xkr=ue/ImdikoIMrsJoerZ+w997EogCnBdOOD93cPFbanNd2Vt2E9KIXSbfPNY5VCUB4kpCjPTZRm5n9r2Wgu2xKnaaLdMEH3EdygauzKlTyPTyhRP+tDkOLS79kLGbGk8d1oJdnmsF+0Z5YKEobFo2Z0StElaHQ/Z

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
    st.image("https://static.elsevier.es/multimedia/07168640/0000002900000004/v4_201810230604/S071686401830083X/v4_201810230604/es/main.assets/gr1.jpeg?xkr=ue/ImdikoIMrsJoerZ+w997EogCnBdOOD93cPFbanNd2Vt2E9KIXSbfPNY5VCUB4kpCjPTZRm5n9r2Wgu2xKnaaLdMEH3EdygauzKlTyPTyhRP+tDkOLS79kLGbGk8d1oJdnmsF+0Z5YKEobFo2Z0StElaHQ/Zxzln4bsZr6SpIGyECJo3zN5e9MhSBTLGEIyh1iHSnNaDvwSThBeYb13Dl4mQuzAF0rIOYrRbqsEElCtLgsStdEbPvnKVXxcLi47ubDcRK6hoXBs8nEcD6h2JNM9FHOQK4L++jZQDRQQi3lrJdc8vWmXUrOzxvZ7LNG", caption="Goiter: Enlarged thyroid gland with heterogeneous echotexture.") # Image URL for Goiter

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
    st.image("https://static.elsevier.es/multimedia/07168640/0000002900000004/v4_201810230604/S071686401830083X/v4_201810230604/es/main.assets/gr2.jpeg?xkr=ue/ImdikoIMrsJoerZ+w997EogCnBdOOD93cPFbanNd2Vt2E9KIXSbfPNY5VCUB4kpCjPTZRm5n9r2Wgu2xKnaaLdMEH3EdygauzKlTyPTyhRP+tDkOLS79kLGbGk8d1oJdnmsF+0Z5YKEobFo2Z0StElaHQ/Zxzln4bsZr6SpIGyECJo3zN5e9MhSBTLGEIyh1iHSnNaDvwSThBeYb13Dl4mQuzAF0rIOYrRbqsEElCtLgsStdEbPvnKVXxcLi47ubDcRK6hoXBs8nEcD6h2JNM9FHOQK4L++jZQDRQQi3lrJdc8vWmXUrOzxvZ7LNG", caption="Graves Disease: Enlarged gland with heterogeneous echotexture.") # Image URL for Graves Disease

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
    st.image("https://static.elsevier.es/multimedia/07168640/0000002900000004/v4_201810230604/S071686401830083X/v4_201810230604/es/main.assets/gr3.jpeg?xkr=ue/ImdikoIMrsJoerZ+w997EogCnBdOOD93cPFbanNd2Vt2E9KIXSbfPNY5VCUB4kpCjPTZRm5n9r2Wgu2xKnaaLdMEH3EdygauzKlTyPTyhRP+tDkOLS79kLGbGk8d1oJdnmsF+0Z5YKEobFo2Z0StElaHQ/Zxzln4bsZr6SpIGyECJo3zN5e9MhSBTLGEIyh1iHSnNaDvwSThBeYb13Dl4mQuzAF0rIOYrRbqsEElCtLgsStdEbPvnKVXxcLi47ubDcRK6hoXBs8nEcD6h2JNM9FHOQK4L++jZQDRQQi3lrJdc8vWmXUrOzxvZ7LNG", caption="Hashimoto Thyroiditis: Mild enlargement of the thyroid gland with heterogeneous echotexture.") # Image URL for Hashimoto Thyroiditis

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
    st.image("https://static.elsevier.es/multimedia/07168640/0000002900000004/v4_201810230604/S071686401830083X/v4_201810230604/es/main.assets/gr4.jpeg?xkr=ue/ImdikoIMrsJoerZ+w997EogCnBdOOD93cPFbanNd2Vt2E9KIXSbfPNY5VCUB4kpCjPTZRm5n9r2Wgu2xKnaaLdMEH3EdygauzKlTyPTyhRP+tDkOLS79kLGbGk8d1oJdnmsF+0Z5YKEobFo2Z0StElaHQ/Zxzln4bsZr6SpIGyECJo3zN5e9MhSBTLGEIyh1iHSnNaDvwSThBeYb13Dl4mQuzAF0rIOYrRbqsEElCtLgsStdEbPvnKVXxcLi47ubDcRK6hoXBs8nEcD6h2JNM9FHOQK4L++jZQDRQQi3lrJdc8vWmXUrOzxvZ7LNG", caption="Benign Thyroid Nodules: Sonographic features include cystic components, hyperechoic mass, and wider-than-tall shape.") # Image URL for Benign Thyroid Nodules

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
    st.image("https://static.elsevier.es/multimedia/07168640/0000002900000004/v4_201810230604/S071686401830083X/v4_201810230604/es/main.assets/gr5.jpeg?xkr=ue/ImdikoIMrsJoerZ+w997EogCnBdOOD93cPFbanNd2Vt2E9KIXSbfPNY5VCUB4kpCjPTZRm5n9r2Wgu2xKnaaLdMEH3EdygauzKlTyPTyhRP+tDkOLS79kLGbGk8d1oJdnmsF+0Z5YKEobFo2Z0StElaHQ/Zxzln4bsZr6SpIGyECJo3zN5e9MhSBTLGEIyh1iHSnNaDvwSThBeYb13Dl4mQuzAF0rIOYrRbqsEElCtLgsStdEbPvnKVXxcLi47ubDcRK6hoXBs8nEcD6h2JNM9FHOQK4L++jZQDRQQi3lrJdc8vWmXUrOzxvZ7LNG", caption="Malignant Thyroid Nodules: Sonographic features include hypoechoic mass, taller-than-wide shape, and microcalcifications.") # Image URL for Malignant Thyroid Nodules


    # Generalidades
    st.markdown(style_title("Generalidades:") + " ", unsafe_allow_html=True)
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

    # Técnica Ecográfica
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

    # Indicaciones de la Ecografía Tiroidea
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

    # El Tiroides Normal y Patológico
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

    st.markdown("## Imágenes:")

    st.markdown("**Figura 1:** Normal thyroid: Thyroid lobe in longitudinal section, homogeneous parenchyma, normal echogenicity, normal shape and size.")
    st.image("https://static.elsevier.es/multimedia/07168640/0000002900000004/v4_201810230604/S071686401830083X/v4_201810230604/es/main.assets/gr1.jpeg?xkr=ue/ImdikoIMrsJoerZ+w997EogCnBdOOD93cPFbanNd2Vt2E9KIXSbfPNY5VCUB4kpCjPTZRm5n9r2Wgu2xKnaaLdMEH3EdygauzKlTyPTyhRP+tDkOLS79kLGbGk8d1oJdnmsF+0Z5YKEobFo2Z0StElaHQ/Zxzln4bsZr6SpIGyECJo3zN5e9MhSBTLGEIyh1iHSnNaDvwSThBeYb13Dl4mQuzAF0rIOYrRbqsEElCtLgsStdEbPvnKVXxcLi47ubDcRK6hoXBs8nEcD6h2JNM9FHOQK4L++jZQDRQQi3lrJdc8vWmXUrOzxvZ7LNG")

    st.markdown("**Figura 2:** Normal thyroid: Thyroid in a transverse section. The isthmus of normal thickness measures 2.3mm anteroposterior diameter.")
    st.image("https://static.elsevier.es/multimedia/07168640/0000002900000004/v4_201810230604/S071686401830083X/v4_201810230604/es/main.assets/gr2.jpeg?xkr=ue/ImdikoIMrsJoerZ+w997EogCnBdOOD93cPFbanNd2Vt2E9KIXSbfPNY5VCUB4kpCjPTZRm5n9r2Wgu2xKnaaLdMEH3EdygauzKlTyPTyhRP+tDkOLS79kLGbGk8d1oJdnmsF+0Z5YKEobFo2Z0StElaHQ/Zxzln4bsZr6SpIGyECJo3zN5e9MhSBTLGEIyh1iHSnNaDvwSThBeYb13Dl4mQuzAF0rIOYrRbqsEElCtLgsStdEbPvnKVXxcLi47ubDcRK6hoXBs8nEcD6h2JNM9FHOQK4L++jZQDRQQi3lrJdc8vWmXUrOzxvZ7LNG")

    st.markdown("**Figura 3:**  Normal thyroid: Left photo: transverse section: the pyramidal lobe in right paramedian location (arrowhead). Right photo: longitudinal section: the left pre-laryngeal pyramidal lobe imperceptibly continues with the isthmus (c: cranial; i: isthmus).")
    st.image("https://static.elsevier.es/multimedia/07168640/0000002900000004/v4_201810230604/S071686401830083X/v4_201810230604/es/main.assets/gr3.jpeg?xkr=ue/ImdikoIMrsJoerZ+w997EogCnBdOOD93cPFbanNd2Vt2E9KIXSbfPNY5VCUB4kpCjPTZRm5n9r2Wgu2xKnaaLdMEH3EdygauzKlTyPTyhRP+tDkOLS79kLGbGk8d1oJdnmsF+0Z5YKEobFo2Z0StElaHQ/Zxzln4bsZr6SpIGyECJo3zN5e9MhSBTLGEIyh1iHSnNaDvwSThBeYb13Dl4mQuzAF0rIOYrRbqsEElCtLgsStdEbPvnKVXxcLi47ubDcRK6hoXBs8nEcD6h2JNM9FHOQK4L++jZQDRQQi3lrJdc8vWmXUrOzxvZ7LNG")

    st.markdown("**Figura 4:**  Hemiagenesis of the left thyroid lobe: Patient without surgical history. There is no paratracheal left glandular parenchyma. In this case, the isthmus is present.")
    st.image("https://static.elsevier.es/multimedia/07168640/0000002900000004/v4_201810230604/S071686401830083X/v4_201810230604/es/main.assets/gr4.jpeg?xkr=ue/ImdikoIMrsJoerZ+w997EogCnBdOOD93cPFbanNd2Vt2E9KIXSbfPNY5VCUB4kpCjPTZRm5n9r2Wgu2xKnaaLdMEH3EdygauzKlTyPTyhRP+tDkOLS79kLGbGk8d1oJdnmsF+0Z5YKEobFo2Z0StElaHQ/Zxzln4bsZr6SpIGyECJo3zN5e9MhSBTLGEIyh1iHSnNaDvwSThBeYb13Dl4mQuzAF0rIOYrRbqsEElCtLgsStdEbPvnKVXxcLi47ubDcRK6hoXBs8nEcD6h2JNM9FHOQK4L++jZQDRQQi3lrJdc8vWmXUrOzxvZ7LNG")

    st.markdown("**Figura 5:**  Goiter. A: Thyroid in a longitudinal section, globose increased in size, gently lobulated contours, hypoechoic parenchyma, heterogeneous, without images of nodules in its thickness. ")
    st.image("https://static.elsevier.es/multimedia/07168640/0000002900000004/v4_201810230604/S071686401830083X/v4_201810230604/es/main.assets/gr5.jpeg?xkr=ue/ImdikoIMrsJoerZ+w997EogCnBdOOD93cPFbanNd2Vt2E9KIXSbfPNY5VCUB4kpCjPTZRm5n9r2Wgu2xKnaaLdMEH3EdygauzKlTyPTyhRP+tDkOLS79kLGbGk8d1oJdnmsF+0Z5YKEobFo2Z0StElaHQ/Zxzln4bsZr6SpIGyECJo3zN5e9MhSBTLGEIyh1iHSnNaDvwSThBeYb13Dl4mQuzAF0rIOYrRbqsEElCtLgsStdEbPvnKVXxcLi47ubDcRK6hoXBs8nEcD6h2JNM9FHOQK4L++jZQDRQQi3lrJdc8vWmXUrOzxvZ7LNG")

    st.markdown("**Figura 5:**  B: Thyroid in a longitudinal section, globose increased in size, lobulated contours, hypoechoic, heterogeneous, with solid nodules of different sizes.")
    st.image("https://static.elsevier.es/multimedia/07168640/0000002900000004/v4_201810230604/S071686401830083X/v4_201810230604/es/main.assets/gr6.jpeg?xkr=ue/ImdikoIMrsJoerZ+w997EogCnBdOOD93cPFbanNd2Vt2E9KIXSbfPNY5VCUB4kpCjPTZRm5n9r2Wgu2xKnaaLdMEH3EdygauzKlTyPTyhRP+tDkOLS79kLGbGk8d1oJdnmsF+0Z5YKEobFo2Z0StElaHQ/Zxzln4bsZr6SpIGyECJo3zN5e9MhSBTLGEIyh1iHSnNaDvwSThBeYb13Dl4mQuzAF0rIOYrRbqsEElCtLgsStdEbPvnKVXxcLi47ubDcRK6hoXBs8nEcD6h2JNM9FHOQK4L++jZQDRQQi3lrJdc8vWmXUrOzxvZ7LNG")

    st.markdown("**Figura 6:** Thyroid nodules. A: On the left, a solid thyroid nodule, isoechoic (same echogenicity as the rest of the lobe) and on the right, the image of a hypoechoic nodule (darker than the rest of the surrounding normal thyroid tissue), in this case with some thick calcifications (white images of eccentric location, upper right). ")
    st.image("https://static.elsevier.es/multimedia/07168640/0000002900000004/v4_201810230604/S071686401830083X/v4_201810230604/es/main.assets/gr7.jpeg?xkr=ue/ImdikoIMrsJoerZ+w997EogCnBdOOD93cPFbanNd2Vt2E9KIXSbfPNY5VCUB4kpCjPTZRm5n9r2Wgu2xKnaaLdMEH3EdygauzKlTyPTyhRP+tDkOLS79kLGbGk8d1oJdnmsF+0Z5YKEobFo2Z0StElaHQ/Zxzln4bsZr6SpIGyECJo3zN5e9MhSBTLGEIyh1iHSnNaDvwSThBeYb13Dl4mQuzAF0rIOYrRbqsEElCtLgsStdEbPvnKVXxcLi47ubDcRK6hoXBs8nEcD6h2JNM9FHOQK4L++jZQDRQQi3lrJdc8vWmXUrOzxvZ7LNG")

    st.markdown("**Figura 6:**  B: Longitudinal ultrasound section of a thyroid nodule: solid, hyperechoic, well-defined, without calcifications.")
    st.image("https://static.elsevier.es/multimedia/07168640/0000002900000004/v4_201810230604/S071686401830083X/v4_201810230604/es/main.assets/gr8.jpeg?xkr=ue/ImdikoIMrsJoerZ+w997EogCnBdOOD93cPFbanNd2Vt2E9KIXSbfPNY5VCUB4kpCjPTZRm5n9r2Wgu2xKnaaLdMEH3EdygauzKlTyPTyhRP+tDkOLS79kLGbGk8d1oJdnmsF+0Z5YKEobFo2Z0StElaHQ/Zxzln4bsZr6SpIGyECJo3zN5e9MhSBTLGEIyh1iHSnNaDvwSThBeYb13Dl4mQuzAF0rIOYrRbqsEElCtLgsStdEbPvnKVXxcLi47ubDcRK6hoXBs8nEcD6h2JNM9FHOQK4L++jZQDRQQi3lrJdc8vWmXUrOzxvZ7LNG")

    st.markdown("**Figura 6:**  C: Cystic thyroid nodule (anechoic): ultrasound passes through the liquid structure without generating echoes and immediately dorsal to the cyst there is an ultrasound reinforcement, due to greater availability of energy to emit more echoes.")
    st.image("https://static.elsevier.es/multimedia/07168640/0000002900000004/v4_201810230604/S071686401830083X/v4_201810230604/es/main.assets/gr9.jpeg?xkr=ue/ImdikoIMrsJoerZ+w997EogCnBdOOD93cPFbanNd2Vt2E9KIXSbfPNY5VCUB4kpCjPTZRm5n9r2Wgu2xKnaaLdMEH3EdygauzKlTyPTyhRP+tDkOLS79kLGbGk8d1oJdnmsF+0Z5YKEobFo2Z0StElaHQ/Zxzln4bsZr6SpIGyECJo3zN5e9MhSBTLGEIyh1iHSnNaDvwSThBeYb13Dl4mQuzAF0rIOYrRbqsEElCtLgsStdEbPvnKVXxcLi47ubDcRK6hoXBs8nEcD6h2JNM9FHOQK4L++jZQDRQQi3lrJdc8vWmXUrOzxvZ7LNG")

    st.markdown("**Figura 6:**  D: Solid cystic thyroid nodule (or mixed), surrounded by a hypoechoic halo. The peripheral portion of the nodule is solid, isoechoic and the center is liquid (anechoic).")
    st.image("https://static.elsevier.es/multimedia/07168640/0000002900000004/v4_201810230604/S071686401830083X/v4_201810230604/es/main.assets/gr10.jpeg?xkr=ue/ImdikoIMrsJoerZ+w997EogCnBdOOD93cPFbanNd2Vt2E9KIXSbfPNY5VCUB4kpCjPTZRm5n9r2Wgu2xKnaaLdMEH3EdygauzKlTyPTyhRP+tDkOLS79kLGbGk8d1oJdnmsF+0Z5YKEobFo2Z0StElaHQ/Zxzln4bsZr6SpIGyECJo3zN5e9MhSBTLGEIyh1iHSnNaDvwSThBeYb13Dl4mQuzAF0rIOYrRbqsEElCtLgsStdEbPvnKVXxcLi47ubDcRK6hoXBs8nEcD6h2JNM9FHOQK4L++jZQDRQQi3lrJdc8vWmXUrOzxvZ7LNG")

    st.markdown("**Figura 7:**  Thyroid nodules with sonographic characteristics of malignancy. A: Solid thyroid nodule, markedly hypoechoic, also presents peripheral microcalcifications (papillary Ca). ")
    st.image("https://static.elsevier.es/multimedia/07168640/0000002900000004/v4_201810230604/S071686401830083X/v4_201810230604/es/main.assets/gr11.jpeg?xkr=ue/ImdikoIMrsJoerZ+w997EogCnBdOOD93cPFbanNd2Vt2E9KIXSbfPNY5VCUB4kpCjPTZRm5n9r2Wgu2xKnaaLdMEH3EdygauzKlTyPTyhRP+tDkOLS79kLGbGk8d1oJdnmsF+0Z5YKEobFo2Z0StElaHQ/Zxzln4bsZr6SpIGyECJo3zN5e9MhSBTLGEIyh1iHSnNaDvwSThBeYb13Dl4mQuzAF0rIOYrRbqsEElCtLgsStdEbPvnKVXxcLi47ubDcRK6hoXBs8nEcD6h2JNM9FHOQK4L++jZQDRQQi3lrJdc8vWmXUrOzxvZ7LNG")

    st.markdown("**Figura 7:**  B: Solid thyroid nodule higher than wide: anteroposterior diameter (height) greater than longitudinal diameter (width). (papillary Ca).")
    st.image("https://static.elsevier.es/multimedia/07168640/0000002900000004/v4_201810230604/S071686401830083X/v4_201810230604/es/main.assets/gr12.jpeg?xkr=ue/ImdikoIMrsJoerZ+w997EogCnBdOOD93cPFbanNd2Vt2E9KIXSbfPNY5VCUB4kpCjPTZRm5n9r2Wgu2xKnaaLdMEH3EdygauzKlTyPTyhRP+tDkOLS79kLGbGk8d1oJdnmsF+0Z5YKEobFo2Z0StElaHQ/Zxzln4bsZr6SpIGyECJo3zN5e9MhSBTLGEIyh1iHSnNaDvwSThBeYb13Dl4mQuzAF0rIOYrRbqsE
