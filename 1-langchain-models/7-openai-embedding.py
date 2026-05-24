from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(
    model = "text-embedding-ada-002", 
    dimensions= 348
)



result = embedding.embed_query("Delhi is the Capital of India")

print(str(result))

