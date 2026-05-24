from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model = "...",
    temperature=0.0,

)

output  = model.invoke("What is system design ?")

# output have 
# 1. content 
# 2. metadata 


result = output.content

print(result)