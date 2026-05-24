from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("C:/Users/Crashlar/Desktop/Book/AI Engineering by Chip Huyen.pdf")

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size = 150,
    chunk_overlap = 10 , 
    separator='' 
)

result = splitter.split_documents(docs)

# print(result[0])

print(result[0].page_content)
print(result[0].metadata)