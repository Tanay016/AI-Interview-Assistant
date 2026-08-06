# 🛠️ Setup Guide - AI Interview Assistant

This guide will walk you through setting up the AI Interview Assistant on your local machine.

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8 or higher** - [Download Python](https://www.python.org/downloads/)
- **pip** (comes with Python)
- **Git** (optional, for cloning) - [Download Git](https://git-scm.com/downloads)
- **Groq API Key** - [Get your free API key](https://console.groq.com/)

### Check Python Installation

```bash
python --version
# or
python3 --version
```

You should see Python 3.8 or higher.

## 🚀 Installation Steps

### Step 1: Get the Project

**Option A: Clone the repository (if using Git)**
```bash
git clone https://github.com/yourusername/ai-interview-assistant.git
cd ai-interview-assistant
```

**Option B: Download the ZIP**
- Download and extract the project folder
- Navigate to the project directory in your terminal

### Step 2: Create a Virtual Environment

Creating a virtual environment keeps your project dependencies isolated.

**On Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

You should see `(.venv)` prefix in your terminal prompt after activation.

### Step 3: Install Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

This will install:
- `streamlit` - Web framework
- `groq` - AI API client
- `SpeechRecognition` - Voice input processing
- `gTTS` - Text-to-speech
- `audio-recorder-streamlit` - Voice recording component
- `python-dotenv` - Environment variable management

### Step 4: Configure Environment Variables

1. **Copy the example environment file:**
   ```bash
   cp .env.example .env
   ```
   
   On Windows (if `cp` doesn't work):
   ```bash
   copy .env.example .env
   ```

2. **Get your Groq API key:**
   - Visit [Groq Console](https://console.groq.com/)
   - Sign up or log in
   - Navigate to API Keys section
   - Create a new API key
   - Copy the key

3. **Edit the `.env` file:**
   Open `.env` in a text editor and add your API key:
   ```
   GROQ_API_KEY=gsk_your_actual_api_key_here
   ```
   
   **Important:** Never share or commit this file to version control!

### Step 5: Verify Installation

Check that all modules are properly installed:

```bash
python -c "import streamlit, groq, speech_recognition, gtts; print('All dependencies installed successfully!')"
```

### Step 6: Run the Application

Start the Streamlit server:

```bash
streamlit run streamlit_app.py
```

The application should automatically open in your default browser at:
```
http://localhost:8501
```

If it doesn't open automatically, manually navigate to that URL.

## 🎤 Audio Setup (Optional)

For voice input/output features to work properly:

### Windows
- Ensure your microphone is connected and enabled
- Check Privacy Settings → Microphone → Allow apps to access microphone

### macOS
- System Preferences → Security & Privacy → Privacy → Microphone
- Grant permission to Terminal or your Python application

### Linux
```bash
sudo apt-get install portaudio19-dev python3-pyaudio
```

## 🔧 Troubleshooting

### Issue: Module Not Found Error

**Solution:**
```bash
pip install --upgrade -r requirements.txt
```

### Issue: API Key Not Found

**Error:** `GROQ_API_KEY not found in environment variables`

**Solution:**
1. Verify `.env` file exists in project root
2. Check the API key is properly formatted (no extra spaces)
3. Restart the application after updating `.env`

### Issue: Audio Recording Not Working

**Solution:**
- Check microphone permissions
- Install additional audio dependencies:
  ```bash
  pip install pyaudio
  ```
- On Linux, install PortAudio:
  ```bash
  sudo apt-get install portaudio19-dev
  ```

### Issue: Port Already in Use

**Error:** `Address already in use`

**Solution:**
```bash
# Kill existing Streamlit process
# On Windows:
taskkill /F /IM streamlit.exe

# On macOS/Linux:
pkill -f streamlit

# Or run on a different port:
streamlit run streamlit_app.py --server.port 8502
```

### Issue: Import Error from Custom Modules

**Error:** `ModuleNotFoundError: No module named 'services'`

**Solution:**
Ensure you're running the command from the project root directory:
```bash
cd /path/to/BCT\ Project
streamlit run streamlit_app.py
```

## 🔄 Updating the Application

To update to the latest version:

```bash
# Pull latest changes (if using Git)
git pull origin main

# Update dependencies
pip install --upgrade -r requirements.txt

# Restart the application
streamlit run streamlit_app.py
```

## 🛑 Stopping the Application

To stop the Streamlit server:
- Press `Ctrl + C` in the terminal where the app is running

To deactivate the virtual environment:
```bash
deactivate
```

## 🌐 Network Access (Optional)

To allow others on your network to access the app:

```bash
streamlit run streamlit_app.py --server.address 0.0.0.0
```

Find your local IP address and share: `http://YOUR_IP:8501`

## 📱 Browser Compatibility

The application works best on:
- ✅ Chrome/Edge (Recommended)
- ✅ Firefox
- ✅ Safari
- ⚠️ Mobile browsers (limited audio support)

## 🔐 Security Notes

- Never commit `.env` file to version control
- Keep your API key private
- The `.gitignore` file is configured to exclude sensitive files
- Regenerate your API key if accidentally exposed

## 📞 Getting Help

If you encounter issues:
1. Check the troubleshooting section above
2. Review error messages in the terminal
3. Ensure all prerequisites are met
4. Verify your API key is valid and has credits

## ✅ Next Steps

Once setup is complete:
1. Read `DOCUMENTATION.md` for feature details
2. Explore the interview types available
3. Practice with voice and text inputs
4. Review the feedback system

---

**Setup complete! Happy interviewing! 🎉**