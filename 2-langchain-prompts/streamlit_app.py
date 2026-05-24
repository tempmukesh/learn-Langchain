import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

st.title("Chatbot")

if "history" not in st.session_state:
    st.session_state.history = [
        SystemMessage(content="You are a helpful AI assistant. Give concise 1-line answers.")
    ]

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.3)

user_input = st.chat_input("Ask something...")

if user_input:
    st.session_state.history.append(HumanMessage(content=user_input))
    response = model.invoke(st.session_state.history)
    st.session_state.history.append(AIMessage(content=response.content))

for msg in st.session_state.history:
    if isinstance(msg, HumanMessage):
        st.chat_message("user").write(msg.content)
    elif isinstance(msg, AIMessage):
        st.chat_message("assistant").write(msg.content)