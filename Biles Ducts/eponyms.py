import streamlit as st

# Initialize the variable in session_state
if 'mostrar_eponimos' not in st.session_state:
    st.session_state.mostrar_eponimos = False

# Function to style the eponym titles
def style_title(title):
    return f"<span style='color:darkorange; font-weight:bold;'>{title}</span>"

# Expandable and collapsible section
with st.expander("Eponyms in Abdominal Sonography:", expanded=st.session_state.mostrar_eponimos):
    st.markdown(style_title("Ampulla of Vater:") + " The point where the pancreatic duct and the common bile duct merge just before the sphincter of Oddi; also called the hepatopancreatic ampulla.", unsafe_allow_html=True)
    st.markdown(style_title("Caroli Disease:") + " A congenital disorder characterized by segmental dilatation of the intrahepatic bile ducts. Associated with the 'central dot sign'.", unsafe_allow_html=True)
    st.markdown(style_title("Charcot Triad:") + "  A clinical presentation of cholangitis, consisting of fever, right upper quadrant pain, and jaundice.", unsafe_allow_html=True)
    st.markdown(style_title("Klatskin Tumor:") + "  A malignant biliary tumor located at the junction of the right and left hepatic ducts.", unsafe_allow_html=True)
    st.markdown(style_title("Mirizzi Syndrome:") + "  A condition where a lodged stone in the cystic duct compresses the common bile duct, leading to jaundice, pain, and fever.", unsafe_allow_html=True)
    st.markdown(style_title("Parallel Tube Sign:") + "  Enlargement of the common bile duct to the size of the adjacent portal vein within the porta hepatis; also called the 'shotgun sign'.", unsafe_allow_html=True)
    st.markdown(style_title("Sphincter of Oddi:") + "  The muscle that controls the flow of bile and pancreatic juices into the duodenum; also known as the hepatopancreatic sphincter.", unsafe_allow_html=True)
    st.markdown(style_title("Triangular Cord Sign:") + "  A sign associated with biliary atresia in children, characterized by an avascular, echogenic, triangular, or tubular structure anterior to the portal vein, representing fibrous tissue replacing the extrahepatic duct.", unsafe_allow_html=True)
