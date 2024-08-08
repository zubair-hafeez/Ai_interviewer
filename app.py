import streamlit as st
from dotenv import load_dotenv
import os
import openai

# Load environment variables from a .env file
load_dotenv()

# Set your OpenAI API key securely
openai.api_key = os.getenv('OPENAI_API_KEY')

def interview(text):
    # Format the prompt correctly
    prompt = f"Conduct a mock interview based on this input: {text}"
    
    # Call OpenAI's API correctly
    try:
        completion = openai.Completion.create(
            model='text-davinci-003',  # For more conversational tasks, consider using 'gpt-3.5-turbo'
            prompt=prompt,
            max_tokens=150,
            temperature=0.7,  # Add temperature for more creative responses
            n=1,              # Number of responses
            stop=None         # Ensure no premature stopping
        )
        return completion.choices[0].text.strip()
    except openai.error.OpenAIError as e:
        return f"An error occurred: {e}"

# Streamlit UI
st.title("AI Interviewer Chatbot")

# User input
input_text = st.text_area('Enter your text for the interview prompt:', height=150)

# Button to start the interview process
if st.button('Start'):
    if input_text.strip():  # Check for non-empty input
        interview_bot = interview(input_text)
        st.subheader('Interview Chatbot Response:')
        st.write(interview_bot)
    else:
        st.warning('Empty text input. Please enter some text to proceed.')
