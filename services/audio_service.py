# Audio Services - Voice Input and Output

import streamlit as st
from gtts import gTTS
import os
import tempfile
import speech_recognition as sr
import io


def text_to_speech(text):
    """Convert text to speech audio"""
    try:
        # Use gTTS with optimized settings for faster, better quality
        tts = gTTS(text=text, lang='en', slow=False, tld='com')

        # Save to bytes buffer instead of file for faster processing
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)

        return fp
    except Exception as e:
        st.error(f"Text-to-speech error: {e}")
        return None


def speech_to_text(audio_bytes):
    """Convert speech audio to text"""
    if not audio_bytes:
        return None

    recognizer = sr.Recognizer()
    audio_file = None
    try:
        # Save audio bytes directly to WAV file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as fp:
            fp.write(audio_bytes)
            audio_file = fp.name

        # Convert to AudioFile for recognition
        with sr.AudioFile(audio_file) as source:
            # Adjust for ambient noise for better accuracy
            recognizer.adjust_for_ambient_noise(source, duration=0.2)
            audio_data = recognizer.record(source)

            # Use Google's speech recognition
            text = recognizer.recognize_google(audio_data, language='en-US')
            return text
    except sr.UnknownValueError:
        st.error("Could not understand audio. Please speak clearly and try again.")
        return None
    except Exception as e:
        st.error(f"Speech recognition error: {e}")
        return None
    finally:
        # Ensure file is deleted after recognition completes
        if audio_file and os.path.exists(audio_file):
            try:
                os.unlink(audio_file)
            except:
                pass  # Ignore deletion errors