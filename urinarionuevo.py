import random
import streamlit as st
from fpdf import FPDF
import requests

# Encabezado con Logo y Links
LOGO_URL = "https://storage.googleapis.com/allostericsolutionsr/Allosteric_Solutions.png"
WEBSITE_URL = "https://www.allostericsolutions.com"
CONTACT_EMAIL = "franciscocuriel@allostericsolutions.com"

# Generate PDF
def generate_pdf(responses, logo_data):  # Pass image data
    pdf = FPDF()
    pdf.add_page()
    # Use UTF-8 encoding for the font (check fpdf documentation for details)
    pdf.set_font("Arial", size=12, encoding='utf-8') 

    # Add logo
    pdf.image(logo_data, x=10, y=8, w=25)  # Use image data here

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
    # ... (Your questions and answers data)
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
else:
    if len(st.session_state.question_list) < NUM_QUESTIONS and not st.session_state.incorrect_questions:
        # Solo resetear si no están tratando de reintentar las incorrectas
        initialize_state()

# Create Question function
def create_question(question, options, correct_answer):
    # ... (Your question display code)

# Display the current question
if st.session_state.current_question < len(st.session_state.question_list):
    question, q_data = st.session_state.question_list[st.session_state.current_question]
    create_question(question, q_data["options"], q_data["answer"])
else:
    # ... (Your quiz completion code)

    # Function to download the PDF with answers and explanations
    if st.button("Download PDF with Explanations"):
        responses = {q[0]: questions_and_answers[q[0]] for q in st.session_state.answered_questions}

        # Download logo image
        response = requests.get(LOGO_URL)
        logo_data = response.content

        pdf = generate_pdf(responses, logo_data)  # Pass image data
        pdf_output = pdf.output(dest='S').encode('utf-8') 
        st.download_button(label="Download PDF",
                           data=pdf_output,
                           file_name="ultrasound_explanations.pdf",
                           mime='application/pdf')

    # ... (Your retry and new quiz buttons)
