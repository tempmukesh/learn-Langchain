from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# Create the model
llm = ChatOpenAI(
    model="mistralai/devstral-2512:free",
    base_url="https://openrouter.ai/api/v1",
    temperature=0.3,
)


# chatbot 
