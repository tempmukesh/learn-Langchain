from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


loader = TextLoader(
    file_path="profile.txt",
    encoding="utf-8"
)

docs = loader.load()

print(docs)

prompts = PromptTemplate(
    template="Write a summary of the following poem -\n {poem}",
    input_variables=['poem']
)

parser = StrOutputParser()

