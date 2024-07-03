import streamlit as st

# Initialize the variable in session_state
if 'mostrar_eponimos' not in st.session_state:
    st.session_state.mostrar_eponimos = False

# Function to style the eponym titles
def style_title(title):
    return f"<span style='color:darkorange; font-weight:bold;'>{title}</span>"

# Expandable and collapsible section
with st.expander("Eponyms in Pancreatic Terminology:", expanded=st.session_state.mostrar_eponimos):
    st.markdown(style_title("Acinar cells:") + " This term describes cells that have a grape-like shape and are involved in the exocrine function of the pancreas, producing digestive enzymes. \"Acinar\" derives from the Latin \"acinus\", meaning \"berry\" or \"grape.\"", unsafe_allow_html=True)
    st.markdown(style_title("Duct of Santorini:") + " Named after  **Giovanni Santorini**, an Italian anatomist, this is the accessory pancreatic duct.", unsafe_allow_html=True)
    st.markdown(style_title("Duct of Wirsung:") + " Named after **Johann Georg Wirsung**, a German anatomist, this is the main pancreatic duct.", unsafe_allow_html=True)
    st.markdown(style_title("Sign of the Double Duct:") + " This refers to the simultaneous enlargement of the common bile duct and the pancreatic duct, seen in imaging studies.", unsafe_allow_html=True)
    st.markdown(style_title("Von Hippel–Lindau disease:") + "  Named after **E. von Hippel** and **A. Lindau**, German ophthalmologists and pathologists, this is a hereditary disease featuring pancreatic cysts and other organ abnormalities.", unsafe_allow_html=True)
    st.markdown(style_title("Whipple procedure:") + "  Named after **Allen Whipple**, an American surgeon, this procedure involves removing the head of the pancreas, the gallbladder, some bile ducts, and the proximal duodenum, often due to pancreatic cancer.", unsafe_allow_html=True)
    st.markdown(style_title("Whipple triad:") + "  Named after **Allen Whipple**, this triad of clinical indicators suggests a functional insulinoma: hypoglycemia, low fasting glucose, and relief with intravenous glucose administration.", unsafe_allow_html=True)
    st.markdown(style_title("Zollinger–Ellison syndrome:") + "  Named after **Robert Zollinger** and **Edwin Ellison**, American surgeons, this syndrome involves excessive stomach acid secretion caused by a functional gastrinoma in the pancreas.", unsafe_allow_html=True)

