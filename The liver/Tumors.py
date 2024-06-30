import streamlit as st

# Variable para controlar la visibilidad de la sección de tumores benignos
mostrar_tumores_benignos = False

# Función para estilizar los títulos
def style_title(title):
    return f"<span style='color:darkorange; font-weight:bold;'>{title}</span>"

def style_subtitle(subtitle):
    return f"<span style='color:yellow; font-weight:bold;'>{subtitle}</span>"

# Sección que se expande y se contrae para los tumores benignos del hígado
with st.expander("Benign Liver Tumors - Flash Card Style:", expanded=mostrar_tumores_benignos):

    # Hemangioma Cavernoso
    st.markdown(style_title("Cavernous Hemangioma"), unsafe_allow_html=True)
    st.write(" - Most common benign liver tumor, more frequent in women.")
    st.write(" - Usually asymptomatic.")
    st.write(" - Symptoms may include abdominal pain, distension, or palpable mass (in cases of large hemangiomas).")
    st.write(" - Risk factors: None specific.")
    st.write(" - **Key USG Findings:**")
    st.write("    - Small, hyperechoic mass, less than 3 cm.")
    st.write("    - Often located in the right lobe of the liver.")
    st.write("    - May show posterior enhancement.")
    st.write("    - Slow flow, color Doppler may not detect it.")
    st.write("    - Possibility of multiple hemangiomas.")
    st.write(" - **Differential Diagnosis:**")
    st.write("    - Liver metastasis.")
    st.write("    - Cyst.")
    st.write("    - Hepatocellular carcinoma (rarely).")
    
    # Hiperplasia Nodular Focal (FNH)
    st.markdown(style_title("Focal Nodular Hyperplasia (FNH)"), unsafe_allow_html=True)
    st.write(" - Second most common benign liver tumor, more frequent in women.")
    st.write(" - Usually asymptomatic.")
    st.write(" - Symptoms may include abdominal pain if the mass presses on adjacent organs or there is bleeding.")
    st.write(" - Risk factors: Exposure to estrogens (such as oral contraceptive use).")
    st.write(" - **Key USG Findings:**")
    st.write("    - Can have isoechoic, hyperechoic, or hypoechoic appearance.")
    st.write("    - Often contains a central stellate scar (high diagnostic value), which can be hypoechoic or hyperechoic and linear.")
    st.write("    - Hypervascularization in the scar detectable with color Doppler.")
    st.write("    - May be difficult to identify (stealth lesion).")
    st.write(" - **Differential Diagnosis:**")
    st.write("    - Normal liver.")
    st.write("    - Small cavernous hemangioma.")
    st.write("    - Hepatocellular adenoma.")

    # Hepatocellular Adenoma
    st.markdown(style_title("Hepatocellular Adenoma"), unsafe_allow_html=True)
    st.write(" - Rare benign liver tumor, associated with oral contraceptive use.")
    st.write(" - Usually asymptomatic.")
    st.write(" - Symptoms may include abdominal pain in case of bleeding.")
    st.write(" - Risk factors: Oral contraceptive use. Estrogen exposure.")
    st.write(" - **Key USG Findings:**")
    st.write("    - Usually appears as a hypoechoic mass.")
    st.write("    - May be hyperechoic, isoechoic or have mixed echogenicity.")
    st.write("    - Possibility of multiple adenomas.")
    st.write(" - **Differential Diagnosis:**")
    st.write("    - FNH.")
    st.write("    - Hepatocellular carcinoma.")

    # Hepatic Lipoma
    st.markdown(style_title("Hepatic Lipoma"), unsafe_allow_html=True)
    st.write(" - Very rare benign tumor.")
    st.write(" - Usually asymptomatic.")
    st.write(" - Risk factors: None specific.")
    st.write(" - **Key USG Findings:**")
    st.write("    - Appears as a hyperechoic mass.")
    st.write(" - **Differential Diagnosis:**")
    st.write("    - Small cavernous hemangioma.")
    st.write("    - Liver metastasis.")

    # Hepatic Hematoma
    st.markdown(style_title("Hepatic Hematoma"), unsafe_allow_html=True)
    st.write(" - Result of trauma or surgery.")
    st.write(" - Symptoms may include abdominal pain.")
    st.write(" - Risk factors: Abdominal trauma. Liver surgery.")
    st.write(" - **Key USG Findings:**")
    st.write("    - Can be intrahepatic or subcapsular.")
    st.write("    - The USG appearance varies according to the age of the hematoma; it can be solid or complex.")
    st.write("    - An acute hematoma may be isoechoic to liver tissue, making it difficult to visualize.")
    st.write("    - A subcapsular hematoma can be mistaken for ascites.")
    st.write("    - Calcification is possible.")
    st.write(" - **Differential Diagnosis:**")
    st.write("    - Liver abscess.")
    st.write("    - Liver neoplasm.")
