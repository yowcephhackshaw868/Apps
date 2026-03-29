import streamlit as st
import google.generativeai as genai

# --- 0. API SETUP ---
# ⚠️ This key is public now, so remember to replace it in AI Studio later!
GEMINI_API_KEY = "AIzaSyAARJHCZngMW4ybe4labAQ6EvPDDfOu_E4" 

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')

# --- 1. SETTING THE MOOD ---
st.set_page_config(page_title="Coda", layout="centered")

st.markdown("""
<style>
.stButton button { 
    background-color: #10b981 !important; 
    color: #000000 !important; 
    border-radius: 12px; 
    font-weight: bold;
    height: 3.5em;
    width: 100%;
    border: 2px solid #e2e8f0 !important;
}
.stButton button:hover { 
    background-color: #059669 !important; 
    color: #ffffff !important;
}
.custom-card {
    padding: 25px;
    border-radius: 16px;
    margin-top: 20px;
    margin-bottom: 20px;
    border: 2px solid #ec4899; 
    background-color: #1f2937; 
}
</style>
""", unsafe_allow_html=True)
# --- 2. THE AI GENERATOR ---
def generate_roadmap(problem, persona, focus, domain):
    """Calls Gemini to generate a highly tailored, first-person 3-phase roadmap."""
    if not model:
        # Fallback text if no API key is provided yet
        return (
            "No API Key Detected",
            "Please add your Gemini API key at the top of the file to generate live roadmaps!",
            "I'm ready to act as your collaborator, but I need my AI brain connected.",
            "Add your API key to the script.", "Then click get help.", "Watch the magic happen."
        )

    prompt = f"""
    You are an AI collaborator helping a user solve a problem. 
    Act as: {persona}.
    Primary focus: {focus}.
    Domain: {domain}.
    
    The user is facing this issue: "{problem}"
    
    Provide a response in exactly this structure. Do not use the words 'Phase 1', 'Phase 2', or 'Phase 3' in your actual answers, just provide the advice. Speak in the first person. Do not quote back the user's settings.
    
    [HEADER]: A short, supportive 3-5 word title for this specific challenge.
    [STRATEGY]: A warm, grounding 1-2 sentence high-level strategy to de-escalate or focus.
    [INSIGHT]: A personal insight on how to approach this given the user's focus.
    [P1]: What is the immediate triage or first step to stop the bleeding?
    [P2]: How do they build momentum or execute the core solution next?
    [P3]: What is the long-term resolution or system to prevent it?
    """
    
    try:
        response = model.generate_content(prompt)
        text = response.text
        
        # Simple parser to extract the custom tags
        def extract(tag):
            try: return text.split(f"[{tag}]:").split("[").strip()
            except: return "I'm still processing this step..."
            
        return extract("HEADER"), extract("STRATEGY"), extract("INSIGHT"), extract("P1"), extract("P2"), extract("P3")
    except Exception as e:
        return "Error", f"Could not connect to AI: {str(e)}", "Please check your API key.", "Error", "Error", "Error"


# --- 3. THE INTERFACE ---
st.title("Coda")
st.write("A customizable space to map your next steps.")

with st.expander("🛠️ Personalize Your Help", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        user_persona = st.selectbox("How do you want to be treated?", ["A supportive peer", "An objective strategist", "A creative visionary"])
        user_domain = st.selectbox("What domain are we focusing on?", ["Personal Life", "Technical/DIY Projects", "Advocacy/Community", "Financial Strategy"])
    with col2:
        user_focus = st.selectbox("What is your primary focus right now?", ["Speed & Momentum", "Depth & Quality", "Peace & Calm", "Strict Problem Solving"])
        stress_val = st.select_slider("How heavy does it feel? (0 = Light, 10 = Heavy)", options=list(range(11)), value=5)

st.write("") 

# --- 4. THE INFINITE LOOP LOGIC ---
if "history" not in st.session_state:
    st.session_state.history = []

problem_text = st.text_area("What friction or challenge are you facing?", height=100, placeholder="Type freely here...")

# First interaction
if st.button("Get Help", key="main_btn"):
    if problem_text.strip():
        # Clear old history on a fresh main search
        st.session_state.history = []
        h, s, i, p1, p2, p3 = generate_roadmap(problem_text, user_persona, user_focus, user_domain)
        st.session_state.history.append({
            "problem": problem_text, "header": h, "strategy": s, "insight": i,
            "p1": p1, "p2": p2, "p3": p3
        })
    else:
        st.info("Whenever you are ready, type what's on your mind above and click the button.")

# Render the continuous, looping chain of roadmaps
for idx, entry in enumerate(st.session_state.history):
    st.divider()
    
    # Render the card for this level
    st.markdown(f"""
        <div class="custom-card">
            <h2 style='color: #10b981; margin-top: 0;'>Level {idx+1}: {entry['header']}</h2>
            <p style='font-size: 1.1em; line-height: 1.6; color: #fce7f3;'><strong>The Strategy:</strong> {entry['strategy']}</p>
            <hr style='border-color: #ec4899; margin: 20px 0;'>
            <p style='color: #fce7f3; font-size: 1.1em; margin-bottom: 5px;'>{entry['insight']}</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Phase 1 Loop
    st.markdown(f"#### 🛠️ Phase 1: Immediate Triage")
    st.write(entry['p1'])
    p1_in = st.text_input("Deepen this step / brainstorm your roadblock:", key=f"p1_in_{idx}", placeholder="Type what's hard about this step...")
    if st.button("Get Help with this Step", key=f"p1_btn_{idx}"):
        if p1_in.strip():
            h, s, i, p1, p2, p3 = generate_roadmap(p1_in, user_persona, user_focus, user_domain)
            st.session_state.history.append({"problem": p1_in, "header": h, "strategy": s, "insight": i, "p1": p1, "p2": p2, "p3": p3})
            st.rerun()

    # Phase 2 Loop
    st.write("") 
    st.markdown(f"#### ⚡ Phase 2: Building Momentum")
    st.write(entry['p2'])
    p2_in = st.text_input("Deepen this step / brainstorm your roadblock:", key=f"p2_in_{idx}", placeholder="Type what's hard about this step...")
    if st.button("Get Help with this Step", key=f"p2_btn_{idx}"):
        if p2_in.strip():
            h, s, i, p1, p2, p3 = generate_roadmap(p2_in, user_persona, user_focus, user_domain)
            st.session_state.history.append({"problem": p2_in, "header": h, "strategy": s, "insight": i, "p1": p1, "p2": p2, "p3": p3})
            st.rerun()

    # Phase 3 Loop
    st.write("") 
    st.markdown(f"#### 🎯 Phase 3: Long-term Resolution")
    st.write(entry['p3'])
    p3_in = st.text_input("Deepen this step / brainstorm your roadblock:", key=f"p3_in_{idx}", placeholder="Type what's hard about this step...")
    if st.button("Get Help with this Step", key=f"p3_btn_{idx}"):
        if p3_in.strip():
            h, s, i, p1, p2, p3 = generate_roadmap(p3_in, user_persona, user_focus, user_domain)
            st.session_state.history.append({"problem": p3_in, "header": h, "strategy": s, "insight": i, "p1": p1, "p2": p2, "p3": p3})
            st.rerun()
