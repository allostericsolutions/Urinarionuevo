import streamlit as st

# Initialize the variable in session_state
if 'mostrar_eponimos' not in st.session_state:
    st.session_state.mostrar_eponimos = False

# Function to style the eponym titles
def style_title(title):
    return f"<span style='color:darkorange; font-weight:bold;'>{title}</span>"

# Gallbladder Signs
gallbladder_signs = [
    ("Ball-on-the-wall sign", "Appearance of a gallbladder polyp."),
    ("Cinnamon bun sign", "Short axis appearance of intussusception."),
    ("Whirlpool sign", "Cystic duct appearance with color Doppler associated with gallbladder torsion."),
    ("Wall-echo-shadow (WES) sign", "Appearance of a gallbladder completely filled with stones."),
    ("Olive sign", "Palpable hypertrophic pyloric muscle associated with pyloric stenosis"),
    ("Murphy sign", "Pain with probe pressure over the gallbladder."),
    ("Pseudogallbladder sign", "Cystic structure noted in the gallbladder fossa without evidence of an actual gallbladder; associated with biliary atresia in children.")
]

# Expandable and collapsible section for Gallbladder Signs
with st.expander("Gallbladder Ultrasound Signs:", expanded=st.session_state.mostrar_eponimos):
    for sign, description in gallbladder_signs:
        st.markdown(style_title(sign) + f": {description}", unsafe_allow_html=True)
