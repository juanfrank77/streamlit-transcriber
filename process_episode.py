import streamlit as st
import whisper

st.title("Podcast Transcriber")

st.sidebar.header("Transcription section")

audio_file = st.file_uploader("Upload audio", type=["wav", "mp3", "m4a"])

process_button = st.sidebar.button("Transcribe Episode")
st.sidebar.markdown("**Note**: Processing can take up to 5 mins, please be patient.")

model = whisper.load_model("base", device="cuda")
st.text("Whisper Model Loaded")

if process_button:
    if audio_file is not None:
        st.sidebar.info("Transcribing audio...")
        result = model.transcribe(audio_file.name)
        st.sidebar.success("Transcription Complete")
        
        st.markdown(episode_info['text'])
    else:
        st.sidebar.error("Please upload an episode.")
