from langchain_experimental.text_splitter import SemanticChunker
from langchain_huggingface import HuggingFaceEmbeddings 

from dotenv import load_dotenv

load_dotenv()

sample = """
In the bustling cities and quiet villages alike, innovation and determination shape the rhythm of daily life. Engineers design bridges that connect distant communities, while teachers ignite curiosity in classrooms filled with eager minds. The digital age has blurred boundaries, allowing ideas to travel faster than ever, creating a tapestry of cultures interwoven through shared knowledge. Festivals and sporting events, whether local or global, remind people of the joy found in collective celebration, transcending borders and languages. Yet, challenges persist—climate change threatens ecosystems, inequality tests social harmony, and misinformation clouds judgment. Against these trials, societies discover strength in cooperation: scientists collaborate across continents, citizens advocate for justice, and leaders strive to balance tradition with progress. It is within this interplay of struggle and hope that humanity continues to evolve, proving that resilience is not merely survival but the art of transforming adversity into opportunity."""


embedding = HuggingFaceEmbeddings(model = "sentence-transformers/all-MiniLM-L6-v2")


text_splitter = SemanticChunker(
    embeddings= embedding,
    breakpoint_threshold_type="standard_deviation",  # Options: "standard_deviation", "percentile", "interquartile", "gradient"
    breakpoint_threshold_amount=1  # Can be 1, 2, 3 for standard deviations
)

chunks = text_splitter.create_documents([sample])

print(f"Number of chunks: {len(chunks)}")
print("\nChunks:")
for i, chunk in enumerate(chunks, 1):
    print(f"\n--- Chunk {i} ---")
    print(chunk)