import streamlit as st
import google.generativeai as genai

# --- 0. API SETUP ---
# ⚠️ Put your actual Gemini API key here
GEMINI_API_KEY = "AIzaSyDVGq2CwF4a3Y0jSDzV3bud7TFxwhXvt18" 

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')

# --- 1. SETTING THE MOOD ---
st.set_page_config(page_title="Coda", layout="centered")

# Custom styling to keep your vibe
st.markdown("""
    <style>
    .stChatMessage {
        border-radius: 12px;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. THE CHAT INITIALIZATION ---
# This ensures our chat history survives app reruns
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- 3. THE INTERFACE ---
st.title("Coda")
st.write("A conversational space to work through your friction.")

# Sidebar for settings so they don't clutter the chat
with st.sidebar:
    st.header("🛠️ Persona Settings")
    user_persona = st.selectbox("How do you want to be treated?", ["A supportive peer", "An objective strategist", "A creative visionary"])
    user_domain = st.selectbox("What domain are we focusing on?", ["Personal Life", "Technical/DIY Projects", "Advocacy/Community", "Financial Strategy"])
    user_focus = st.selectbox("What is your primary focus right now?", ["Speed & Momentum", "Depth & Quality", "Peace & Calm", "Strict Problem Solving"])
    stress_val = st.select_slider("How heavy does it feel? (0 = Light, 10 = Heavy)", options=list(range(11)), value=5)
    
    st.divider()
    if st.button("Clear Conversation"):
        st.session_state.messages = []
        st.rerun()

# --- 4. DISPLAY CONVERSATION HISTORY ---
# This renders the past messages every time the screen refreshes
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- 5. HANDLE NEW USER INPUT ---
# st.chat_input places a sticky text bar at the absolute bottom of the screen!
if prompt := st.chat_input("What challenge are we solving today?"):
    
    # 1. Show the user's message immediately
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # 2. Add it to our memory
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # 3. Build a smart prompt for Gemini using your sidebar settings
    full_prompt = f"""
    You are an AI collaborator helping a user solve problems in real-time conversation.
    Act as: {user_persona}.
    Primary focus: {user_focus}.
    Domain: {user_domain}.
    The user's current stress level is {stress_val}/10.

    Keep your tone highly conversational, first-person, and authentic. 
    If they are starting a brand new problem, give them a brief strategy and break your advice into clear, actionable steps or phases. 
    If they are replying to a previous step, help them brainstorm that specific friction.

    User says: "{prompt}"
    """
    
    # 4. Generate the response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        try:
            # We can use streaming so the text appears letter-by-letter as it thinks!
            response = model.generate_content(full_prompt, stream=True)
            
            full_response = ""
            for chunk in response:
                full_response += chunk.text
                message_placeholder.markdown(full_response + "▌")
            
            message_placeholder.markdown(full_response)
            
            # Save the assistant response to memory
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            
        except Exception as e:
            st.error(f"Could not connect to AI: {str(e)}")
