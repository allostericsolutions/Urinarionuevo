import streamlit as st

# Initialize the variable in session_state
if 'mostrar_eponimos' not in st.session_state:
    st.session_state.mostrar_eponimos = False

# Button to show/hide the eponyms section
if st.button("Eponyms"):
    st.session_state.mostrar_eponimos = not st.session_state.mostrar_eponimos

# Function to style the eponym titles
def style_title(title):
    return f"<span style='color:darkorange; font-weight:bold;'>{title}</span>"

# Expandable and collapsible section
with st.expander("Eponyms related to Liver Conditions:", expanded=st.session_state.mostrar_eponimos):
    st.markdown(style_title("Budd–Chiari syndrome:") + " A syndrome described as the occlusion of the hepatic veins, with possible coexisting occlusion of the inferior vena cava. Named after William Budd and  Jules-Auguste Chiari.", unsafe_allow_html=True)
    st.markdown(style_title("Beckwith–Wiedemann syndrome:") + " A growth disorder syndrome synonymous with enlargement of several organs, including the skull, tongue, and liver.  Children with this disorder are prone to several childhood cancers, including within the liver and kidney. Named after  Henry Beckwith and  Herbert Wiedemann.", unsafe_allow_html=True)
    st.markdown(style_title("Cruveilhier–Baumgarten syndrome:") + " Syndrome characterized by cirrhosis, portal hypertension, and dilation of the umbilical and paraumbilical veins. Named after Jean Cruveilhier and  Paul Baumgarten.", unsafe_allow_html=True)
    st.markdown(style_title("Epstein–Barr virus:") + " The virus responsible for mononucleosis and other potential complications. Named after  Albert  Epstein  and  Yvonne Barr.", unsafe_allow_html=True)
