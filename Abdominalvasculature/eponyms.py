import streamlit as st

# Initialize the variable in session_state
if 'mostrar_eponimos' not in st.session_state:
    st.session_state.mostrar_eponimos = False

# Function to style the eponym titles
def style_title(title):
    return f"<span style='color:darkorange; font-weight:bold;'>{title}</span>"

# Expandable and collapsible section
with st.expander("Eponyms in Abdominal Sonography:", expanded=st.session_state.mostrar_eponimos):
    st.markdown(style_title("Budd–Chiari Syndrome:") + " Occlusion of the hepatic veins, possibly including occlusion of the inferior vena cava (IVC). Named after William Budd and Hans Chiari.", unsafe_allow_html=True)
    st.markdown(style_title("Marfan Syndrome:") + " Connective tissue disorder characterized by tall stature, and aortic and mitral valve insufficiency. Named after Antoine Marfan.", unsafe_allow_html=True)
    st.markdown(style_title("Wilms Tumor (Nephroblastoma):") + " The most common solid malignant pediatric abdominal mass; a malignant pediatric renal mass. Named after Max Wilms.", unsafe_allow_html=True)
