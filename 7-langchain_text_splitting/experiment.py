from langchain_classic import SemanticChunker
from langchain_openai import OpenAIEmbeddings

# Sample text with different topics
text = """
Agriculture is the backbone of India's economy. Farmers work hard in the fields. 
The sun was bright and the air smelled of earth and fresh grass.

The Indian Premier League (IPL) is a professional Twenty20 cricket league in India. 
It features teams representing different cities. Virat Kohli plays for RCB.

Terrorism is a global threat that affects peace and security. 
Countries worldwide are working together to combat this menace.
"""

# Create semantic chunker with OpenAI embeddings
text_splitter = SemanticChunker(
    embeddings=OpenAIEmbeddings(),
    breakpoint_threshold_type="standard_deviation",  # Options: "standard_deviation", "percentile", "interquartile", "gradient"
    breakpoint_threshold_amount=1  # Can be 1, 2, 3 for standard deviations
)

# Split the text
chunks = text_splitter.split_text(text)

# Display results
print(f"Number of chunks: {len(chunks)}")
print("\nChunks:")
for i, chunk in enumerate(chunks, 1):
    print(f"\n--- Chunk {i} ---")
    print(chunk)