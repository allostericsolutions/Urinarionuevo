import streamlit as st

# Initialize the variable in session_state
if 'mostrar_eponimos' not in st.session_state:
    st.session_state.mostrar_eponimos = False

# Button to show/hide the eponyms section
if st.button("Eponyms"):
    st.session_state.mostrar_eponimos = not st.session_state.mostrar_eponimos

# Expandable and collapsible section
with st.expander("Eponyms related to Medical Conditions:", expanded=st.session_state.mostrar_eponimos):
    st.write("Kaposi sarcoma: A cancer characterized by lesions on the skin and other areas; often linked to AIDS. Named after Moritz Kaposi.")
    st.write("Morison Pouch: The space between the liver and the right kidney; also known as the posterior right subhepatic space. Named after James R. Morison.")
    st.write("Space of Retzius: The area between the urinary bladder and the pubic bone; also referred to as the retropubic space. Named after Anders Retzius.")
    st.write("Wilson disease: A genetic disorder leading to excess copper accumulation in the body. Named after Samuel Alexander Kinnier Wilson.")