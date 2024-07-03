import streamlit as st

# Initialize the variable in session_state
if 'mostrar_eponimos' not in st.session_state:
    st.session_state.mostrar_eponimos = False

# Function to style the eponym titles
def style_title(title):
    return f"<span style='color:darkorange; font-weight:bold;'>{title}</span>"

# Expandable and collapsible section
with st.expander("Eponyms related to Medical Conditions:", expanded=st.session_state.mostrar_eponimos):
    st.markdown(style_title("Kaposi sarcoma:") + " A cancer characterized by lesions on the skin and other areas; often linked to AIDS. Named after Moritz Kaposi.", unsafe_allow_html=True)
    st.markdown(style_title("Morison Pouch:") + " The space between the liver and the right kidney; also known as the posterior right subhepatic space. Named after James R. Morison.", unsafe_allow_html=True)
    st.markdown(style_title("Space of Retzius:") + " The area between the urinary bladder and the pubic bone; also referred to as the retropubic space. Named after Anders Retzius.", unsafe_allow_html=True)
    st.markdown(style_title("Wilson disease:") + " A genetic disorder leading to excess copper accumulation in the body. Named after Samuel Alexander Kinnier Wilson.", unsafe_allow_html=True)
