import streamlit as st
import whisper

def main():
    st.title("Podcast Transcriber")
    
    st.sidebar.header("Transcription section")
    
    audio_file = st.file_uploader("Upload audio", type=["wav", "mp3", "m4a"])
    
    process_button = st.sidebar.button("Transcribe Episode")
    st.sidebar.markdown("**Note**: Processing can take up to 5 mins, please be patient.")
    
    if process_button:
        if audio_file is not None:
            st.text("Loading Whisper Model...")
            episode_info = transcribe_episode(audio_file)
            
            st.markdown(episode_info['text'])
        else:
            st.sidebar.error("Please upload an episode.")
            
def transcribe_episode(audio_file):
    st.text(audio_file)
    model = whisper.load_model("base")
    st.text("Whisper Model Loaded")

    audio = whisper.load_audio(audio_file.name)
    st.sidebar.info("Transcribing audio...")
    
    result = model.transcribe(audio)
    st.sidebar.success("Transcription Complete")

    return result
    
if __name__ == '__main__':
    main()
