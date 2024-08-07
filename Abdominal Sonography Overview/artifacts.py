import streamlit as st

# Initialize the variable in session_state
if 'mostrar_artifacts' not in st.session_state:
    st.session_state.mostrar_artifacts = False

# Function to style the artifact titles
def style_title(title):
    return f"<span style='color:darkorange; font-weight:bold;'>{title}</span>"

# Ultrasound Artifacts
artifacts = [
    ("Anisotropy", 
     "This phenomenon occurs when the sound beam strikes a structure at a non-perpendicular angle, leading to a loss of the structure's true echogenicity. It can result in an inaccurate representation of tendon imaging.", 
     "Abdominal Sonography Overview/imagenes/anisotrophy.png", 
     "Anisotropy. Left image is obtained perpendicular to the tendon (arrows), whereas the right image has been obtained in an obliqued orientation to the tendon."
    ),
    ("Comet-tail Artifact", 
     "Comet tail artifacts are generated from closely spaced, highly reflective interfaces. Often seen in cases of adenomyomatosis of the gallbladder.", 
     "Abdominal Sonography Overview/imagenes/comet tail.png",
     "Comet tail artifact observed as a tapering, bright line extending from the anterior wall of the gallbladder."
    ),
    ("Dirty Shadowing", 
     "This artifact arises due to the presence of gas within the bowel, obstructing the ultrasound signal and creating shadowing effects. It can obscure important anatomical details.", 
     "Abdominal Sonography Overview/imagenes/dirty_shadowing.png",
     "The image displays both a ring-down artifact and 'dirty shadowing' caused by gas in the duodenum. The central region exhibits a ring-down appearance characterized by an echogenic step-ladder. Surrounding the ring-down is the dirty shadowing effect, which complicates visualization."
    ),
    ("Edge Shadowing", 
     "This reflective effect occurs when sound waves encounter a sudden change in tissue density, such as at the boundary between two organs. It may produce a bright line that can obscure underlying structures.", 
     "Abdominal Sonography Overview/imagenes/Refraction, edge shadowing.png"),
    ("Mirror Image Artifact", 
     "Produced by strong specular reflectors, this artifact causes a duplicate of anatomical structures to appear deeper than their correct location. It may lead to confusion, especially in areas posterior to the liver and diaphragm. Moving the transducer will make the mirrored structure disappear, while the original structure remains.", 
     "Abdominal Sonography Overview/imagenes/Mirrow.png"),
    ("Acoustic Enhancement", 
     "This phenomenon results when the sound beam is minimally attenuated while passing through a fluid-filled structure, leading to increased brightness posterior to the structure. It is commonly observed behind the gallbladder and renal cysts, enhancing the appearance of the surrounding tissues.", 
     "Abdominal Sonography Overview/imagenes/shadowing, enhacement.png",
     "Image enhancement and shadowing are created by anatomy with low attenuation, such as fluid-filled cysts, and high attenuation, such as calcifications. Anatomic examples illustrate through transmission (enhancement) distal to a cyst and shadowing distal to a gallstone."
    ),
    ("Refraction", 
     "Refraction occurs when the sound beam bends as it crosses an interface between tissues with significantly different densities, leading to artifacts such as acoustic shadowing at the interface or duplication effects.", 
     "Abdominal Sonography Overview/imagenes/REfractions.png"),
    ("Reverberation Artifact", 
     "Reverberation artifacts arise from multiple echoes generated between highly reflective and parallel structures that interact at a perpendicular angle to the ultrasound beam. These artifacts are often caused by reflections between a reflective interface and the transducer or between reflective interfaces, such as metallic objects, calcified tissues, or air pocket/partial liquid areas of the anatomy. They are manifested as multiple equally spaced parallel lines at progressive depth with decreasing amplitude and can hinder visualization of deeper anatomy. ",
     ["Abdominal Sonography Overview/imagenes/Reververation image.png", "Abdominal Sonography Overview/imagenes/reververatios artifactos .png"],
     "Left: Reverberation artifacts arise from a highly reflective boundary close to the transducer surface that then reflects echoes from the transducer back to the boundary several times, displaying multiple equally spaced structures that decrease in intensity with depth. Right: Ring-down artifacts show long reverberations due to resonant vibrations in air bubbles contained within the anatomy."
    ),
    ("Ring-down Artifact", 
     "Ring-down artifacts are generated by resonant vibrations in air bubbles contained in abscesses, emphysematous infections, and other processes that contain air, often resulting in long reverberations at depth in the image.", 
     "Abdominal Sonography Overview/imagenes/reververatios artifactos .png",
     "Comet tail artifacts are generated from closely spaced, highly reflective interfaces. Ultrasound of the gallbladder with adenomyomatosis demonstrating comet tail artifacts from the anterior gallbladder wall, probably due to cholesterol crystals within Rokitansky–Aschoff sinuses. (B) Ring-down artifacts are generated by resonant vibrations in air bubbles contained in abscesses, emphysematous infections, and other processes that contain air, often resulting in long reverberations at depth in the image."
    ),
    ("Shadowing", 
     "Occurs when sound waves are obstructed by dense objects or gas-filled organs, leading to a loss of signal that results in a shadow on the image. This obscures important anatomical details and complicates interpretation.", 
     "Abdominal Sonography Overview/imagenes/Shadowing.png"),
    ("Side Lobes", 
     "Generated by sound beams that originate outside the main beam path, resulting in low-level echoes that can mimic sludge, debris, or pus within a fluid-filled structure.", 
     None),
    ("Slice Thickness", 
     "This artifact arises from the compression of 3D data into 2D images, creating the illusion of false echoes resembling debris in the bladder or gallbladder. Slice thickness artifacts are typically seen in transverse views of the urinary bladder when adjacent structures are incorporated into the anechoic urinary bladder fluid.", 
     "Abdominal Sonography Overview/imagenes/Slice thickness.png"),
    ("Speed Displacement", 
     "This artifact results from the substantial variability of sound speed in fat (1450 m/s) compared to soft tissues (1540 m/s), which is about a 6% slower propagation speed. This leads to the distal displacement of anatomic borders when ultrasound interacts with fat-containing structures, affecting the accuracy of distance measurements.", 
     ["Abdominal Sonography Overview/imagenes/speed displacement.jpg", "Abdominal Sonography Overview/imagenes/speed displacement.png"])
]

dopp_artifacts = [
    ("Absent Doppler Signal", 
     "This artifact may occur due to low gain, low frequency, high wall filter settings, or an excessively high velocity scale, making it difficult to detect blood flow accurately.", 
     None,
     [
         "Decrease the pulse repetition frequency (PRF)",
         "Increase spectral gain",
         "Decrease the wall filter",
         "Open the sample gate"
     ]),
    ("Aliasing", 
     "Aliasing occurs when the Doppler sampling rate (pulse-repetition frequency) is insufficient to accurately display the Doppler frequency shift.", 
     "Abdominal Sonography Overview/imagenes/aliasing .png",
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
                    st.image(img, caption=artifact[3] if len(artifact) > 3 else None)
            else:
                st.image(artifact[2], caption=artifact[3] if len(artifact) > 3 else None)

with st.expander("Doppler Artifacts"):
    for artifact in dopp_artifacts:
        st.markdown(style_title(artifact[0]) + f": {artifact[1]}", unsafe_allow_html=True)
        if artifact[2]:
            st.image(artifact[2])
        st.markdown(style_title("Adjustments") + ":", unsafe_allow_html=True)
        for adjustment in artifact[3]:
            st.markdown(f"- {adjustment}")
