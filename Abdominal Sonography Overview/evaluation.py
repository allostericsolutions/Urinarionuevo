import streamlit as st

st.title("Peritoneal vs. Retroperitoneal Organs")

# Organ Lists
peritoneales = [
    "Stomach", "Liver", "Spleen", "First part of the Duodenum", "Jejunum",
    "Ileum", "Transverse Colon", "Sigmoid Colon", "Appendix", "Upper Rectum"
]
retroperitoneales = [
    "Kidneys", "Adrenal Glands", "Ureters", "Pancreas (except tail)",
    "Duodenum (except first part)", "Ascending Colon", "Descending Colon",
    "Middle and Lower Rectum", "Abdominal Aorta", "Inferior Vena Cava"
]

# Combine lists for the selectbox
all_organs = peritoneales + retroperitoneales

# Selectbox for the organ
selected_organ = st.selectbox("Select an organ:", all_organs)

# Selectbox for the location
location = st.selectbox("Where is this organ located?", ["Peritoneal", "Retroperitoneal"])

# Check the answer
if st.button("Check Answer"):
    if selected_organ in peritoneales and location == "Peritoneal":
        st.success("Correct! 🎉")
        st.markdown(
            """
            <audio autoplay>
                <source src="https://www2.cs.uic.edu/~i101/SoundFiles/StarWars3.wav" type="audio/wav">
                Your browser does not support the audio element.
            </audio>
            """,
            unsafe_allow_html=True
        )
    elif selected_organ in retroperitoneales and location == "Retroperitoneal":
        st.success("Correct! 🎉")
        st.markdown(
            """
            <audio autoplay>
                <source src="https://www2.cs.uic.edu/~i101/SoundFiles/StarWars3.wav" type="audio/wav">
                Your browser does not support the audio element.
            </audio>
            """,
            unsafe_allow_html=True
        )
    else:
        st.error("Incorrect. Try again! ❌")
        st.markdown(
            """
            <audio autoplay>
                <source src="https://www2.cs.uic.edu/~i101/SoundFiles/ImperialMarch60.wav" type="audio/wav">
                Your browser does not support the audio element.
            </audio>
            """,
            unsafe_allow_html=True
