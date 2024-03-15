import streamlit as st
from dotenv import load_dotenv 
load_dotenv()    #load all the environment variables

import google.generativeai as genai
import os



genai.configure(api_key = os.getenv('GOOGLE_API_KEY'))


prompt = '''You are a youtube video summarizer. You will be taking the transcript text
        of a youtube video and generate a summary of the entire video. providing the important key points within 
        around 260 words limit . The transcript text will be appended here :  '''

def generate_gemini_content(transcript_text,prompt):
    model = genai.GenerativeModel("gemini-pro")

    response = model.generate_content(prompt+transcript_text)
    return response.text


