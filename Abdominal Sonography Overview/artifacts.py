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
    ("Cinnamon bun sign", " Short axis appearance of intussusception "),
    ("Whirlpool sign", "Cystic duct appearance with color Doppler associated with gallbladder torsion."),
    ("Wall-echo-shadow (WES) sign", "Appearance of a gallbladder completely filled with stones."),
    ("Olive sign", "Palpable hypertrophic pyloric muscle associated with pyloric stenosis"),
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
pancreas_signs = [] # There are no eponymous signs for the pancreas in this list

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

# Display Artifacts Section
st.title("Ultrasound Artifacts")

# Call additional artifacts code
import Abdominal Sonography Overview.artifacts

# Example artifacts code from the previous example
artifacts = [
    ("Anisotropy", "This phenomenon occurs when the sound beam strikes a structure at a non-perpendicular angle, leading to a loss of the structure's true echogenicity. It can result in an inaccurate representation of tendon imaging.", None),
    ("Comet-tail Artifact", "This artifact is the result of multiple small, highly reflective interfaces creating a characteristic pattern. It is commonly seen in cases of adenomyomatosis of the gallbladder.", "Abdominal Sonography Overview/imagenes/comet tail.png"),
    ("Dirty Shadowing", "Caused by the presence of air or gas within the bowel, this artifact affects image quality and can obscure important details. It is frequently noted when the ultrasound beam encounters gas-filled structures.", None),
    ("Edge Shadowing", "This reflective effect occurs when sound waves encounter a sudden change in tissue density, such as at the boundary between two organs. It may produce a bright line that can obscure underlying structures.", "Abdominal Sonography Overview/imagenes/Refraction, edge shadowing.png"),
    ("Mirror Image Artifact", "Produced by strong specular reflectors, this artifact causes a duplicate of anatomical structures to appear deeper than their correct location. It may lead to confusion, especially in areas posterior to the liver and diaphragm. Moving the transducer will make the mirrored structure disappear, while the original structure remains.", "Abdominal Sonography Overview/imagenes/Mirrow.png"),
    ("Acoustic Enhancement", "This phenomenon results when the sound beam is minimally attenuated while passing through a fluid-filled structure, leading to increased brightness posterior to the structure. It is commonly observed behind the gallbladder and renal cysts, enhancing the appearance of the surrounding tissues.", "Abdominal Sonography Overview/imagenes/shadowing, enhacement.png"),
    ("Refraction", "Refraction occurs when the sound beam bends as it crosses an interface between tissues with significantly different densities, leading to artifacts such as acoustic shadowing at the interface or duplication effects.", "Abdominal Sonography Overview/imagenes/REfractions.png"),
    ("Reverberation Artifact", "These artifacts happen when sound waves bounce between two surfaces, resulting in multiple echoes that appear as parallel lines on the image. They are commonly found in regions where sound interacts with various tissue layers or air.", "Abdominal Sonography Overview/imagenes/Reververation image.png"),
    ("Ring-down Artifact", "This artifact manifests as a solid streak or a series of parallel bands radiating from gas bubbles within the abdomen. It can aid in identifying the presence of air in certain structures.", None),
    ("Shadowing", "Occurs when sound waves are obstructed by dense objects or gas-filled organs, leading to a loss of signal that results in a shadow on the image. This obscures important anatomical details and complicates interpretation.", "Abdominal Sonography Overview/imagenes/Shadowing.png"),
    ("Side Lobes", "Generated by sound beams that originate outside the main beam path, resulting in low-level echoes that can mimic sludge, debris, or pus within a fluid-filled structure.", None),
    ("Slice Thickness", "This artifact arises from the compression of 3D data into 2D images, creating the illusion of false echoes resembling debris in the bladder or gallbladder. Slice thickness artifacts are typically seen in transverse views of the urinary bladder when adjacent structures are incorporated into the anechoic urinary bladder fluid.", "Abdominal Sonography Overview/imagenes/Slice thickness.png"),
    ("Speed Displacement", "This artifact results from the substantial variability of sound speed in fat (1450 m/s) compared to soft tissues (1540 m/s), which is about a 6% slower propagation speed. This leads to the distal displacement of anatomic borders when ultrasound interacts with fat-containing structures, affecting the accuracy of distance measurements.", ["Abdominal Sonography Overview/imagenes/speed displacement.jpg", "Abdominal Sonography Overview/imagenes/speed displacement.png"]),
    ("Attenuation Artifacts", "Caused by the loss of energy as sound waves pass through tissue, resulting in hypoechoic or anechoic areas on the image, complicating the visualization of structures.", None),
    ("Enhancement Artifacts", "These occur when structures with low acoustic impedance artificially increase brightness below them, making it challenging to visualize underlying structures, such as blood vessels or the bladder.", None),
    ("Speckle Artifacts", "Results from the interference of sound waves with each other, producing a granular or speckled appearance on the images, which may hinder differentiation between smaller structures, like blood vessels.", None),
    ("Absent Doppler Signal", "This artifact may occur due to low gain, low frequency, high wall filter settings, or an excessively high velocity scale, making it difficult to detect blood flow accurately. Adjustments: Decrease the pulse repetition frequency (PRF), Increase spectral gain, Decrease the wall filter, Open the sample gate.", None),
    ("Aliasing", "Aliasing occurs when the Doppler sampling rate (pulse-repetition frequency) is insufficient to accurately display the Doppler frequency shift. Adjustments: Increase the PRF, Adjust the baseline, Switch to a lower transmitted frequency, Increase the angle of insonation to decrease the Doppler shift.", "Abdominal Sonography Overview/imagenes/aliasing .png")
]

# Display the Artifacts
for artifact in artifacts:
    st.markdown(style_title(artifact[0]) + f": {artifact[1]}", unsafe_allow_html=True)
    if artifact[2]:
        if isinstance(artifact[2], list):
            for img in artifact[2]:
                st.image(img)
        else:
            st.image(artifact[2])
