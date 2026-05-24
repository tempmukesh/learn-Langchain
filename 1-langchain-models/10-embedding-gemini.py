from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()


# Initialize embeddings model
embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

# Single query embedding
vector = embeddings.embed_query("hello, world!")


print(vector)

# Batch document embeddings
docs = ["Today is Monday", "Today is Tuesday", "Today is April Fools day"]

vectors = embeddings.embed_documents(docs)

print(len(vectors), len(vectors[0]))