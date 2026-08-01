# Session State Management

import streamlit as st


def initialize_session_state():
    """Initialize session state variables"""
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'interview_started' not in st.session_state:
        st.session_state.interview_started = False
    if 'last_audio' not in st.session_state:
        st.session_state.last_audio = None
    if 'processing_audio' not in st.session_state:
        st.session_state.processing_audio = False