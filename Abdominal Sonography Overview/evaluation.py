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
                <source src="https://www.zapsplat.com/wp-content/uploads/2015/sound-effects-46437/zapsplat_multimedia_game_sound_collect_coin_002_47384.mp3" type="audio/mp3">
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
                <source src="https://www.zapsplat.com/wp-content/uploads/2015/sound-effects-46437/zapsplat_multimedia_game_sound_collect_coin_002_47384.mp3" type="audio/mp3">
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
                <source src="https://www.zapsplat.com/wp-content/uploads/2015/sound-effects-46437/zapsplat_multimedia_game_sound_wrong_buzzer_001_47535.mp3" type="audio/mp3">
                Your browser does not support the audio element.
            </audio>
            """,
            unsafe_allow_html=True
        )
