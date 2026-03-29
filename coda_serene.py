import streamlit as st
from datetime import datetime

# --- 1. SETTING THE MOOD ---
st.set_page_config(page_title="Coda", layout="centered")

# Smooth, dark mode readable styling
st.markdown("""
    <style>
    .stApp { background-color: #1a202c !important; }
    h1, h2, h3, h4, p, span, label { color: #e2e8f0 !important; }
    
    .stTextArea textarea, .stTextInput input { 
        background-color: #ffffff !important; 
        color: #1a202c !important; 
        border-radius: 10px;
    }
    
    .stButton button { 
        background-color: #4a5568 !important; 
        color: white !important; 
        border-radius: 10px; 
        font-weight: bold;
        height: 3.5em;
        width: 100%;
        border: none;
    }
    .stButton button:hover { background-color: #2d3748 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. THE ADAPTABLE LOGIC ---
def get_guidance(stress, problem):
    # Adapt background color to the energy level
    try:
        stress = int(stress)
    except:
        stress = 5
        
    if stress >= 8:
        strategy = "Emergency pause. Do not try to solve the whole puzzle right now."
        action = "Pick the single smallest piece you can physically touch or do in 60 seconds. Do only that."
    elif 4 <= stress <= 7:
        strategy = "Momentum over perfection. Let's keep the wheels turning."
        action = "Write down just one sentence about what needs to happen next. Don't do it yet, just name it."
    else:
        strategy = "Clear skies. This is a great time to organize or enjoy the build."
        action = "What is one fun or optimizing tweak you can make to this current project?"

    return strategy, action


# --- 3. THE INTERFACE ---
st.title("Coda")
st.write("Drop your thoughts. Get a clear path forward.")

problem_text = st.text_area("What is on your mind or causing friction right now?", height=150, placeholder="Type freely here...")
stress_val = st.select_slider("How heavy does it feel? (0 = Light, 10 = Heavy)", options=list(range(11)), value=5)

st.write("") # Clean spacing

if st.button("Find the Next Step"):
    if problem_text.strip():
        # Get the simple text strings instead of a big messy HTML block
        strategy, action = get_guidance(stress_val, problem_text)
        
        # Display them using Streamlit's built-in clean containers
        st.divider()
        
        # This creates a pretty, clean callout box without any code leaks!
        with st.container(border=True):
            st.subheader("Let's look at this together.")
            st.write(f"**The Strategy:** {strategy}")
            st.write(f"**Your Next Step:** {action}")
            
    else:
        st.info("Whenever you are ready, type what's on your mind above.")
