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
    
    .comfort-card { 
        padding: 25px; 
        border-radius: 16px; 
        color: white !important; 
        margin-top: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. THE ADAPTABLE LOGIC ---
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
    now = datetime.now().strftime("%I:%M %p")
    
    # Adapt background color to the energy level
    try:
        stress = int(stress)
    except:
        stress = 5
        
    if stress >= 8:
        bg_color = "#802b2b" # Heavy / Urgent (Brick Red)
        strategy = "Emergency pause. Do not try to solve the whole puzzle right now."
        action = "Pick the single smallest piece you can physically touch or do in 60 seconds. Do only that."
    elif 4 <= stress <= 7:
        bg_color = "#3b4a6b" # Steady / Noisy (Slate Blue)
        strategy = "Momentum over perfection. Let's keep the wheels turning."
        action = "Write down just one sentence about what needs to happen next. Don't do it yet, just name it."
    else:
        bg_color = "#2d5a43" # Flow / Light (Forest Green)
        strategy = "Clear skies. This is a great time to organize or enjoy the build."
        action = "What is one fun or optimizing tweak you can make to this current project?"

    return f"""
        <div class="comfort-card" style="background-color: {bg_color};">
            <p style='opacity: 0.8; font-size: 0.9em; margin-bottom: 5px;'>Processed at {now}</p>
            <h3 style='color: white; margin-top: 0; margin-bottom: 10px;'>Let's look at this together.</h3>
            
            <p style='font-size: 1.1em; line-height: 1.5; margin-bottom: 15px;'>
                <strong>The Strategy:</strong> {strategy}
            </p>
            
            <hr style='border-color: rgba(255,255,255,0.2); margin: 15px 0;'>
            
            <p style='font-weight: bold; font-size: 1.1em; color: #ffe066; margin-bottom: 5px;'>Your Next Step:</p>
            <p style='font-size: 1.1em;'>{action}</p>
        </div>
    """

# --- 3. THE INTERFACE ---
st.title("Coda")
st.write("Drop your thoughts. Get a clear path forward.")

# We removed the sidebar and categories entirely to keep it clean.
problem_text = st.text_area("What is on your mind or causing friction right now?", height=150, placeholder="Type freely here...")

# Slider is front and center
stress_val = st.select_slider("How heavy does it feel? (0 = Light, 10 = Heavy)", options=list(range(11)), value=5)

st.write("") # Clean spacing

if st.button("Find the Next Step"):
    if problem_text.strip():
        output_html = get_guidance(stress_val, problem_text)
        st.markdown(output_html, unsafe_allow_html=True)
    else:
        st.info("Whenever you are ready, type what's on your mind above.")
