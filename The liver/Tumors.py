import streamlit as st

# Inicializar la variable en session_state
if 'mostrar_tumores_benignos' not in st.session_state:
    st.session_state.mostrar_tumores_benignos = False

if 'mostrar_tumores_malignos' not in st.session_state:
    st.session_state.mostrar_tumores_malignos = False

# Botón para alternar la visibilidad del expander de tumores benignos
if st.button("Benign Liver Tumors"):
    st.session_state.mostrar_tumores_benignos = not st.session_state.mostrar_tumores_benignos

# Botón para alternar la visibilidad del expander de tumores malignos
if st.button("Malignant Liver Tumors"):
    st.session_state.mostrar_tumores_malignos = not st.session_state.mostrar_tumores_malignos

# Función para estilizar los títulos principales
def style_title(title):
    return f"<span style='color:darkorange; font-weight:bold;'>{title}</span>"

# Función para estilizar los subtítulos
def style_subtitle(subtitle):
    return f"<span style='color:yellow; font-weight:bold;'>{subtitle}</span>"

# Sección que se expande y se contrae para los tumores benignos del hígado
with st.expander("Benign Liver Tumors - Flash Card Style:", expanded=st.session_state.mostrar_tumores_benignos):

    # Cavernous Hemangioma
    st.markdown(style_title("Cavernous Hemangioma"), unsafe_allow_html=True)
    st.markdown(style_subtitle("Symptoms"), unsafe_allow_html=True)
    st.write(" - Usually asymptomatic.")
    st.write(" - Symptoms may include abdominal pain, distension, or palpable mass (in cases of large hemangiomas).")
    st.markdown(style_subtitle("Risk Factors"), unsafe_allow_html=True)
    st.write(" - None specific.")
    st.markdown(style_subtitle("Key USG Findings"), unsafe_allow_html=True)
    st.write(" - Small, hyperechoic mass, less than 3 cm.")
    st.write(" - Often located in the right lobe of the liver.")
    st.write(" - May show posterior enhancement.")
    st.write(" - Slow flow, color Doppler may not detect it.")
    st.write(" - Possibility of multiple hemangiomas.")
    st.markdown(style_subtitle("Differential Diagnosis"), unsafe_allow_html=True)
    st.write(" - Liver metastasis.")
    st.write(" - Cyst.")
    st.write(" - Hepatocellular carcinoma (rarely).")
    
    # Focal Nodular Hyperplasia (FNH)
    st.markdown(style_title("Focal Nodular Hyperplasia (FNH)"), unsafe_allow_html=True)
    st.markdown(style_subtitle("Symptoms"), unsafe_allow_html=True)
    st.write(" - Usually asymptomatic.")
    st.write(" - Symptoms may include abdominal pain if the mass presses on adjacent organs or there is bleeding.")
    st.markdown(style_subtitle("Risk Factors"), unsafe_allow_html=True)
    st.write(" - Exposure to estrogens (such as oral contraceptive use).")
    st.markdown(style_subtitle("Key USG Findings"), unsafe_allow_html=True)
    st.write(" - Can have isoechoic, hyperechoic, or hypoechoic appearance.")
    st.write(" - Often contains a central stellate scar (high diagnostic value), which can be hypoechoic or hyperechoic and linear.")
    st.write(" - Hypervascularization in the scar detectable with color Doppler.")
    st.write(" - May be difficult to identify (stealth lesion).")
    st.markdown(style_subtitle("Differential Diagnosis"), unsafe_allow_html=True)
    st.write(" - Normal liver.")
    st.write(" - Small cavernous hemangioma.")
    st.write(" - Hepatocellular adenoma.")

    # Hepatocellular Adenoma
    st.markdown(style_title("Hepatocellular Adenoma"), unsafe_allow_html=True)
    st.markdown(style_subtitle("Symptoms"), unsafe_allow_html=True)
    st.write(" - Usually asymptomatic.")
    st.write(" - Symptoms may include abdominal pain in case of bleeding.")
    st.markdown(style_subtitle("Risk Factors"), unsafe_allow_html=True)
    st.write(" - Oral contraceptive use. Estrogen exposure.")
    st.markdown(style_subtitle("Key USG Findings"), unsafe_allow_html=True)
    st.write(" - Usually appears as a hypoechoic mass.")
    st.write(" - May be hyperechoic, isoechoic or have mixed echogenicity.")
    st.write(" - Possibility of multiple adenomas.")
    st.markdown(style_subtitle("Differential Diagnosis"), unsafe_allow_html=True)
    st.write(" - FNH.")
    st.write(" - Hepatocellular carcinoma.")

    # Hepatic Lipoma
    st.markdown(style_title("Hepatic Lipoma"), unsafe_allow_html=True)
    st.markdown(style_subtitle("Symptoms"), unsafe_allow_html=True)
    st.write(" - Usually asymptomatic.")
    st.markdown(style_subtitle("Risk Factors"), unsafe_allow_html=True)
    st.write(" - None specific.")
    st.markdown(style_subtitle("Key USG Findings"), unsafe_allow_html=True)
    st.write(" - Appears as a hyperechoic mass.")
    st.markdown(style_subtitle("Differential Diagnosis"), unsafe_allow_html=True)
    st.write(" - Small cavernous hemangioma.")
    st.write(" - Liver metastasis.")

    # Hepatic Hematoma
    st.markdown(style_title("Hepatic Hematoma"), unsafe_allow_html=True)
    st.markdown(style_subtitle("Symptoms"), unsafe_allow_html=True)
    st.write(" - Symptoms may include abdominal pain.")
    st.markdown(style_subtitle("Risk Factors"), unsafe_allow_html=True)
    st.write(" - Abdominal trauma. Liver surgery.")
    st.markdown(style_subtitle("Key USG Findings"), unsafe_allow_html=True)
    st.write(" - Can be intrahepatic or subcapsular.")
    st.write(" - The USG appearance varies according to the age of the hematoma; it can be solid or complex.")
    st.write(" - An acute hematoma may be isoechoic to liver tissue, making it difficult to visualize.")
    st.write(" - A subcapsular hematoma can be mistaken for ascites.")
    st.write(" - Calcification is possible.")
    st.markdown(style_subtitle("Differential Diagnosis"), unsafe_allow_html=True)
    st.write(" - Liver abscess.")
    st.write(" - Liver neoplasm.")

