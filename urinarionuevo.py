import random
import streamlit as st

# Corporate branding
st.markdown(
    """<div style="text-align: center;">
    <img src="https://storage.googleapis.com/allostericsolutionsr/Allosteric_Solutions.png" style="width:50%; max-width:200px;">
    </div>""",
    unsafe_allow_html=True
)
st.markdown("[Visit our website](https://www.allostericsolutions.com)")
st.markdown("Contact: [franciscocuriel@allostericsolutions.com](mailto:franciscocuriel@allostericsolutions.com)")

# Questions and answers
questions_and_answers = {
    "Length of the adult kidney": {
        "options": ["7-10 cm", "9-12 cm", "11-14 cm", "13-16 cm"],
        "answer": "9-12 cm"
    },
    "Diameter of the ureters": {
        "options": ["2 mm", "4 mm", "6 mm", "8 mm"],
        "answer": "6 mm"
    },
    # Add other questions as needed
}

# Shuffle the questions
question_list = list(questions_and_answers.items())
random.shuffle(question_list)

# Initialize session state
if 'correct_answers' not in st.session_state:
    st.session_state.correct_answers = 0
if 'answered_questions' not in st.session_state:
    st.session_state.answered_questions = []
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0  # Start with the first question

def create_question(question, options, correct_answer):
    """
    Creates a single question with options and checks the user's response.
    """
    st.write(f"**{question}**")

    # Add an initial option to prompt the user to select
    options = ["Select an option"] + options
    selected_option = st.selectbox("Select an option", options, key=f"selectbox_{st.session_state.current_question}")

    # Only enable the Submit button if a valid option is selected
    if selected_option != "Select an option":
        if st.button("Submit", key=f"button_{st.session_state.current_question}"):
            if selected_option == correct_answer:
                st.success("Correct!")
                st.session_state.correct_answers += 1
            else:
                st.error("Incorrect.")
                st.session_state.incorrect_questions.append((question, options[1:], correct_answer))  # Append excluding the "Select an option" entry

            st.session_state.answered_questions.append((question, options, correct_answer))
            st.session_state.current_question += 1
            st.experimental_rerun()  # Force a rerun to show the next question
    else:
        st.warning("You need to select an option to submit.")

# Display the current question
if st.session_state.current_question < len(question_list):
    question, q_data = question_list[st.session_state.current_question]
    create_question(question, q_data["options"], q_data["answer"])
else:
    st.write("### Quiz Completed!")
    
    # Show grade
    total_questions = len(questions_and_answers)
    percentage = (st.session_state.correct_answers / total_questions) * 100
    
    st.markdown(f"### Your final grade: {st.session_state.correct_answers}/{total_questions} ({percentage:.1f}%)")
    
    if percentage <= 50:
        st.write("You need more practice. Keep going!")
    elif percentage <= 70:
        st.write("Good effort, but there's room for improvement.")
    elif percentage <= 85:
        st.write("Well done!")
    elif percentage <= 90:
        st.write("Very good!")
    else:
        st.write("Excellent!")
    
    # Option to retry incorrect questions
    if st.button("Retry Incorrect Questions") and st.session_state.incorrect_questions:
        st.session_state.question_list = st.session_state.incorrect_questions.copy()
        random.shuffle(st.session_state.question_list)
        st.session_state.incorrect_questions.clear()
        st.session_state.correct_answers = 0
        st.session_state.current_question = 0
        st.session_state.answered_questions.clear()
        st.experimental_rerun()
