import streamlit as st

# Initialize the variable in session_state
if 'mostrar_eponimos' not in st.session_state:
    st.session_state.mostrar_eponimos = False

# Function to style the sign titles
def style_title(title):
    return f"<span style='color:darkorange; font-weight:bold;'>{title}</span>"

# Ultrasound Signs by Region
# Gallbladder
gallbladder_signs = [
    ("Ball-on-the-wall sign", "Appearance of a gallbladder polyp."),
    ("Cinnamon bun sign", "Air within the gallbladder wall associated with emphysematous cholecystitis."),
    ("Whirlpool sign", "Cystic duct appearance with color Doppler associated with gallbladder torsion."),
    ("Wall-echo-shadow (WES) sign", "Appearance of a gallbladder completely filled with stones."),
    ("Olive sign", "Pain with probe pressure over the gallbladder."),
    ("Murphy sign", "Pain with probe pressure over the gallbladder."),
    ("Pseudogallbladder sign", "Cystic structure noted in the gallbladder fossa without evidence of an actual gallbladder; associated with biliary atresia in children.")
]

# Liver
liver_signs = [
    ("Central dot sign", "Echogenic dot in dilated intrahepatic ducts associated with Caroli disease."),
    ("Mickey sign", "Cross section appearance of the porta hepatis."),
    ("Starry sky sign", "Bright portal triads seen with hepatitis."),
    ("Water lily sign", "Pericyst surrounding a free floating endocyst; associated with a hydatid liver cyst."),
    ("Turtleback sign", "Calcified septa and fibrosis associated with schistosomiasis."),
    ("Triangle cord sign", "Avascular, triangular, or tubular structure representing fibrous replacement of duct associated with biliary atresia.")
]

# Lungs
lungs_signs = [
    ("Barcode sign", "Abnormal M-mode appearance of lung sliding indicating pneumothorax."),
    ("Seashore sign", "Normal M-mode tracing of lung sliding.")
]

# Bowel
bowel_signs = [
    ("Double-duct sign", "Dilatation of both the pancreatic duct and common bile duct."),
    ("Doughnut sign (target sign)", "Dilatation of both the pancreatic and common bile duct."),
    ("Keyboard sign", "Seen in small bowel obstruction."),
    ("McBurney sign", "Pain over McBurney point in the right lower quadrant."),
    ("Rovsing sign", "Right lower quadrant pain when the left lower quadrant is palpated."),
    ("Short-axis sign", "Short axis appearance of intussusception."),
    ("Pseudokidney sign", "Longitudinal appearance of intussusception (may be used for some bowel masses also).")
]

# Scrotum
scrotum_signs = [
    ("Central dot sign", "Torsed appendage of the testicle that can be seen superficially.")
]

# Pancreas
pancreas_signs = []  # There are no eponymous signs for the pancreas in this list

# Display the sections
st.title("Ultrasound Signs")

with st.expander("Gallbladder Ultrasound Signs"):
    for item in gallbladder_signs:
        st.markdown(style_title(item[0]) + f": {item[1]}", unsafe_allow_html=True)

with st.expander("Liver Ultrasound Signs"):
    for item in liver_signs:
        st.markdown(style_title(item[0]) + f": {item[1]}", unsafe_allow_html=True)

with st.expander("Lungs Ultrasound Signs"):
    for item in lungs_signs:
        st.markdown(style_title(item[0]) + f": {item[1]}", unsafe_allow_html=True)

with st.expander("Bowel Ultrasound Signs"):
    for item in bowel_signs:
        st.markdown(style_title(item[0]) + f": {item[1]}", unsafe_allow_html=True)

with st.expander("Scrotum Ultrasound Signs"):
    for item in scrotum_signs:
        st.markdown(style_title(item[0]) + f": {item[1]}", unsafe_allow_html=True)

with st.expander("Pancreas Ultrasound Signs"):
    for item in pancreas_signs:
        st.markdown(style_title(item[0]) + f": {item[1]}", unsafe_allow_html=True)
