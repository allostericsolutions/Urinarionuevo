import random
import streamlit as st
from fpdf import FPDF

# Encabezado con Logo y Links
LOGO_URL = "https://storage.googleapis.com/allostericsolutionsr/Allosteric_Solutions.png"
WEBSITE_URL = "https://www.allostericsolutions.com"
CONTACT_EMAIL = "franciscocuriel@allostericsolutions.com"

# Generate PDF
def generate_pdf(responses):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Add logo
    pdf.image(LOGO_URL, x=10, y=8, w=25)
    
    # Add title
    pdf.cell(200, 10, txt="Allosteric Solutions", ln=True, align="C")
    pdf.cell(200, 10, txt=f"Visit our website: {WEBSITE_URL}", ln=True, align="C")
    pdf.cell(200, 10, txt=f"Contact: {CONTACT_EMAIL}", ln=True, align="C")
    
    # Add a space
    pdf.ln(20)
    
    # Add responses
    for i, (question, response) in enumerate(responses.items(), 1):
        pdf.cell(200, 10, txt=f"{i}. {question}", ln=True)
        pdf.cell(200, 10, txt=f"   - Correct Answer: {response['answer']}", ln=True)
        pdf.multi_cell(0, 10, txt=f"   - Explanation: {response['explanation']}", align="L")
        pdf.ln(5)
    
    return pdf

# Questions and answers explanation
questions_and_answers = {
    "Length of the adult kidney": {
        "options": ["7-10 cm", "9-12 cm", "11-14 cm", "13-16 cm"],
        "answer": "9-12 cm",
        "explanation": "The normal length of an adult kidney observed via ultrasound is between 9-12 cm. Kidneys measuring below 9 cm may indicate chronic kidney disease (CKD), whereas lengths exceeding 12 cm could suggest hypertrophy due to compensatory mechanisms or chronic conditions like diabetes or hypertension (ARDMS Core Curriculum for Ultrasound)."
    },
    "Width of the adult kidney": {
        "options": ["2-4 cm", "4-6 cm", "6-8 cm", "8-10 cm"],
        "answer": "4-6 cm",
        "explanation": "The width of an adult kidney, typically falling between 4-6 cm as seen on ultrasound, is essential for gauging the organ’s health. Ensuring a normal width helps confirm that the kidney has adequate filtration capacity and no signs of swelling or shrinkage (ARDMS guidelines)."
    },
    # Add other questions here ...
}

NUM_QUESTIONS = 8

# Initialize session state
def initialize_state():
    if len(questions_and_answers) >= NUM_QUESTIONS:  # Check if there are enough questions
        st.session_state.correct_answers = 0
        st.session_state.answered_questions = []
        st.session_state.current_question = 0
        st.session_state.incorrect_questions = []
        st.session_state.question_list = random.sample(list(questions_and_answers.items()), NUM_QUESTIONS)
    else:
        st.error(f"Not enough questions in the pool to sample {NUM_QUESTIONS} questions.")

if 'question_list' not in st.session_state:
    initialize_state()
elif len(st.session_state.question_list) != NUM_QUESTIONS and not st.session_state.incorrect_questions:
    # Solo resetear si no están tratando de reintentar las incorrectas
    initialize_state()

# Create Question function
def create_question(question, options, correct_answer):
    st.write(f"**{question}**")
    options = ["Select an option"] + options
    selected_option = st.selectbox("Select an option", options, key=f"selectbox_{st.session_state.current_question}")

    if st.button("Submit", key=f"button_{st.session_state.current_question}"):
        if selected_option != "Select an option":
            if selected_option == correct_answer:
                st.success("Correct!")
                st.session_state.correct_answers += 1
            else:
                st.error("Incorrect.")
                st.session_state.incorrect_questions.append((question, {"options": options[1:], "answer": correct_answer}))  # Exclude "Select an option"

            st.session_state.answered_questions.append((question, {"options": options[1:], "answer": correct_answer}))
            st.session_state.current_question += 1
            st.experimental_rerun()  # Force a rerun to show the next question
        else:
            st.warning("You need to select an option to submit.")

# Display the current question
if st.session_state.current_question < len(st.session_state.question_list):
    question, q_data = st.session_state.question_list[st.session_state.current_question]
    create_question(question, q_data["options"], q_data["answer"])
else:
    st.write("### Quiz Completed!")
    
    # Calculate and display the score
    total_questions = len(st.session_state.question_list)
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

    # Function to download the PDF with answers and explanations
    if st.button("Download PDF with Explanations"):
        responses = {q[0]: questions_and_answers[q[0]] for q in st.session_state.answered_questions}
        pdf = generate_pdf(responses)
        pdf_output = pdf.output(dest='S').encode('latin1')
        st.download_button(label="Download PDF",
                           data=pdf_output,
                           file_name="ultrasound_explanations.pdf",
                           mime='application/pdf')

    # Option to retry incorrect questions
    if st.button("Retry Incorrect Questions") and st.session_state.incorrect_questions:
        st.session_state.question_list = st.session_state.incorrect_questions.copy()
        random.shuffle(st.session_state.question_list)
        st.session_state.incorrect_questions.clear()
        st.session_state.correct_answers = 0
        st.session_state.current_question = 0
        st.session_state.answered_questions.clear()
        st.experimental_rerun()

    if st.button("Start a New Quiz"):
        initialize_state()
        st.experimental_rerun()
