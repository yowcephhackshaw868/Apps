import streamlit as st
from datetime import datetime

# --- 1. SETTING THE MOOD ---
st.set_page_config(page_title="Coda", layout="centered")

# This CSS makes the app look clean, soft, and easy on the eyes.
st.markdown("""
    <style>
    .stApp { background-color: #f7f9fc; }
    .stTextArea textarea { border-radius: 12px; border: 1px solid #d0d7de; }
    .stButton button { 
        background-color: #4a5568; 
        color: white; 
        border-radius: 10px; 
        font-weight: bold;
        height: 3em;
        width: 100%;
        border: none;
    }
    .stButton button:hover { background-color: #2d3748; color: white; }
    .comfort-card { 
        padding: 25px; 
        border-radius: 16px; 
        color: white; 
        margin-top: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. THE LOGIC (Simple & Bulletproof) ---
def get_guidance(stress, domain, problem):
    now = datetime.now().strftime("%I:%M %p")
    
    # Simple color shift based on how heavy things feel
    try:
        stress = int(stress)
    except:
        stress = 5
        
    if stress >= 8:
        bg_color = "#802b2b" # Warm, grounding brick red
    elif 4 <= stress <= 7:
        bg_color = "#3b4a6b" # Calm, steady slate blue
    else:
        bg_color = "#2d5a43" # Soft, peaceful forest green

    # Real, plain-English guidance
    guides = {
        "Technical/DIY": "Take a breath. When things aren't clicking, zoom in. What is the very smallest piece or line of code you can look at right now? Just focus on that one tiny part.",
        "Financial/Property": "Money and property can feel incredibly heavy. Strip away the 'what-ifs' for a second. What is the one factual number or single move that protects you today?",
        "Community/Advocacy": "Building a bridge or fighting for a cause takes time. You don't have to fix the whole system today. Who is just one person you can reach out to for a quick chat?",
        "General/Serene": "It is okay to feel overwhelmed. Right now, give yourself permission to step back. What is one kind, quiet thing you can do for yourself in the next five minutes?"
    }
    
    message = guides.get(domain, "Let's take it one small step at a time. What is the thing directly in front of you?")
    
    return f"""
        <div class="comfort-card" style="background-color: {bg_color};">
            <p style='opacity: 0.9; font-size: 0.9em; margin-bottom: 5px;'>Time: {now}</p>
            <h3 style='color: white; margin-top: 0; margin-bottom: 15px;'>Let's take a breath.</h3>
            <p style='font-size: 1.1em; line-height: 1.5;'>{message}</p>
            <hr style='border-color: rgba(255,255,255,0.2); margin: 15px 0;'>
            <p style='font-weight: bold; font-size: 1.1em; color: #ffe066;'>The Next Step:</p>
            <p style='font-size: 1.1em;'>Just do one small thing. Don't worry about how it turns out yet. Just make the move.</p>
        </div>
    """

# --- 3. THE INTERFACE (Digestible & Clean) ---
st.title("Coda")
st.write("A quiet space to figure out the next step.")

# Sidebar for profile (tucked away so it doesn't clutter the main screen)
with st.sidebar:
    st.header("Profile")
    name = st.text_input("What should I call you?", value="Friend")
    st.caption("Your entries aren't saved anywhere. This is just for this session.")

# Main input area
problem_text = st.text_area("What is on your mind or causing friction right now?", height=120)

col1, col2 = st.columns(2)
with col1:
    domain_choice = st.selectbox("What area of life is this?", ["General/Serene", "Technical/DIY", "Financial/Property", "Community/Advocacy"])
with col2:
    stress_val = st.select_slider("How heavy does it feel? (0 = Light, 10 = Heavy)", options=list(range(11)), value=5)

st.write("") # Adds a little clean spacing

if st.button("Get a Next Step"):
    if problem_text.strip():
        output_html = get_guidance(stress_val, domain_choice, problem_text)
        st.markdown(output_html
