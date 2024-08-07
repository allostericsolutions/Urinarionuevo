import streamlit as st

# Initialize the variable in session_state
if 'mostrar_artifacts' not in st.session_state:
    st.session_state.mostrar_artifacts = False

# Function to style the artifact titles
def style_title(title):
    return f"<span style='color:darkorange; font-weight:bold;'>{title}</span>"

# Ultrasound Artifacts
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
    ("Speckle Artifacts", "Results from the interference of sound waves with each other, producing a granular or speckled appearance on the images, which may hinder differentiation between smaller structures, like blood vessels.", None)
]

dopp_artifacts = [
    ("Absent Doppler Signal", "This artifact may occur due to low gain, low frequency, high wall filter settings, or an excessively high velocity scale, making it difficult to detect blood flow accurately.", None,
     [
         "Decrease the pulse repetition frequency (PRF)",
         "Increase spectral gain",
         "Decrease the wall filter",
         "Open the sample gate"
     ]),
    ("Aliasing", "Aliasing occurs when the Doppler sampling rate (pulse-repetition frequency) is insufficient to accurately display the Doppler frequency shift.", "Abdominal Sonography Overview/imagenes/aliasing .png",
     [
         "Increase the pulse repetition frequency (PRF)",
         "Adjust the baseline",
         "Switch to a lower transmitted frequency",
         "Increase the angle of insonation to decrease the Doppler shift"
     ])
]

# Display the sections
st.title("Ultrasound Artifacts")

with st.expander("General Artifacts"):
    for artifact in artifacts:
        st.markdown(style_title(artifact[0]) + f": {artifact[1]}", unsafe_allow_html=True)
        if artifact[2]:
            if isinstance(artifact[2], list):
                for img in artifact[2]:
                    st.image(img)
            else:
                st.image(artifact[2])

with st.expander("Doppler Artifacts"):
    for artifact in dopp_artifacts:
        st.markdown(style_title(artifact[0]) + f": {artifact[1]}", unsafe_allow_html=True)
        if artifact[2]:
            st.image(artifact[2])
        st.markdown(style_title("Adjustments") + ":", unsafe_allow_html=True)
        for adjustment in artifact[3]:
            st.markdown(f"- {adjustment}")
