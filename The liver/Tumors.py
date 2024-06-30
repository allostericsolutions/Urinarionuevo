import streamlit as st

# Variable para controlar la visibilidad de la sección de tumores benignos
mostrar_tumores_benignos = st.session_state.get('mostrar_tumores_benignos', False)

# Botón para alternar la visibilidad del expander
if st.button("Benign Liver Tumors"):
    st.session_state.mostrar_tumores_benignos = not mostrar_tumores_benignos

# Función para estilizar los títulos principales
def style_title(title):
    return f"<span style='color:darkorange; font-weight:bold;'>{title}</span>"

# Función para estilizar los subtítulos
def style_subtitle(subtitle):
    return f"<span style='color:yellow; font-weight:bold;'>{subtitle}</span>"

# Sección que se expande y se contrae para los tumores benignos del hígado
with st.expander("Benign Liver Tumors - Flash Card Style:", expanded=st.session_state.mostrar_tumores_benignos):

    # Hemangioma Cavernoso
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
    
    # Hiperplasia Nodular Focal (FNH)
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
