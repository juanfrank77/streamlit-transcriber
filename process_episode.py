import streamlit as st
from openai_whisper import Transcriber

st.title("Podcast Transcriber")

st.sidebar.header("Transcription section")

audio_file = st.file_uploader("Upload audio", type=["wav", "mp3", "m4a"])

process_button = st.sidebar.button("Transcribe Episode")
st.sidebar.markdown("**Note**: Processing can take up to 5 mins, please be patient.")

# model = whisper.load_model("base")
st.text("Whisper Model Loaded")

if process_button:
    if audio_file is not None:
        st.sidebar.info("Transcribing audio...")
        audio_data = audio_file.read()
        audio = whisper.load_audio("audio.mp3")
        audio = whisper.pad_or_trim(audio)
        transcriber = Transcriber()
        # result = model.transcribe("NW-S4-Demo-Video.mp3")
        result = transcriber.transcribe(audio)
        
        st.sidebar.success("Transcription Complete")
        
        st.markdown(result['text'])
    else:
        st.sidebar.error("Please upload an episode.")
