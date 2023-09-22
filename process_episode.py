import streamlit as st

def main():
    st.title("Podcast Transcriber")
    
    st.sidebar.header("Transcription section")
    
    audio_file = st.file_uploader("Upload audio", type=["wav", "mp3", "m4a"])
    
    process_button = st.sidebar.button("Transcribe Episode")
    st.sidebar.markdown("**Note**: Processing can take up to 5 mins, please be patient.")
    
    if process_button:
        if audio_file is not None:
            st.sidebar.info("Transcribing audio...")
            
            episode_info = transcribe_episode(audio_file)
            
            st.markdown(episode_info['text'])
        else:
            st.sidebar.error("Please upload an episode.")
            
def transcribe_episode(episode):
    # Load the Whisper model
    import whisper
    
    model = whisper.load_model("base")
    st.text("Whisper Model Loaded")
    
    result = model.transcribe(audio_file.name)
    st.sidebar.success("Transcription Complete")
    
    return result
    
if __name__ == '__main__':
    main()
