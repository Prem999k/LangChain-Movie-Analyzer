import streamlit as st
from dotenv import load_dotenv

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

# Load ENV
load_dotenv()

# Page Settings
st.set_page_config(
    page_title="Mood AI ChatBot",
    page_icon="🤖",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: white;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    color: gray;
    margin-bottom: 30px;
}

.mode-box {
    padding: 15px;
    border-radius: 12px;
    text-align: center;
    font-weight: bold;
    margin-bottom: 20px;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# Title
st.markdown(
    '<div class="title">🤖 Mood AI ChatBot</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Chat with Different AI Personalities</div>',
    unsafe_allow_html=True
)

# Model
model = ChatMistralAI(
    model="mistral-small-2603",
    temperature=0.9,
    max_tokens=120
)

# Modes
modes = {
    "😂 Funny": "You are a Funny AI Agent. Give humorous responses.",
    
    "😡 Angry": "You are an Angry AI Agent. Reply aggressively.",
    
    "😢 Sad": "You are a Sad AI Agent. Reply emotionally."
}

# Top Navigation Style
col1, col2, col3 = st.columns(3)

with col1:
    funny = st.button("😂 Funny")

with col2:
    angry = st.button("😡 Angry")

with col3:
    sad = st.button("😢 Sad")

# Default Mode
if "mode" not in st.session_state:
    st.session_state.mode = "😂 Funny"

# Change Modes
if funny:
    st.session_state.mode = "😂 Funny"
    st.session_state.chat_history = [
        SystemMessage(content=modes["😂 Funny"])
    ]

if angry:
    st.session_state.mode = "😡 Angry"
    st.session_state.chat_history = [
        SystemMessage(content=modes["😡 Angry"])
    ]

if sad:
    st.session_state.mode = "😢 Sad"
    st.session_state.chat_history = [
        SystemMessage(content=modes["😢 Sad"])
    ]

# Chat History
if "chat_history" not in st.session_state:

    st.session_state.chat_history = [
        SystemMessage(
            content=modes[st.session_state.mode]
        )
    ]

# Current Mode Display
st.markdown(
    f"""
    <div class="mode-box">
        Current Mode: {st.session_state.mode}
    </div>
    """,
    unsafe_allow_html=True
)

# Show Messages
for message in st.session_state.chat_history:

    if isinstance(message, HumanMessage):

        with st.chat_message("user"):
            st.markdown(message.content)

    elif isinstance(message, AIMessage):

        with st.chat_message("assistant"):
            st.markdown(message.content)

# Input
prompt = st.chat_input("Type your message...")

if prompt:

    # User Message
    st.session_state.chat_history.append(
        HumanMessage(content=prompt)
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # AI Response
    response = model.invoke(
        st.session_state.chat_history
    )

    st.session_state.chat_history.append(
        AIMessage(content=response.content)
    )

    with st.chat_message("assistant"):
        st.markdown(response.content)