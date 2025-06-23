import streamlit as st 
import speech_recognition as sr 

st.title('Speech to Text Converter')

recog = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    st.write('Please Speak...')
    audio = recog.listen(source)

    try:
        text = recog.recognize_google(audio)
        st.write(f'You said: {text}')

    except:
        st.write('Sorry,I could not understand the audio')
    finally:
        st.write('Processing Complete')