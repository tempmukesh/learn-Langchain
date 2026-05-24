from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np 

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

documents = [
"Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
"MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
"Sachin.Tendulkar, also known as the 'God of Cricket', holds many batting recerds.",
"Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
"Jasprit Bumrah is an Indian fast bowler known for his unothodox action and yorkers",
]

query = "tell me about Ms dhoni"

document_embedding = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

# 2d 
score = cosine_similarity([query_embedding] , document_embedding)[0]

index , score = sorted(list(enumerate(score)) , key = lambda x:x[1])[-1]

print(query)
print(documents[index])
print("similarity score is : ", score)