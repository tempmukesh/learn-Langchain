from langchain_community.document_loaders import TextLoader
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

path = "national_anthem.txt"

loader = TextLoader(path , encoding="utf-8")

docs = loader.load()

# print(docs) ## type is list 
# print(len(docs))

# in every data have 
# [metadata , page_ccontent]


# print(docs[0])
# print(type(docs[0])) # <class 'langchain_core.documents.base.Document'>
# print(docs[0].metadata) # extract the metadata 
# print(docs[0].page_content) # extract the data from the txt file 


# ------now generating the summary of the txt.file content-------------
load_dotenv()


llm = HuggingFaceEndpoint(
    model = "deepseek-ai/DeepSeek-V3.2",
    task = "text_generation"
)

model = ChatHuggingFace(llm = llm )


prompt = PromptTemplate(
    template="generate the summary on {text}",
    input_variables=['text']
)

parser = StrOutputParser()


chain = prompt | model | parser

result = chain.invoke({"text" : docs[0].page_content})

print(result)
