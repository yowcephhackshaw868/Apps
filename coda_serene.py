import streamlit as st
from datetime import datetime

# --- 1. SETTING THE MOOD ---
st.set_page_config(page_title="Coda", layout="centered")

# Safe CSS that styles the button and the card border
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

# --- 2. THE MALLEABLE LOGIC (With Full Roadmaps) ---
def get_detailed_guidance(stress, domain, persona, focus, problem):
    try:
        stress = int(stress)
    except:
        stress = 5
        
    # 1. Header & Strategy based on Stress
    if stress >= 8:
        header = "🛑 Strategic De-escalation Roadmap"
        strategy = "I can tell this is feeling incredibly heavy right now. My main goal here is to help you protect your energy and find solid ground. Let's not try to solve the whole puzzle today."
        
        phase_1 = "Pause everything. Put down whatever you are holding and identify the single most urgent thread of this problem. Disregard the rest for the next 24 hours. Your only job is to stop the bleeding."
        phase_2 = "Once you have stabilized the immediate fire, let's look at what is causing the bottleneck. We will pick the smallest, most accessible action step to prove to yourself that you are making progress."
        phase_3 = "After we establish that initial win, we can look at the bigger picture and figure out how to delegate, automate, or prevent this heavy friction from stacking up again."
        
    elif 4 <= stress <= 7:
        header = "⚡ Progress & Momentum Roadmap"
        strategy = "I see there is some friction here, but you've definitely got the energy to tackle it. Let's channel that into some steady momentum together."
        
        phase_1 = "Clear your physical workspace or close unnecessary tabs to remove background noise. Write down the top 3 things that need to happen today, and cross off the bottom 2."
        phase_2 = "Execute the remaining task with full focus. Don't let yourself get distracted by perfect results—just focus on finishing and pushing the ball down the court."
        phase_3 = "Once the immediate work is done, let's take a quick look at why this friction popped up and make a small system adjustment so it doesn't slow you down next time."
        
    else:
        header = "🌱 Flow & Optimization Roadmap"
        strategy = "Things are looking pretty clear here. I think this is a perfect window for us to organize, build systems, or just find some joy in refining your work."
        
        phase_1 = "Look at what you have already built or executed recently. Let's find one small tweak that would make it 10% more efficient or enjoyable for you to maintain."
        phase_2 = "Use this calm window to map out your next big move or project. Since your stress is low, take a calculated risk or try a creative solution you wouldn't normally have the energy for."
        phase_3 = "Reflect on how smooth this process felt. Let's document or lock in this workflow so we can replicate this low-stress environment in the future."

    # 2. Personalized Insight shaped SILENTLY by Persona and Focus
    if persona == "A supportive peer":
        if focus == "Peace & Calm":
            insight = "I want you to take a deep breath and remember that you don't have to carry all of this at once. Whatever we do next should make you feel lighter, not more burdened."
        elif focus == "Speed & Momentum":
            insight = "Let's link up and get a quick win under our belts. I'm right here with you, and I think getting one fast victory will shift the whole mood."
        else:
            insight = "Let's put our heads together on this. I want to help you find a path forward that feels genuinely good to execute."
            
    elif persona == "An objective strategist":
        if focus == "Strict Problem Solving":
            insight = "Let's look at the facts and strip away the noise. I want to help you map out the most logical, high-impact move available to us right now."
        elif focus == "Depth & Quality":
            insight = "I want to help you look at the foundation of this challenge. Let's make sure our next move is calculated and built to last."
        else:
            insight = "Let's evaluate the landscape here. I want to find the most efficient leverage point to shift this situation in your favor."
            
    else: # A creative visionary
        if focus == "Peace & Calm":
            insight = "I want to help you find the hidden harmony here. Let's look past the stress and see how this friction can guide us toward a more peaceful design."
        else:
            insight = "I see a really interesting opportunity hidden inside this challenge. Let's look at this from a fresh angle and create something unique."

    return header, strategy, insight, phase_1, phase_2, phase_3


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

# 1. Initialize our scratchpad so it remembers if we clicked the button
if "consulted" not in st.session_state:
    st.session_state.consulted = False
    st.session_state.header = ""
    st.session_state.strategy = ""
    st.session_state.insight = ""
    st.session_state.phase_1 = ""
    st.session_state.phase_2 = ""
    st.session_state.phase_3 = ""

# 2. When the button is clicked, save the generated text to the scratchpad
if st.button("Get Help"):
    if problem_text.strip():
        # Call the logic function
        h, s, i, p1, p2, p3 = get_detailed_guidance(stress_val, user_domain, user_persona, user_focus, problem_text)
        
        # Save them to session state so they survive the reruns!
        st.session_state.consulted = True
        st.session_state.header = h
        st.session_state.strategy = s
        st.session_state.insight = i
        st.session_state.phase_1 = p1
        st.session_state.phase_2 = p2
        st.session_state.phase_3 = p3
    else:
        st.info("Whenever you are ready, type what's on your mind above and click the button.")

# 3. If we have consulted the system, ALWAYS show the results (even if typing reruns the script)
if st.session_state.consulted:
    st.divider()
    
    # Render the card
    st.markdown(f"""
        <div class="custom-card">
            <h2 style='color: #10b981; margin-top: 0;'>{st.session_state.header}</h2>
            <p style='font-size: 1.1em; line-height: 1.6; color: #fce7f3;'><strong>The Strategy:</strong> {st.session_state.strategy}</p>
            <hr style='border-color: #ec4899; margin: 20px 0;'>
            <p style='color: #fce7f3; font-size: 1.1em; margin-bottom: 5px;'>{st.session_state.insight}</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Render the phases and inputs
    st.write("") 
    st.markdown(f"#### 🛠️ Phase 1: Immediate Triage")
    st.write(st.session_state.phase_1)
    st.text_input("Your notes / action plan for Phase 1:", key="phase1_input", placeholder="Type how you'll execute this here...")
    
    st.write("") 
    st.markdown(f"#### ⚡ Phase 2: Building Momentum")
    st.write(st.session_state.phase_2)
    st.text_input("Your notes / action plan for Phase 2:", key="phase2_input", placeholder="Type your milestones or tasks here...")
    
    st.write("") 
    st.markdown(f"#### 🎯 Phase 3: Long-term Resolution")
    st.write(st.session_state.phase_3)
    st.text_input("Your notes / action plan for Phase 3:", key="phase3_input", placeholder="Type how you'll prevent this next time...")
