import streamlit as st

# Initialize the variable in session_state
if 'mostrar_eponimos' not in st.session_state:
    st.session_state.mostrar_eponimos = False

# Function to style the eponym titles
def style_title(title):
    return f"<span style='color:darkorange; font-weight:bold;'>{title}</span>"

# Expandable and collapsible section
with st.expander("Signs related to Gallbladder:", expanded=st.session_state.mostrar_eponimos):
    st.markdown(style_title("Ball-on-the-wall sign:") + " Appearance of a gallbladder polyp.", unsafe_allow_html=True)
    st.markdown(style_title("Cinnamon bun sign:") + " Short axis appearance of intussusception ", unsafe_allow_html=True)
    st.markdown(style_title("Whirlpool sign:") + " Cystic duct appearance with color Doppler associated with gallbladder torsion.", unsafe_allow_html=True)
    st.markdown(style_title("Wall-echo-shadow (WES) sign:") + " Appearance of a gallbladder completely filled with stones.", unsafe_allow_html=True)
    st.markdown(style_title("Olive sign:") + " Palpable hypertrophic pyloric muscle associated with pyloric stenosis", unsafe_allow_html=True)
    st.markdown(style_title("Murphy sign:") + " Pain with probe pressure over the gallbladder.", unsafe_allow_html=True)
    st.markdown(style_title("Pseudogallbladder sign:") + " Cystic structure noted in the gallbladder fossa without evidence of an actual gallbladder; associated with biliary atresia in children.", unsafe_allow_html=True)
I've simply removed the original eponyms and replaced them with the new ones.
