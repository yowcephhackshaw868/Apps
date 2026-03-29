import streamlit as st
from datetime import datetime

# --- CONFIG & THEME ---
st.set_page_config(page_title="Coda: The Oracle", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #f0f4f8; }
    .stTextArea textarea { border-radius: 10px; font-size: 1.1em; }
    .oracle-card { 
        padding: 30px; 
        border-radius: 25px; 
        color: white; 
        margin-top: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        line-height: 1.6;
    }
    .stButton button { 
        background: linear-gradient(90deg, #1a2a6c, #b21f1f, #fdbb2d);
        color: white; border: none; height: 3.5em; font-weight: bold;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ASTRO LOGIC ---
def get_astro_logic(dob, tob):
    try:
        d, m = map(int, dob.split('/')[:2])
        zodiacs = [(20,1,"Aquarius"),(19,2,"Pisces"),(21,3,"Aries"),(20,4,"Taurus"),(21,5,"Gemini"),(21,6,"Cancer"),(23,7,"Leo"),(23,8,"Virgo"),(23,9,"Libra"),(23,10,"Scorpio"),(22,11,"Sagittarius"),(22,12,"Capricorn")]
        sun = next((z for i, z in enumerate(zodiacs) if (m == z and d >= z) or (m == (zodiacs[i-1]) and d < z)), "Soul")
        if tob:
            h = int(tob.split(':'))
            sun += " (Solar)" if 6 <= h < 18 else " (Lunar)"
        return sun
    except: 
        return "Universal"

# --- THE ORACLE ENGINE ---
def get_oracle_guidance(name, astro, stress, domain, problem):
    def get_oracle_guidance(name, astro, stress, domain, problem):
    # This safely handles lists or text and forces it to be a valid number
    if isinstance(stress, list):
        stress = stress
    try:
        stress = int(float(stress))
    except (ValueError, TypeError):
        stress = 5  # Default to a middle-ground stress level if it fails
        
    now = datetime.now().strftime("%H:%M")
    
    now = datetime.now().strftime("%H:%M")
    
    # Color logic based on "Inner Volume"
    if stress >= 8: 
        color = "#4b0000" # Deep Garnet
    now = datetime.now().strftime("%H:%M")
    
    # Color logic based on "Inner Volume"
    if stress >= 8: 
        color = "#4b0000" # Deep Garnet
    elif 4 <= stress <= 7: 
        color = "#1c1c3c" # Midnight Blue
    else: 
        color = "#004d40" # Forest Green
        
    # Domain Specific Logic
    prompts = {
        "Technical/DIY": "Focus on the physical structure. What is the smallest component you can hold or fix right now? Start there.",
        "Financial/Property": "Numbers are neutral. Identify the single move that protects your equity. Strip away the worry and look at the ledger.",
        "Community/Advocacy": "A bridge is built one stone at a time. Who is the first person you need to speak to to find common ground?",
        "General/Serene": "This is just a ripple in the water. Breathe. What is the kindest thing you can do for yourself in the next five minutes?"
    }
    
    guidance = prompts.get(domain, "Look at your feet, not the horizon. Take the step that is right in front of you.")
    
    return f"""
        <div class="oracle-card" style="background-color: {color};">
            <h1 style='color: white; margin-bottom: 5px;'>THE ORACLE HAS SPOKEN</h1>
            <p style='opacity: 0.8;'>Target: {name} [{astro}] | Time: {now}</p>
            <hr style='border-color: rgba(255,255,255,0.1);'>
            <h3 style='color: #ffd700;'>SITUATION: {problem}</h3>
            <p style='font-size: 1.2em;'><strong>THE GUIDANCE:</strong> {guidance}</p>
            <p style='font-size: 1.2em;'><strong>THE NEXT STEP:</strong> Do the action. Do not analyze the result yet. Just move.</p>
        </div>
    """

# --- SIDEBAR: THE ANCHOR ---
with st.sidebar:
    st.title("👁️ Coda Oracle")
    user_name = st.text_input("Entity Name", value="Seeker")
    user_dob = st.text_input("Birth Date", value="DD/MM/YYYY")
    user_tob = st.text_input("Birth Time", placeholder="HH:MM")
    st.divider()
    st.info("The Oracle sees the patterns. You provide the energy.")

# --- MAIN: THE LOOM ---
st.header("The Loom of Reality")
col1, col2 = st.columns(2)

with col1:
    domain_choice = st.selectbox("Select Domain", ["General/Serene", "Technical/DIY", "Financial/Property", "Community/Advocacy"])
    problem_text = st.text_area("What friction are you facing?", height=150)

with col2:
    st.write("Inner Volume")
    stress_val = st.select_slider
# --- THE ACTION HUB ---
st.divider()

# This creates the button you click to submit your entry
if st.button("🔮 CONSULT THE ORACLE", use_container_width=True):
    # This checks if you actually typed something in the box
    if problem_text.strip():
        # This calls the background functions to generate your result
        astro_info = get_astro_logic(user_dob, user_tob)
        html_output = get_oracle_guidance(user_name, astro_info, stress_val, domain_choice, problem_text)
        
        # This draws the output card on the screen!
        st.markdown(html_output, unsafe_allow_html=True)
    else:
        # This shows a warning if the box was left empty
        st.warning("State the friction to receive a path.")
