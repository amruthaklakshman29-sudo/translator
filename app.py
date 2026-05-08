import streamlit as st
from audio_recorder_streamlit import audio_recorder
from deep_translator import GoogleTranslator
from gtts import gTTS
import speech_recognition as sr
from io import BytesIO

# Get a list of supported languages for the dropdown
langs_dict = GoogleTranslator().get_supported_languages(as_dict=True)

def main():
    st.image("image-asset.png")
    st.title(" PragyanAI - VVIET Workshop: Audio Hub")
