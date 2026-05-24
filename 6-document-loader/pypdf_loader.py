# pip install pypdf  # make sure installed in your sysytem 
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("The_Research_Layer.pdf")

pdf = loader.load()

# print(len(pdf)) # 47 page converted each page in single document 

print(pdf[0].page_content)
print(pdf[0].metadata)
