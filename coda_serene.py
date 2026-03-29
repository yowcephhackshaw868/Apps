import streamlit as st
from datetime import datetime

# --- 1. SETTING THE MOOD & CUSTOM THEME ---
st.set_page_config(page_title="Coda", layout="wide")

# Applying your custom palette: Green, Pink, Silver, and Black
st.markdown("""
    <style>
    /* 1. Deep Black/Silver background for high contrast */
    .stApp { 
        background-color: #0d1117 !important; 
    }
    
    /* 2. Silver & Soft Pink headers and text */
    h1, h2, h3, h4, span, label { 
        color: #e2e8f0 !important; /* Silver */
    }
    p {
        color: #fce7f3 !important; /* Soft Pink */
    }
    
    /* 3. Input boxes (White with black text for readability) */
    .stTextArea textarea, .stTextInput input, .stSelectbox div[data-baseweb="select"] { 
        background-color: #ffffff !important; 
        color: #000000 !important; 
        border-radius: 12px;
        border: 2px solid #ec4899 !important; /* Pink Border */
    }
    
    /* 4. The Action Button (Vibrant Green with Black Text) */
    .stButton button { 
        background-color: #10b981 !important; /* Green */
        color: #000000 !important; /* Black details */
        border-radius: 12px; 
        font-weight: bold;
        height: 3.5em;
        width: 100%;
        border: 2px solid #e2e8f0 !important; /* Silver Border */
    }
    .stButton button:hover { 
        background-color: #059669 !important; 
        color: #ffffff !important;
    }
    
    /* 5. Custom result cards using the palette */
    .custom-card {
        padding: 30px;
        border-radius: 16px;
        margin-top: 20px;
        border: 2px solid #ec4899; /* Pink */
        background-color: #1f2937; /* Dark Silver/Gray */
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. THE FLESHED-OUT LOGIC ---
def get_detailed_guidance(stress, domain, persona, focus, problem):
    # Determine the core energy based on stress
    try:
        stress = int(stress)
    except:
        stress = 5
        
    # Generate long-form, multi-step advice tailored to your inputs
    if stress >= 8:
        bg_color = "#4c0519" # Deep dark pink/red for heavy situations
        header = "🛑 Emergency De-escalation Path"
        strategy = "When things are this heavy, your only goal is to stop the bleeding and find solid ground. Do not attempt to solve the whole problem today."
        steps = [
            "**Step 1 (First 60 Seconds):** Put down whatever you are holding. Take three slow breaths. Feel your feet on the floor. Right now, you are safe.",
            "**Step 2 (The Next Hour):** Identify the single most urgent thread of this problem. Ignore the rest. What is the one thing that will cause a collapse if not handled? Do only that.",
