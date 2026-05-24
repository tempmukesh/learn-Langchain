from langchain_community.document_loaders import DirectoryLoader , PyPDFLoader

loader = DirectoryLoader(
    path="C:/Users/Crashlar/Desktop/Book",
    glob="*.pdf",
    loader_cls= PyPDFLoader
)

docs = loader.load()

# print(len(docs))
print(docs[0].metadata)
print(docs[0].page_content)

# load is worst to use for big memory data 
# so use lazy_load()