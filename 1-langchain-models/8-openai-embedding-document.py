from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(
    model = "text-embedding-ada-002", 
    dimensions= 348
)


document = [
    "Delhi is the capital of India",
    "Kolkata is the capital of west bengal",
    "Paris id the capital of France"
]


result = embedding.embed_documents(document)
print(str(result))