# Sección que se expande y se contrae para los tumores malignos del hígado
with st.expander("Malignant Liver Tumors - Flash Card Style:", expanded=st.session_state.mostrar_tumores_malignos):

    # Hepatocellular Carcinoma (HCC)
    st.markdown(style_title("Hepatocellular Carcinoma (HCC)"), unsafe_allow_html=True)
    st.write(" - Most common primary form of liver cancer.")
    st.write(" - HCC is not encountered as often as metastatic liver disease.")
    st.write(" - Most often seen in men and frequently accompanied by cirrhosis or chronic hepatitis.")
    st.write(" - Other causes include hemochromatosis, von Gierke disease, and Wilson disease.")
    st.write(" - The malignant mass associated with HCC is referred to as a hepatoma.")
    st.write(" - Hepatomas can invade the portal veins or hepatic veins.")
    st.write(" - Occlusion of the hepatic veins, with possible tumor invasion into the IVC, is termed Budd–Chiari syndrome, and thus the sonographic evaluation of pertinent vasculature is warranted for evidence of tumor thrombus.")
    st.write(" - Color Doppler may yield evidence of hypervascularity within the mass, although this is not a specific indicator for malignancy.")
    st.markdown(style_subtitle("Clinical Findings"), unsafe_allow_html=True)
    st.write(" - Possible abnormal liver function tests.")
    st.write(" - Signs of cirrhosis.")
    st.write(" - History of chronic hepatitis.")
    st.write(" - Unexplained weight loss.")
    st.write(" - Hepatomegaly.")
    st.write(" - Fever.")
    st.write(" - Abdominal swelling with ascites.")
    st.write(" - Perhaps a palpable mass.")
    st.write(" - Elevated serum alpha-fetoprotein (AFP).")
    st.markdown(style_subtitle("Key USG Findings"), unsafe_allow_html=True)
    st.write(" - Solitary, small, hypoechoic mass, or as heterogeneous masses scattered throughout the liver.")
    st.write(" - A hypoechoic halo may be noted around the hepatoma as well, yielding the target or bull’s-eye pattern.")
    st.write(" - The target lesion will yield a hypoechoic rim, with the center of the mass often isoechoic to normal liver tissue.")
    st.write(" - Possible ascites.")
    st.markdown(style_subtitle("Differential Diagnosis"), unsafe_allow_html=True)
    st.write(" - Metastasis.")
    st.write(" - Benign liver tumors (e.g., hemangioma, FNH, adenoma)")

    # Hepatic Metastasis
    st.markdown(style_title("Hepatic Metastasis"), unsafe_allow_html=True)
    st.write(" - The liver is a common location for metastatic disease to manifest in the abdomen.")
    st.write(" - Metastatic liver disease is the most common form of liver cancer.")
    st.write(" - The malignant cells from other sites enter the liver through the portal veins or lymphatic channels.")
    st.write(" - Primary cancers that metastasize to the liver include the gallbladder, colon, stomach, pancreas, breast, and lung, with the latter being the most common primary source.")
    st.write(" - Patients with hepatic metastasis may present with weight loss, jaundice, right upper quadrant pain, hepatomegaly, and ascites.")
    st.write(" - However, in about half of patients, there are no clinical signs or symptoms, including the possibility of normal liver function tests initially.")
    st.markdown(style_subtitle("Clinical Findings"), unsafe_allow_html=True)
    st.write(" - Abnormal liver function test (possibly)")
    st.write(" - Weight loss")
    st.write(" - Jaundice")
    st.write(" - Right upper quadrant pain")
    st.write(" - Hepatomegaly")
    st.write(" - Abdominal swelling with ascites")
    st.markdown(style_subtitle("Key USG Findings"), unsafe_allow_html=True)
    st.write(" - Hyperechoic, hypoechoic, calcified, cystic, or heterogeneous masses")
    st.write(" - Mass or masses demonstrating a hypoechoic rim and central echogenic region")
    st.write(" - Diffusely heterogeneous liver")
    st.write(" - Possible ascites")
    st.markdown(style_subtitle("Differential Diagnosis"), unsafe_allow_html=True)
    st.write(" - HCC")
    st.write(" - Benign liver tumors (e.g., hemangioma, FNH, adenoma)")
