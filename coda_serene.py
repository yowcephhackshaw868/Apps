import streamlit as st
from datetime import datetime

# --- 1. SETTING THE MOOD ---
st.set_page_config(page_title="Coda", layout="centered")

# Safe CSS that only changes the button and card colors (won't blank the screen!)
st.markdown("""
    <style>
    /* Vibrant Green Button with Black Text */
    .stButton button { 
        background-color: #10b981 !important; 
        color: #000000 !important; 
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
    
    /* Pink border for the output card */
    .custom-card {
        padding: 25px;
        border-radius: 16px;
        margin-top: 20px;
        border: 2px solid #ec4899; /* Pink */
        background-color: #1f2937; /* Dark Silver/Gray */
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. THE MALLEABLE LOGIC ---
def get_detailed_guidance(stress, domain, persona, focus, problem):
    try:
        stress = int(stress)
    except:
        stress = 5
        
    # 1. Header & Strategy based on Stress
    if stress >= 8:
        header = "🛑 Urgent De-escalation"
        strategy = "I can tell this is feeling incredibly heavy right now. My main goal here is to help you protect your energy and find solid ground. Let's not try to solve the whole puzzle today."
    elif 4 <= stress <= 7:
        header = "⚡ Progress & Momentum"
        strategy = "I see there is some friction here, but you've definitely got the energy to tackle it. Let's channel that into some steady momentum together."
    else:
        header = "🌱 Flow & Optimization"
        strategy = "Things are looking pretty clear here. I think this is a perfect window for us to organize, build systems, or just find some joy in refining your work."

    # 2. Personalized Insight based on Persona and Focus
    insight = f"Since you asked me to be **{persona.lower()}** and prioritize **{focus.lower()}**, I want to make sure we find a path that respects both of those goals."

    # 3. Custom Action based on Domain (Now in 1st person!)
    if domain == "Personal Life":
        action = "I've been thinking about the friction you mentioned. My advice is to find just one small boundary or space you can create for yourself today. Let's give you a little room to breathe and reset."
    elif domain == "Technical/DIY Projects":
        action = "Looking at what you're building, I think our best move is to isolate the absolute smallest component or line of code causing the bottleneck. Let's ignore the big picture for a few minutes and just get that one small gear to turn."
    elif domain == "Advocacy/Community":
        action = "I know that building bridges and organizing takes a massive amount of time. I'd suggest reaching out to just one person in your circle for a quick, grounding chat today to share the load."
    else: # Financial Strategy
        action = "Money and planning can get so loud and overwhelming. I want us to strip away the big 'what-ifs' right now and focus on the single, most practical move that protects your position today."

    return header, strategy, insight, action


# --- 3. THE INTERFACE ---
st.title("Coda")
st.write("A customizable space to map your next steps.")

# Simple expander for settings
with st.expander("🛠️ Personalize Your Help", expanded=True):
    col1, col2 = st.columns(2)
    
    with col1:
        user_persona = st.selectbox("How do you want to be treated?", ["A supportive peer", "An objective strategist", "A creative visionary"])
        user_domain = st.selectbox("What domain are we focusing on?", ["Personal Life", "Technical/DIY Projects", "Advocacy/Community", "Financial Strategy"])
        
    with col2:
        user_focus = st.selectbox("What is your primary focus right now?", ["Speed & Momentum", "Depth & Quality", "Peace & Calm", "Strict Problem Solving"])
        stress_val = st.select_slider("How heavy does it feel? (0 = Light, 10 = Heavy)", options=list(range(11)), value=5)

st.write("") 

problem_text = st.text_area("What friction or challenge are you facing?", height=150, placeholder="Type freely here...")

st.write("") 

# This is the part that was missing!
if st.button("Consult the System"):
    if problem_text.strip():
        header, strategy, insight, action = get_detailed_guidance(stress_val, user_domain, user_persona, user_focus, problem_text)
        
        st.divider()
        
        # This draws the pretty card on the screen!
        st.markdown(f"""
            <div class="custom-card">
                <h2 style='color: #10b981; margin-top: 0;'>{header}</h2>
                <p style='font-size: 1.1em; line-height: 1.6; color: #fce7f3;'><strong>The Strategy:</strong> {strategy}</p>
                <hr style='border-color: #ec4899; margin: 20px 0;'>
                <p style='color: #fce7f3; font-size: 1.1em; margin-bottom: 12px;'>{insight}</p>
                <p style='color: #fce7f3; font-size: 1.1em; line-height: 1.6;'><strong>Your Next Move:</strong> {action}</p>
            </div>
        """, unsafe_allow_html=True)
            
    else:
        st.info("Whenever you are ready, type what's on your mind above and click the button.")
