from langchain_community.document_loaders import PDFPlumberLoader

loader = PDFPlumberLoader("https://assets.accessible-digital-documents.com/uploads/2017/01/sample-tables.pdf")

pdf = loader.load()

# print(len(pdf)) 
print(pdf[0].page_content)
print(pdf[0].metadata)


