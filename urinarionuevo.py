import random
import streamlit as st

# Corporate branding
st.image("https://storage.googleapis.com/allostericsolutionsr/Allosteric_Solutions.png", use_column_width=True)
st.markdown("[Visit our website](https://www.allostericsolutions.com)")
st.markdown("Contact: [franciscocuriel@allostericsolutions.com](mailto:franciscocuriel@allostericsolutions.com)")

# Questions and answers
questions_and_answers = {
    "Length of the adult kidney": {
        "options": ["7-10 cm", "9-12 cm", "11-14 cm", "13-16 cm"],
        "answer": "9-12 cm"
    },
    "Width of the adult kidney": {
        "options": ["2-4 cm", "4-6 cm", "6-8 cm", "8-10 cm"],
        "answer": "4-6 cm"
    },
    "Length of the neonatal kidney": {
        "options": ["1.5-2.5 cm", "2-3 cm", "3.5-5.0 cm", "4-6 cm"],
        "answer": "3.5-5.0 cm"
    },
    "Width of the neonatal kidney": {
        "options": ["1-2 cm", "2-3 cm", "3-4 cm", "4-5 cm"],
        "answer": "2-3 cm"
    },
    "Length of the ureters": {
        "options": ["10-15 cm", "15-20 cm", "20-25 cm", "28-34 cm"],
        "answer": "28-34 cm"
    },
    "Diameter of the ureters": {
        "options": ["2 mm", "4 mm", "6 mm", "8 mm"],
        "answer": "6 mm"
    },
    "Thickness of the bladder wall": {
        "options": ["1-3 mm", "3-6 mm", "6-9 mm", "9-12 mm"],
        "answer": "3-6 mm"
    },
    "Length of the female urethra": {
        "options": ["2 cm", "4 cm", "6 cm", "8 cm"],
        "answer": "4 cm"
    },
    "Length of the male urethra": {
        "options": ["10 cm", "15 cm", "20 cm", "25 cm"],
        "answer": "20 cm"
    },
    "AP dimension of the adult kidney": {
        "options": ["1.5-2.5 cm", "2-3 cm", "2.5-4.0 cm", "3-4 cm"],
        "answer": "2.5-4.0 cm"
    },
    "AP dimension of the neonatal kidney": {
        "options": ["0.5-1.5 cm", "1-2 cm", "1.5-2.5 cm", "2-3 cm"],
        "answer": "1.5-2.5 cm"
    }
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
    st.write(f"**{question}**")
    
    selected_option = st.radio("", options, key=question, index=-1)  # Do not preselect any option
    
    if st.button("Submit", key=f"button_{question}"):
        if selected_option:
            if selected_option == correct_answer:
                st.success("Correct")
                st.session_state.correct_answers += 1
            else:
                st.error("Incorrect")
                st.session_state.incorrect_questions.append((question, options, correct_answer))
            
            st.session_state.answered_questions.append((question, options, correct_answer))
            st.session_state.current_question += 1
            st.experimental_rerun()  # Force a rerun to show the next question

# Display the current question
if st.session_state.current_question < len(question_list):
    question, q_data = question_list[st.session_state.current_question]
    create_question(question, q_data["options"], q_data["answer"])
else:
    st.write("Quiz Completed")

    # Show grade
    total_questions = len(questions_and_answers)
    percentage = (st.session_state.correct_answers / total_questions) * 100
    
    st.markdown(f"### Your final grade is: {st.session_state.correct_answers}/{total_questions} ({percentage:.1f}%)")
    
    if percentage <= 50:
        st.write("You need more practice. Keep going!")
    elif percentage <= 70:
        st.write("Good effort, but there's room for improvement.")
    elif percentage <= 85:
        st.write("Well done, but you can do better.")
    elif percentage <= 90:
        st.write("Very good!")
    else:
        st.write("Excellent!")

    # Option to retry incorrect questions
    if st.button("Retry Incorrect Questions") and st.session_state.incorrect_questions:
        question_list = st.session_state.incorrect_questions.copy()
        random.shuffle(question_list)
        st.session_state.incorrect_questions.clear()
        st.session_state.correct_answers = 0
        st.session_state.current_question = 0
        st.session_state.answered_questions.clear()
        st.experimental_rerun()
