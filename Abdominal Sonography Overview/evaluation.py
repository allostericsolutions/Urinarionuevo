import streamlit as st
import pandas as pd

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

# Initialize variables for scoring
score = 0
total_questions = len(all_organs)
questions_answered = 0
scores = []  # List to store scores after each question

# Loop through each organ 
for i in range(total_questions):
    # Selectbox for the organ
    selected_organ = st.selectbox(f"Select organ {i+1}:", all_organs)

    # Selectbox for the location
    location = st.selectbox(f"Where is {selected_organ} located?", ["Peritoneal", "Retroperitoneal"])

    # Check the answer
    if st.button(f"Check Answer {i+1}"):
        if (selected_organ in peritoneales and location == "Peritoneal") or (selected_organ in retroperitoneales and location == "Retroperitoneal"):
            score += 1
            st.success("Correct! 🎉")
            scores.append(score)  # Update the scores list
            st.line_chart(pd.DataFrame({"Score": scores}))  # Update line chart
        else:
            st.error("Incorrect. Try again! ❌")
            scores.append(score)  # Update the scores list
            st.line_chart(pd.DataFrame({"Score": scores}))  # Update line chart
        questions_answered += 1

        # Check if all questions answered
        if questions_answered == total_questions:
            st.write(f"You answered {score} out of {total_questions} questions correctly!")
            if score == total_questions:
                st.success("Congratulations! You aced the quiz! 🎉")
            else:
                st.info("Keep practicing! You can do it!")
