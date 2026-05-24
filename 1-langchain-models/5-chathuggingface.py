from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    model = "TinyLlama/TinyLlama-1.1B-Chat-v1.0", 
    task = "text-generation",
)

model = ChatHuggingFace(llm = llm)

result = model.invoke("What is the area of a square")

print(result.content)

