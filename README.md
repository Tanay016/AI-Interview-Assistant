# 🎤 AI Interview Assistant

An intelligent interview practice application powered by Groq's Llama-3.3-70B model, featuring voice interaction and real-time feedback.

## ✨ Features

- 🎯 **Role-Tailored Interviews** - Practice for Technical, Behavioral, or HR interviews
- 🎙️ **Voice & Text Input** - Respond via voice recording or text
- 🔊 **Audio Playback** - Listen to AI responses with text-to-speech
- 💬 **Natural Conversation** - Dynamic follow-up questions based on your answers
- 📊 **Performance Feedback** - Get detailed assessment at the end
- 🎨 **Modern UI** - Beautiful glassmorphism design with smooth animations

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- A Groq API key ([Get one here](https://console.groq.com/))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ai-interview-assistant.git
   cd ai-interview-assistant
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and add your Groq API key:
   ```
   GROQ_API_KEY=your_actual_api_key_here
   ```

5. **Run the application**
   ```bash
   streamlit run streamlit_app.py
   ```

The app will open in your browser at `http://localhost:8501`

## 📁 Project Structure

```
BCT Project/
│
├── services/                    # External integrations
│   ├── ai_service.py           # Groq AI API integration
│   └── audio_service.py        # Voice input/output processing
│
├── utils/                      # Utility functions
│   └── session_manager.py     # Session state management
│
├── components/                 # UI components
│   └── styles.py              # CSS styling
│
├── app.py                     # Main application
├── config.py                  # Configuration
├── requirements.txt           # Dependencies
├── .env.example              # Environment template
└── .gitignore                # Git ignore rules
```

## 🎯 Usage

1. **Select Interview Type** - Choose from Technical, Behavioral, HR, or Custom
2. **Start Interview** - Click "Start Interview" to begin
3. **Respond** - Use voice recording or text input to answer questions
4. **Get Feedback** - Click "End Interview" for comprehensive feedback

## 🛠️ Technologies Used

- **Streamlit** - Web application framework
- **Groq API** - LLM (Llama-3.3-70B) for AI responses
- **gTTS** - Google Text-to-Speech
- **SpeechRecognition** - Voice input processing
- **audio-recorder-streamlit** - Voice recording component

## 🔐 Security

- API keys are stored in `.env` file (never committed to Git)
- `.gitignore` prevents sensitive files from being tracked
- Use `.env.example` as a template for required variables

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Code:016** (Tanay Ghosh),
**Swagatam Ghosh**,
**Subham Hazra**,
**Anku Mandal**

## 🙏 Acknowledgments

- Groq for providing the LLM API
- Streamlit for the amazing framework
- Google for Text-to-Speech services

---

Made with  by Code:016,Swagatam Ghosh,Subham Hazra, Anku Mandal
