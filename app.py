import streamlit as st
from dotenv import load_dotenv
import os
import openai  # Correct import for OpenAI
load_dotenv()
#Hi
# Set your OpenAI API key securely
openai.api_key = os.getenv('OPENAI_API_KEY')

def interview(text):
    # Properly format the prompt
    prompt = f"Take the Interview: {text}"
    
    # Call OpenAI's API correctly
    completion = openai.Completion.create(
        model='text-davinci-003',  # or 'gpt-3.5-turbo'
        prompt=prompt,
        max_tokens=150
    )
    return completion.choices[0].text.strip()

# Streamlit UI
st.title("AI Interviewer Chatbot")

# User input
input_text = st.text_area('Enter your text')

# Button to start the interview process
if st.button('Start'):
    if input_text:
        interview_bot = interview(input_text)
        st.write('Interview Chatbot Response:')
        st.write(interview_bot)
    else:
        st.warning('Empty text input. Please enter some text.')
