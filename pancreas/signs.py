import streamlit as st

# Initialize the variable in session_state
if 'mostrar_eponimos' not in st.session_state:
    st.session_state.mostrar_eponimos = False

# Function to style the titles
def style_title(title):
    return f"<span style='color:darkorange; font-weight:bold;'>{title}</span>"

# Expandable and collapsible section
with st.expander("Signs & Terms in Abdominal Sonography:", expanded=st.session_state.mostrar_eponimos):
    st.markdown(style_title("Ampulla of Vater:") + " The point where the pancreatic duct and the common bile duct merge just before the sphincter of Oddi; also called the hepatopancreatic ampulla.", unsafe_allow_html=True)
    st.markdown(style_title("Caroli Disease:") + " A congenital disorder characterized by segmental dilatation of the intrahepatic bile ducts. Associated with the 'central dot sign'.", unsafe_allow_html=True)
    st.markdown(style_title("Charcot Triad:") + "  A clinical presentation of cholangitis, consisting of fever, right upper quadrant pain, and jaundice.", unsafe_allow_html=True)
    st.markdown(style_title("Klatskin Tumor:") + "  A malignant biliary tumor located at the junction of the right and left hepatic ducts.", unsafe_allow_html=True)
    st.markdown(style_title("Mirizzi Syndrome:") + "  A condition where a lodged stone in the cystic duct compresses the common bile duct, leading to jaundice, pain, and fever.", unsafe_allow_html=True)
    st.markdown(style_title("Parallel Tube Sign:") + "  Enlargement of the common bile duct to the size of the adjacent portal vein within the porta hepatis; also called the 'shotgun sign'.", unsafe_allow_html=True)
    st.markdown(style_title("Sphincter of Oddi:") + "  The muscle that controls the flow of bile and pancreatic juices into the duodenum; also known as the hepatopancreatic sphincter.", unsafe_allow_html=True)
    st.markdown(style_title("Triangular Cord Sign:") + "  A sign associated with biliary atresia in children, characterized by an avascular, echogenic, triangular, or tubular structure anterior to the portal vein, representing fibrous tissue replacing the extrahepatic duct.", unsafe_allow_html=True)

    st.markdown("## Signs in Pancreatic Ultrasound:")
    st.markdown(style_title("Double-duct Sign:") + " Coexisting enlargement of the common bile duct and pancreatic duct.", unsafe_allow_html=True)
    st.markdown(style_title("Pancreatic Pseudocyst:") + " A fluid-filled cyst surrounded by fibrous tissue, typically formed by leaked pancreatic enzymes.", unsafe_allow_html=True)
    st.markdown(style_title("Whipple Triad:") + "  A set of clinical indicators suggestive of a functional insulinoma:  Hypoglycemia (low blood sugar), low fasting glucose levels, and relief of symptoms with intravenous glucose administration.", unsafe_allow_html=True)

    # Explanation of double bubble sign in the context of annular pancreas
    st.markdown(style_title("Double Bubble Sign in Annular Pancreas:") + " In the context of annular pancreas, the 'double bubble' sign on ultrasound is an important diagnostic clue. Annular pancreas is a congenital condition where a ring of pancreatic tissue encircles and narrows the duodenum, leading to obstruction. This sign shows two dark, rounded areas on the ultrasound: - The first bubble is the distended stomach filled with fluid or gas due to the blockage. - The second bubble is the dilated part of the duodenum just before the point where it is encircled by pancreatic tissue. This 'double bubble' can indicate duodenal obstruction caused by the annular pancreas. It is often diagnosed in neonates or infants due to symptoms like vomiting and feeding difficulties. In adults, it may be detected during evaluations for chronic duodenal obstruction or pancreatitis. When the 'double bubble' sign is noted, further imaging such as an upper gastrointestinal series, CT, or MRI is typically performed to confirm the diagnosis. Treatment usually involves surgery to bypass the obstructed section of the duodenum and relieve symptoms.", unsafe_allow_html=True)

    st.markdown("## Other Pancreatic Terms:")
    st.markdown(style_title("Hyperamylasemia:") + " Elevated levels of amylase in the blood, often associated with pancreatitis.", unsafe_allow_html=True)
    st.markdown(style_title("Pancreatic Steatosis:") + " Fatty infiltration of the pancreas, which can be caused by alcohol abuse or other factors.", unsafe_allow_html=True)
    st.markdown(style_title("Phlegmon:") + " A peripancreatic fluid collection resulting from pancreatic inflammation.", unsafe_allow_html=True)
