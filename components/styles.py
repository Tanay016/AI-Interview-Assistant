# UI Styles and CSS

CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

/* Global Font & App Container */
html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
}

.stApp {
    background: radial-gradient(circle at 15% 15%, rgba(30, 27, 75, 0.9) 0%, rgba(15, 23, 42, 0.98) 100%),
                linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #0f172a 100%);
    background-attachment: fixed;
    color: #f8fafc;
}

/* Sidebar styling */
[data-testid="stSidebar"] {
    background: rgba(15, 23, 42, 0.8) !important;
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border-right: 1px solid rgba(255, 255, 255, 0.08);
}

[data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
    color: #f1f5f9 !important;
    font-weight: 700;
}

/* Hero Section */
.hero-container {
    background: linear-gradient(135deg, rgba(30, 41, 59, 0.6) 0%, rgba(15, 23, 42, 0.8) 100%);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 20px;
    padding: 32px;
    margin-bottom: 24px;
    box-shadow: 0 12px 40px rgba(0, 0, 0, 0.3);
}

.hero-title {
    background: linear-gradient(135deg, #60a5fa 0%, #a78bfa 50%, #f472b6 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 2.6rem;
    font-weight: 800;
    letter-spacing: -0.02em;
    margin-bottom: 8px;
}

.hero-subtitle {
    color: #94a3b8;
    font-size: 1.05rem;
    font-weight: 400;
    margin-bottom: 18px;
}

/* Glass Card */
.glass-card {
    background: rgba(30, 41, 59, 0.5);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 16px;
    padding: 24px;
    margin-bottom: 20px;
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.25);
    transition: transform 0.2s ease, border-color 0.2s ease;
}

.glass-card:hover {
    border-color: rgba(99, 102, 241, 0.35);
}

/* Status Pills */
.status-pill {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 5px 12px;
    border-radius: 9999px;
    font-size: 0.8rem;
    font-weight: 600;
    margin-right: 6px;
    margin-bottom: 8px;
}

.pill-success {
    background: rgba(16, 185, 129, 0.15);
    color: #34d399;
    border: 1px solid rgba(52, 211, 153, 0.3);
}

.pill-warning {
    background: rgba(245, 158, 11, 0.15);
    color: #fbbf24;
    border: 1px solid rgba(251, 191, 36, 0.3);
}

.pill-purple {
    background: rgba(139, 92, 246, 0.15);
    color: #c084fc;
    border: 1px solid rgba(192, 132, 252, 0.3);
}

.pill-blue {
    background: rgba(59, 130, 246, 0.15);
    color: #60a5fa;
    border: 1px solid rgba(96, 165, 250, 0.3);
}

/* Feature Grid Cards */
.feature-card {
    background: rgba(15, 23, 42, 0.5);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 14px;
    padding: 20px;
    height: 100%;
    transition: transform 0.2s ease;
}

.feature-card:hover {
    transform: translateY(-3px);
    border-color: rgba(139, 92, 246, 0.3);
}

.feature-icon {
    font-size: 1.8rem;
    margin-bottom: 12px;
}

.feature-title {
    font-size: 1.05rem;
    font-weight: 700;
    color: #f1f5f9;
    margin-bottom: 6px;
}

.feature-desc {
    font-size: 0.88rem;
    color: #94a3b8;
    line-height: 1.4;
}

/* Buttons Styling */
.stButton > button {
    border-radius: 12px !important;
    font-weight: 600 !important;
    padding: 0.6rem 1.25rem !important;
    transition: all 0.25s ease !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    background: linear-gradient(135deg, rgba(99, 102, 241, 0.25) 0%, rgba(139, 92, 246, 0.25) 100%) !important;
    color: #f8fafc !important;
}

.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 20px rgba(99, 102, 241, 0.35) !important;
    background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%) !important;
    color: #ffffff !important;
    border-color: transparent !important;
}

div[data-testid="stButton"] button[kind="primary"] {
    background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%) !important;
    color: #ffffff !important;
    box-shadow: 0 4px 18px rgba(99, 102, 241, 0.45) !important;
    border: none !important;
}

div[data-testid="stButton"] button[kind="primary"]:hover {
    background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%) !important;
    box-shadow: 0 8px 28px rgba(99, 102, 241, 0.65) !important;
}

/* Chat Messages */
[data-testid="stChatMessage"] {
    background: rgba(30, 41, 59, 0.55) !important;
    backdrop-filter: blur(8px) !important;
    -webkit-backdrop-filter: blur(8px) !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    border-radius: 16px !important;
    padding: 18px 22px !important;
    margin-bottom: 14px !important;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2) !important;
}

[data-testid="stChatMessageAvatar"] {
    background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%) !important;
    border-radius: 12px !important;
}

/* Text Inputs & Selectboxes */
[data-testid="stTextInput"] input {
    background: rgba(15, 23, 42, 0.7) !important;
    border: 1px solid rgba(255, 255, 255, 0.15) !important;
    border-radius: 10px !important;
    color: #f8fafc !important;
    padding: 10px 14px !important;
}

[data-testid="stTextInput"] input:focus {
    border-color: #6366f1 !important;
    box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.3) !important;
}

div[data-baseweb="select"] > div {
    background: rgba(15, 23, 42, 0.7) !important;
    border: 1px solid rgba(255, 255, 255, 0.15) !important;
    border-radius: 10px !important;
    color: #f8fafc !important;
}

hr {
    border-color: rgba(255, 255, 255, 0.1) !important;
    margin: 1.5rem 0 !important;
}

/* Audio Player */
audio {
    width: 100%;
    border-radius: 12px;
    margin-top: 10px;
}
</style>
"""