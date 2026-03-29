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

# --- 2. THE FLESHED-OUT LOGIC ---
def get_detailed_guidance(stress, domain, persona, focus):
    try:
        stress = int(stress)
    except:
        stress = 5
        
    if stress >= 8:
        header = "🛑 Emergency De-escalation Path"
        strategy = "When things are this heavy, your only goal is to stop the bleeding and find solid ground. Do not attempt to solve the whole problem today."
        steps = [
            "**Step 1 (First 60 Seconds):** Put down whatever you are holding. Take three slow breaths. Feel your feet on the floor. Right now, you are safe.",
            "**Step 2 (The Next Hour):** Identify the single most urgent thread of this problem. Ignore the rest. What is the one thing that will cause a collapse if not handled? Do only that.",
            f"**Step 3 (Moving Forward as a {persona}):** Lean heavily on your natural strengths. You don't have to carry the whole world. Step back and delegate or pause what you can."
        ]
    elif 4 <= stress <= 7:
        header = "⚡ Momentum & Progress Path"
        strategy = "You have energy, but there is friction. The goal here is momentum over perfection. Let's break the paralysis and get moving."
        steps = [
            "**Step 1 (The Setup):** Clear your physical workspace or close unnecessary tabs. Visual clutter creates mental clutter.",
            f"**Step 2 (The {domain} Approach):** Look at this through a structured lens. Write down the top 3 things that need to happen. Cross off the bottom 2.",
            f"**Step 3 (Focusing on {focus}):** Since you want to prioritize {focus.lower()}, make your next action directly serve that goal. Do not get distracted by side quests."
        ]
    else:
        header = "🌱 Optimization & Growth Path"
        strategy = "Things are flowing well. This is the perfect time to organize, build systems, and find joy in the process."
        steps = [
            "**Step 1 (Refine):** Look at what you've already built or done. What is one small tweak that would make it 10% more efficient or enjoyable?",
            f"**Step 2 (The {persona} Vision):** How does solving this friction help you grow into the person you want to be? Take a moment to appreciate your progress.",
            f"**Step 3 (The Master Move):** Since things are light, take a risk or try a creative solution you wouldn't normally have the energy for."
        ]

    return header, strategy, steps


# --- 3. THE INTERFACE ---
st.title("Coda")
st.write("A customizable space to map your next steps.")

# Simple expander for settings
with st.expander("🛠️ Personalize Your Oracle", expanded=True):
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

if st.button("Consult the System"):
    if problem_text.strip():
        header, strategy, steps = get_detailed_guidance(stress_val, user_domain, user_persona, user_focus)
        
        st.divider()
        
        # This draws the pretty card on the screen!
        st.markdown(f"""
            <div class="custom-card">
                <h2 style='color: #10b981; margin-top: 0;'>{header}</h2>
                <p style='font-size: 1.1em; line-height: 1.6; color: #fce7f3;'><strong>The Strategy:</strong> {strategy}</p>
                <hr style='border-color: #ec4899; margin: 20px 0;'>
                <h4 style='color: #e2e8f0; margin-bottom: 10px;'>Your Tailored Action Plan:</h4>
                <p style='color: #fce7f3; margin-bottom:
