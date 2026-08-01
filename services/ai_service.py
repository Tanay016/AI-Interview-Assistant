# AI Service - Groq API Integration

import streamlit as st
from groq import Groq
from config import GROQ_API_KEY


def get_ai_response(messages):
    """Get AI response from Groq API"""
    try:
        client = Groq(api_key=GROQ_API_KEY)

        # Convert messages to Groq format
        groq_messages = []
        for msg in messages:
            groq_messages.append({
                "role": msg["role"],
                "content": msg["content"]
            })

        if len(groq_messages) == 0:
            return ""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=groq_messages
        )

        return response.choices[0].message.content
    except Exception as e:
        st.error(f"Error getting AI response: {e}")
        return None