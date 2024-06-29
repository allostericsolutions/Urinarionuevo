import random
import streamlit as st
from fpdf import FPDF
import requests
from io import BytesIO
import tempfile
import os

# Encabezado con Logo y Links
LOGO_URL = "https://storage.googleapis.com/allostericsolutionsr/Allosteric_Solutions.png"
WEBSITE_URL = "https://www.allostericsolutions.com"
CONTACT_EMAIL = "franciscocuriel@allostericsolutions.com"

# Mostrar imagen corporativa y links en Streamlit
st.image(LOGO_URL, width=150)
st.markdown(f"[Visit our website]({WEBSITE_URL})")
st.markdown(f"Contact: [franciscocuriel@allostericsolutions.com](mailto:{CONTACT_EMAIL})")

# Custom PDF class to include the header with logo and support Unicode
class PDF(FPDF):
    def header(self):
        if hasattr(self, 'logo_path'):
            self.image(self.logo_path, 10, 8, 33)
        self.set_font('Arial', 'B', 12)
        self.cell(80)
        self.cell(30, 10, 'Allosteric Solutions', 0, 1, 'C')
        self.cell(80)
        self.set_font('Arial', '', 9)
        self.cell(30, 10, f'Visit our website: {WEBSITE_URL}', 0, 1, 'C')
        self.cell(80)
        self.cell(30, 10, f'Contact: {CONTACT_EMAIL}', 0, 1, 'C')
        self.ln(20)

    def add_chapter(self, title, body):
        self.add_page()
        self.chapter_title(title)
        self.chapter_body(body)

    def chapter_title(self, title):
        self.set_font('FreeSerif', 'B', 12)
        self.cell(0, 10, title.encode('latin1', 'replace').decode('latin1'), 0, 1, 'L')
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('FreeSerif', '', 12)
        self.multi_cell(0, 10, body.encode('latin1', 'replace').decode('latin1'))
        self.ln()

def generate_pdf(responses):
    pdf = PDF()
    pdf.add_page()
    
    # Add the header for each chapter
    if hasattr(pdf, 'logo_path'):
        pdf.image(pdf.logo_path, 10, 8, 33)
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(80)
    pdf.cell(30, 10, 'Allosteric Solutions', 0, 1, 'C')
    pdf.cell(80)
    pdf.set_font('Arial', '', 9)
    pdf.cell(30, 10, f'Visit our website: {WEBSITE_URL}', 0, 1, 'C')
    pdf.cell(80)
    pdf.cell(30, 10, f'Contact: {CONTACT_EMAIL}', 0, 1, 'C')
    pdf.ln(20)
    
    for i, (question, response) in enumerate(responses.items(), 1):
        title = f"{i}. {question}"
        body = f"Correct Answer: {response['answer']}"

        pdf.chapter_title(title.encode('latin1', 'replace').decode('latin1'))
        pdf.chapter_body(body.encode('latin1', 'replace').decode('latin1'))
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmpfile:
        pdf.output(tmpfile.name)
    return tmpfile.name

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

def initialize_state():
    if 'question_list' not in st.session_state or len(st.session_state.question_list) < NUM_QUESTIONS:
        if len(questions_and_answers) >= NUM_QUESTIONS:
            st.session_state.correct_answers = 0
            st.session_state.answered_questions = []
            st.session_state.current_question = 0
            st.session_state.incorrect_questions = []
            st.session_state.question_list = random.sample(list(questions_and_answers.items()), NUM_QUESTIONS)
        else:
            st.error(f"Not enough questions in the pool to sample {NUM_QUESTIONS} questions. Please add more questions.")

initialize_state()

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
                st.session_state.incorrect_questions.append((question, {"options": options[1:], "answer": correct_answer}))

            st.session_state.answered_questions.append((question, {"options": options[1:], "answer": correct_answer}))
            st.session_state.current_question += 1
            st.experimental_rerun()
        else:
            st.warning("You need to select an option to submit.")

if 'question_list' in st.session_state and st.session_state.current_question < len(st.session_state.question_list):
    question, q_data = st.session_state.question_list[st.session_state.current_question]
    create_question(question, q_data["options"], q_data["answer"])
else:
    st.write("### Quiz Completed!")
    
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

    if st.button("Download PDF with Explanations"):
        responses = {q[0]: questions_and_answers[q[0]] for q in st.session_state.answered_questions}
        pdf_file_path = generate_pdf(responses)

        with open(pdf_file_path, "rb") as pdf_file:
            st.download_button(
                label="Download PDF",
                data=pdf_file,
                file_name="ultrasound_explanations.pdf",
                mime='application/pdf'
            )

        os.remove(pdf_file_path)

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
