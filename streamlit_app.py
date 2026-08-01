import streamlit as st
import os
from audio_recorder_streamlit import audio_recorder

# Import custom modules
from config import SPEECH_AVAILABLE
from components import CUSTOM_CSS
from services import get_ai_response, text_to_speech, speech_to_text
from utils import initialize_session_state

# Page configuration
st.set_page_config(
    page_title="AI Interview Assistant",
    page_icon="🎤",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom CSS
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Initialize session state
initialize_session_state()

# Top Hero Header
st.markdown("""
<div class="hero-container">
    <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 16px;">
        <div>
            <div class="hero-title">🎤 AI Interview Assistant</div>
            <div class="hero-subtitle">Elevate your interviewing skills with real-time AI conversation, voice feedback & comprehensive analytics.</div>
        </div>
    </div>
    <div>
        <span class="status-pill pill-purple">⚡ Groq Llama-3.3-70B</span>
        <span class="status-pill pill-blue">🎙️ Voice & Text Interactive</span>
        <span class="status-pill pill-success">📊 Smart Feedback Engine</span>
    </div>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### ⚙️ Interview Controls")

    if SPEECH_AVAILABLE:
        st.markdown('<span class="status-pill pill-success">🟢 Voice Engine Ready</span>', unsafe_allow_html=True)
    else:
        st.markdown('<span class="status-pill pill-warning">⚠️ Voice Unavailable (Text Only)</span>', unsafe_allow_html=True)

    st.markdown("---")
    interview_type = st.selectbox(
        "Select Interview Domain",
        ["Technical", "Behavioral", "HR Round", "Custom"]
    )

    if interview_type == "Custom":
        custom_role = st.text_input("Specify Job Role", "Software Engineer")
    else:
        custom_role = interview_type

    st.markdown("---")
    if st.button("🔄 Reset Session", use_container_width=True):
        st.session_state.messages = []
        st.session_state.interview_started = False
        st.rerun()

if not st.session_state.interview_started:
    # Feature showcase grid
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🎯</div>
            <div class="feature-title">Role-Tailored Probing</div>
            <div class="feature-desc">Dynamic questions generated specifically for your target domain, from system design to STAR behavioral prompts.</div>
        </div>
        """, unsafe_allow_html=True)
    with col_b:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🎙️</div>
            <div class="feature-title">Dual Voice & Text Input</div>
            <div class="feature-desc">Practice natural spoken articulation or type detailed responses to build confidence under real conditions.</div>
        </div>
        """, unsafe_allow_html=True)
    with col_c:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📈</div>
            <div class="feature-title">Detailed Performance Feedback</div>
            <div class="feature-desc">Receive instant structural feedback, identifying key strengths, clarity gaps, and actionable tips for improvement.</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(f"""
    <div class="glass-card" style="text-align: center;">
        <h3 style="margin-top: 0; color: #f1f5f9;">Ready to start your practice session?</h3>
        <p style="color: #94a3b8;">Target Domain: <strong style="color: #60a5fa;">{custom_role}</strong></p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🚀 Start Interview", type="primary", use_container_width=True):
        st.session_state.interview_started = True
        system_prompt = f"""You are an experienced interviewer conducting a {custom_role} interview.

Your role:
- Ask one relevant question at a time
- Listen carefully to the candidate's answers
- Ask follow-up questions based on their responses to dive deeper
- Probe for details, examples, and understanding
- Challenge assumptions when appropriate
- Provide constructive feedback occasionally
- Keep the conversation natural and engaging

Start by introducing yourself briefly and asking the first question."""

        st.session_state.messages = [
            {"role": "user", "content": system_prompt}
        ]

        response = get_ai_response(st.session_state.messages)
        if response:
            st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()
else:
    # Active interview header badge
    st.markdown(f"""
    <div style="display: flex; justify-content: space-between; align-items: center; background: rgba(30, 41, 59, 0.4); padding: 12px 20px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.08); margin-bottom: 20px;">
        <div><strong style="color: #94a3b8;">Active Session:</strong> <span style="color: #60a5fa; font-weight: 700;">{custom_role}</span></div>
        <div><span class="status-pill pill-success">Live Interview</span></div>
    </div>
    """, unsafe_allow_html=True)

    for idx, message in enumerate(st.session_state.messages[1:]):
        if message["role"] == "assistant":
            with st.chat_message("assistant", avatar="👔"):
                st.markdown(message["content"])
                # Add audio playback button for assistant responses
                if st.button(f"🔊 Play Response", key=f"play_{idx}", help="Listen to this response"):
                    with st.spinner("Generating audio..."):
                        audio_fp = text_to_speech(message["content"])
                        if audio_fp:
                            st.audio(audio_fp, format='audio/mp3')
        else:
            with st.chat_message("user", avatar="👤"):
                st.markdown(message["content"])

    st.markdown("<br>", unsafe_allow_html=True)

    # Response Input Card Container
    st.markdown('<div class="glass-card"><h4 style="margin-top:0; margin-bottom: 16px; color: #f1f5f9;">💬 Provide Your Response</h4>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("**🎤 Voice Input**")
        audio_bytes = audio_recorder(
            text="Click to record",
            recording_color="#e74c3c",
            neutral_color="#6366f1",
            icon_name="microphone",
            icon_size="2x",
        )

        # Only process if we have new audio and it's different from the last one
        if audio_bytes and audio_bytes != st.session_state.last_audio and not st.session_state.processing_audio:
            st.session_state.processing_audio = True
            st.session_state.last_audio = audio_bytes

            with st.spinner("🎤 Transcribing your voice..."):
                user_input = speech_to_text(audio_bytes)
                if user_input:
                    st.session_state.messages.append({"role": "user", "content": user_input})

                    with st.spinner("🤔 AI is thinking..."):
                        response = get_ai_response(st.session_state.messages[1:])
                        if response:
                            st.session_state.messages.append({"role": "assistant", "content": response})

            st.session_state.processing_audio = False
            st.rerun()

    with col2:
        text_input = st.text_input("Or type your answer:", key="text_answer", label_visibility="collapsed", placeholder="Type your response here...")
        if st.button("📝 Submit Text Answer", use_container_width=True) and text_input:
            st.session_state.messages.append({"role": "user", "content": text_input})

            response = get_ai_response(st.session_state.messages[1:])
            st.session_state.messages.append({"role": "assistant", "content": response})

            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")
    if st.button("🏁 End Interview & Get Feedback", use_container_width=True):
        feedback_prompt = "Please provide detailed feedback on the candidate's performance throughout this interview. Include strengths, areas for improvement, and an overall assessment."
        st.session_state.messages.append({"role": "user", "content": feedback_prompt})

        feedback = get_ai_response(st.session_state.messages[1:])

        st.markdown("""
        <div class="glass-card" style="border-left: 4px solid #6366f1;">
            <h3 style="margin-top:0; color: #60a5fa;">📊 Comprehensive Interview Feedback</h3>
        </div>
        """, unsafe_allow_html=True)
        st.markdown(feedback)

        if st.button("🔄 Start New Practice Session", use_container_width=True):
            st.session_state.messages = []
            st.session_state.interview_started = False
            st.rerun()
