import base64
import io
import os

import google.generativeai as genai
import pdf2image
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_text, pdf_content, prompt):
    """
    Function to get a response from Gemini Generative AI API.
    """
    try:
        # Use the updated model name
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content([input_text, pdf_content[0], prompt])
        return response.text
    except Exception as e:
        return f"Error fetching response from Gemini API: {e}"

def input_pdf_setup(uploaded_file):
    """
    Convert uploaded PDF to images and extract the first page as base64-encoded content.
    """
    try:
        # Specify the path to Poppler's bin directory
        poppler_path = r"C:\\Program Files (x86)\\poppler\\Library\\bin"

        # Convert the PDF to images
        images = pdf2image.convert_from_bytes(uploaded_file.read(), poppler_path=poppler_path)

        first_page = images[0]

        # Convert image to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # Encode to base64
            }
        ]
        return pdf_parts
    except Exception as e:
        st.error(f"Error processing PDF: {e}")
        return None

# Streamlit App Configuration
st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking System")

# Input fields
input_text = st.text_area("Job Description: ", key="input")
uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"])

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

# Buttons for different functionalities
submit1 = st.button("Tell Me About the Resume")
submit3 = st.button("Percentage Match")

# Prompts for AI interaction
input_prompt1 = """
You are an experienced Technical Human Resource Manager. Your task is to review the provided resume against the job description. 
Please share your professional evaluation on whether the candidate's profile aligns with the role. Highlight the strengths 
and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt3 = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality. 
Your task is to evaluate the resume against the provided job description. Provide the percentage match of the resume with 
the job description. Include the percentage match first, followed by missing keywords and final thoughts.
"""

# Action for "Tell Me About the Resume"
if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        if pdf_content:
            response = get_gemini_response(input_text, pdf_content, input_prompt1)
            st.subheader("The Response is:")
            st.write(response)
        else:
            st.error("Failed to process the uploaded resume. Please try again.")
    else:
        st.warning("Please upload the resume.")

# Action for "Percentage Match"
if submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        if pdf_content:
            response = get_gemini_response(input_text, pdf_content, input_prompt3)
            st.subheader("The Response is:")
            st.write(response)
        else:
            st.error("Failed to process the uploaded resume. Please try again.")
    else:
        st.warning("Please upload the resume.")
