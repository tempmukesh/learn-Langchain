from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage , AIMessage , SystemMessage   
from dotenv import load_dotenv
import streamlit as st 

load_dotenv()


model = ChatGoogleGenerativeAI(model= "gemini-2.5-flash" , temperature= 0.3)


# chat history that to not halosinate 
chat_history = [
    SystemMessage(content= "You are a Helpful AI assistant Who  concise as answer 1 line answer"),
]

print("Chat started! Type 'exit' to quit.\n")

while True:
    user_input = input("You : ")
    # append the query 
    if user_input == "exit":
        print("chat ended.")
        break
    
    chat_history.append(HumanMessage(content = user_input))
    
    
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content  = result.content))
    
    print("AI : " , result.content)

print(chat_history)