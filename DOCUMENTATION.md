# 📚 Documentation - AI Interview Assistant

Complete technical and user documentation for the AI Interview Assistant application.

## 📖 Table of Contents

1. [Overview](#overview)
2. [Architecture](#architecture)
3. [Features](#features)
4. [User Guide](#user-guide)
5. [API Reference](#api-reference)
6. [Configuration](#configuration)
7. [Development](#development)
8. [Troubleshooting](#troubleshooting)

---

## 🎯 Overview

The AI Interview Assistant is a web-based application that simulates realistic interview scenarios using advanced AI. Built with Streamlit and powered by Groq's Llama-3.3-70B model, it provides an interactive platform for interview practice with voice and text capabilities.

### Key Technologies

- **Frontend:** Streamlit (Python web framework)
- **AI Engine:** Groq API (Llama-3.3-70B model)
- **Voice Input:** SpeechRecognition library
- **Voice Output:** Google Text-to-Speech (gTTS)
- **Audio Recording:** audio-recorder-streamlit component

### Use Cases

- Technical interview preparation
- Behavioral interview practice
- HR round rehearsal
- Custom role-specific interviews
- Communication skills development

---

## 🏗️ Architecture

### Project Structure

```
BCT Project/
│
├── streamlit_app.py           # Main application entry point
├── config.py                  # Configuration and environment setup
├── requirements.txt           # Python dependencies
├── .env                       # Environment variables (not in Git)
├── .env.example              # Environment template
├── .gitignore                # Git ignore rules
│
├── components/               # UI Components
│   ├── __init__.py
│   └── styles.py            # Custom CSS and styling
│
├── services/                # External Service Integrations
│   ├── __init__.py
│   ├── ai_service.py        # Groq API integration
│   └── audio_service.py     # Speech recognition & TTS
│
└── utils/                   # Utility Functions
    ├── __init__.py
    └── session_manager.py   # Session state management
```

### Data Flow

```
User Input (Voice/Text)
        ↓
Session State Management
        ↓
AI Service (Groq API)
        ↓
Response Generation
        ↓
Audio Service (TTS) ← Optional
        ↓
Display to User
```

### Module Breakdown

#### `streamlit_app.py` (Main Application)
- Page configuration and layout
- Session state initialization
- UI rendering
- User interaction handling
- Interview flow orchestration

#### `config.py` (Configuration)
- Environment variable loading
- API key validation
- Feature flags (e.g., SPEECH_AVAILABLE)

#### `components/styles.py` (Styling)
- Custom CSS with glassmorphism design
- Responsive layout styles
- Animation definitions
- Color scheme and theming

#### `services/ai_service.py` (AI Integration)
- Groq API client initialization
- Message formatting
- Response generation
- Error handling for API calls

#### `services/audio_service.py` (Audio Processing)
- Speech-to-text conversion
- Text-to-speech generation
- Audio file handling
- Microphone input processing

#### `utils/session_manager.py` (State Management)
- Session state initialization
- Conversation history management
- Audio state tracking
- Interview status flags

---

## ✨ Features

### 1. Role-Tailored Interviews

**Description:** Dynamic question generation based on selected interview domain.

**Available Domains:**
- **Technical:** System design, algorithms, coding problems
- **Behavioral:** STAR method questions, past experiences
- **HR Round:** Company fit, career goals, soft skills
- **Custom:** User-defined job roles

**Implementation:**
- System prompts tailored per domain
- Context-aware follow-up questions
- Progressive difficulty adjustment

### 2. Dual Input Modes

#### Voice Input
- **Technology:** SpeechRecognition with Google Speech API
- **Features:**
  - Real-time audio recording
  - Automatic transcription
  - Visual recording indicator
  - Processing state feedback

#### Text Input
- **Features:**
  - Standard text field
  - Instant submission
  - Full keyboard support

### 3. Audio Playback

**Description:** Listen to AI interviewer responses with text-to-speech.

**Features:**
- Click-to-play buttons for each response
- Google TTS voice synthesis
- MP3 audio format
- In-browser playback

### 4. Conversational AI

**Powered by:** Groq Llama-3.3-70B

**Capabilities:**
- Natural language understanding
- Context-aware responses
- Follow-up question generation
- Adaptive difficulty
- Constructive feedback

### 5. Performance Feedback

**End-of-Interview Analysis:**
- Overall performance assessment
- Strength identification
- Improvement areas
- Specific examples from responses
- Actionable recommendations

### 6. Modern UI/UX

**Design Elements:**
- Glassmorphism aesthetic
- Smooth animations
- Responsive layout
- Status indicators
- Clear visual hierarchy

---

## 📘 User Guide

### Getting Started

1. **Launch the Application**
   ```bash
   streamlit run streamlit_app.py
   ```

2. **Select Interview Domain**
   - Use the sidebar dropdown
   - Choose from preset types or enter custom role

3. **Start Interview**
   - Click "🚀 Start Interview" button
   - AI introduces itself and asks first question

### During the Interview

#### Responding with Voice

1. Click the microphone button
2. Speak your answer clearly
3. Click stop when finished
4. Wait for transcription
5. AI processes and responds

**Tips:**
- Speak in a quiet environment
- Enunciate clearly
- Keep responses focused

#### Responding with Text

1. Type your answer in the text field
2. Click "📝 Submit Text Answer"
3. AI processes and responds

**Tips:**
- Structure your thoughts before typing
- Use proper grammar
- Be concise but thorough

### Listening to Responses

- Click "🔊 Play Response" button next to any AI message
- Audio generates and plays automatically
- Useful for practicing listening comprehension

### Ending the Interview

1. Click "🏁 End Interview & Get Feedback"
2. AI analyzes entire conversation
3. Comprehensive feedback displayed
4. Option to start new session

### Resetting the Session

- Click "🔄 Reset Session" in sidebar
- Clears all conversation history
- Returns to home screen
- Useful for starting fresh

---

## 🔌 API Reference

### AI Service Functions

#### `get_ai_response(messages: list) -> str`

Generates AI response using Groq API.

**Parameters:**
- `messages` (list): Conversation history in OpenAI format

**Returns:**
- `str`: AI-generated response text

**Example:**
```python
messages = [
    {"role": "user", "content": "What is your approach to system design?"}
]
response = get_ai_response(messages)
```

### Audio Service Functions

#### `speech_to_text(audio_bytes: bytes) -> str`

Converts audio recording to text.

**Parameters:**
- `audio_bytes` (bytes): Raw audio data

**Returns:**
- `str`: Transcribed text or None if failed

**Example:**
```python
text = speech_to_text(audio_data)
if text:
    print(f"User said: {text}")
```

#### `text_to_speech(text: str) -> str`

Converts text to audio file.

**Parameters:**
- `text` (str): Text to synthesize

**Returns:**
- `str`: Path to generated MP3 file

**Example:**
```python
audio_path = text_to_speech("Hello, welcome to your interview.")
st.audio(audio_path)
```

### Session Management Functions

#### `initialize_session_state()`

Initializes Streamlit session state variables.

**Session State Variables:**
- `messages` (list): Conversation history
- `interview_started` (bool): Interview active status
- `processing_audio` (bool): Audio processing flag
- `last_audio` (bytes): Last recorded audio

**Example:**
```python
initialize_session_state()
if st.session_state.interview_started:
    # Show interview UI
```

---

## ⚙️ Configuration

### Environment Variables

**`.env` File:**
```env
GROQ_API_KEY=gsk_your_actual_api_key_here
```

### Configuration Options

**`config.py`:**
```python
GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # Required
SPEECH_AVAILABLE = True                    # Enable/disable voice
```

### Streamlit Configuration (Optional)

Create `.streamlit/config.toml`:

```toml
[theme]
primaryColor = "#6366f1"
backgroundColor = "#0f172a"
secondaryBackgroundColor = "#1e293b"
textColor = "#f1f5f9"

[server]
port = 8501
headless = false
```

### Model Configuration

Change AI model in `services/ai_service.py`:

```python
model = "llama-3.3-70b-versatile"  # Default
# Alternatives: llama-3.1-8b-instant, mixtral-8x7b-32768
```

---

## 💻 Development

### Setting Up Development Environment

1. Clone repository
2. Create virtual environment
3. Install dependencies
4. Create `.env` file
5. Run in development mode

### Adding New Features

#### Adding a New Interview Type

1. Update `streamlit_app.py`:
   ```python
   interview_type = st.selectbox(
       "Select Interview Domain",
       ["Technical", "Behavioral", "HR Round", "Product Manager", "Custom"]
   )
   ```

2. Customize system prompt for new type

#### Customizing AI Behavior

Edit system prompt in `streamlit_app.py`:

```python
system_prompt = f"""You are an experienced {custom_role} interviewer.

Your role:
- Custom instruction 1
- Custom instruction 2
...
"""
```

#### Styling Modifications

Edit `components/styles.py` to customize:
- Colors and gradients
- Animations
- Layout spacing
- Component styles

### Testing

**Manual Testing Checklist:**
- [ ] Voice recording works
- [ ] Text input works
- [ ] Audio playback works
- [ ] Session reset works
- [ ] Feedback generation works
- [ ] UI responsive on mobile
- [ ] Error handling displays properly

### Code Style

Follow PEP 8 guidelines:
```bash
pip install black flake8
black .
flake8 .
```

---

## 🐛 Troubleshooting

### Common Issues

#### Issue: API Rate Limiting

**Symptoms:** Slow responses or errors

**Solutions:**
- Wait a few seconds between requests
- Check Groq dashboard for rate limits
- Consider upgrading API plan

#### Issue: Audio Not Recording

**Symptoms:** Microphone button not working

**Solutions:**
- Check browser microphone permissions
- Use Chrome/Edge (best audio support)
- Test microphone in other apps

#### Issue: Poor Transcription Quality

**Symptoms:** Incorrect text from voice

**Solutions:**
- Speak clearly and slowly
- Use in quiet environment
- Check microphone quality
- Use text input as alternative

#### Issue: Session State Lost

**Symptoms:** Conversation disappears

**Solutions:**
- Avoid browser refresh (use app controls)
- Check browser console for errors
- Restart application if persistent

### Error Messages

#### "GROQ_API_KEY not found"

**Cause:** Missing or invalid API key

**Fix:**
1. Create `.env` file
2. Add valid API key
3. Restart application

#### "Module not found"

**Cause:** Missing dependencies

**Fix:**
```bash
pip install -r requirements.txt
```

#### "Address already in use"

**Cause:** Port 8501 occupied

**Fix:**
```bash
streamlit run streamlit_app.py --server.port 8502
```

### Debug Mode

Enable Streamlit debug mode:

```bash
streamlit run streamlit_app.py --logger.level=debug
```

### Logging

Add logging to track issues:

```python
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Processing user input")
```

---

## 📊 Performance Optimization

### Tips for Better Performance

1. **API Calls:** Minimize unnecessary requests
2. **Audio Processing:** Use efficient codecs
3. **Session State:** Clear old messages periodically
4. **Caching:** Enable Streamlit caching where appropriate

### Resource Usage

**Typical Resource Consumption:**
- RAM: ~200-300 MB
- CPU: Low (spikes during audio processing)
- Network: Minimal (API calls only)

---

## 🔒 Security Best Practices

1. **Never commit `.env` file**
2. **Regenerate exposed API keys immediately**
3. **Use HTTPS in production**
4. **Validate user inputs**
5. **Keep dependencies updated**

---

## 📈 Future Enhancements

**Potential Features:**
- Multi-language support
- Interview recording/replay
- Progress tracking over time
- Custom question banks
- Interview scheduling
- Performance analytics dashboard

---

## 📞 Support

For issues or questions:
- Review this documentation
- Check troubleshooting section
- Refer to `SETUP.md` for installation issues

---

**Documentation Version:** 1.0  
**Last Updated:** August 6, 2026  
**Author:** Code:016 (Tanay Ghosh)