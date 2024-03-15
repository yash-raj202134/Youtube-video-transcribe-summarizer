import streamlit as st
from dotenv import load_dotenv 
load_dotenv()    #load all the environment variables

from youtube_transcript_api import YouTubeTranscriptApi
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


def extract_transcript_details(youtube_video_URL):
    try:
        video_id = youtube_video_URL.split("=")[1]
        print(video_id)
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = ""

        for i in transcript_text:
            transcript += " " + i["text"]
        
        return transcript


    except Exception as e:
        raise e



# Application

st.title("YouTube Transcript to Detailed Notes Converter")
youtube_link = st.text_input("Enter YouTube Video Link:")


if youtube_link:
    video_id = youtube_link.split("=")[1]
    print(video_id)
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg",use_column_width=True)

if st.button("Get Detailed Notes"):
    transcript_text=extract_transcript_details(youtube_link)

    if transcript_text:
        summary=generate_gemini_content(transcript_text,prompt)
        st.markdown("## Detailed Notes:")
        st.write(summary)