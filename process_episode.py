import streamlit as st
from faster_whisper import WhisperModel

def main():
    st.title("Podcast Transcriber")
    
    st.sidebar.header("Transcription section")
    
    audio_file = st.file_uploader("Upload audio", type=["wav", "mp3", "m4a"])
    
    process_button = st.sidebar.button("Transcribe Episode")
    st.sidebar.markdown("**Note**: Processing can take up to 5 mins, please be patient.")
    
    if process_button:
        if audio_file is not None:
            st.sidebar.info("Transcribing audio...")
            st.text(audio_file.name)
            episode_info = transcribe_episode(audio_file)
            
            st.markdown(episode_info['text'])
        else:
            st.sidebar.error("Please upload an episode.")
            
def transcribe_episode(audio_file):
    
    model = WhisperModel("medium", device="cpu", compute_type="int8")
    st.text("Whisper Model Loaded")
    
    segments, _ = model.transcribe(audio_file)
    segments = list(segments)
    st.sidebar.success("Transcription Complete")
    
    return segments
    
if __name__ == '__main__':
    main()
