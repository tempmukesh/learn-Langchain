# first lookup on Webbaseloader.py file of last line 

from langchain_community.document_loaders import WebBaseLoader
from langchain_huggingface import HuggingFaceEndpoint , ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# load the page and save in docs 
url = "https://www.flipkart.com/apple-macbook-air-m4-16-gb-256-gb-ssd-macos-sequoia-mc6t4hn-a/p/itm7c1831ce25509"
loader = WebBaseLoader(url)
docs = loader.load()

llm = HuggingFaceEndpoint(
    model = "deepseek-ai/DeepSeek-V3.2",
    task = "text_generation"
)

model = ChatHuggingFace(llm = llm )

parser = StrOutputParser()

prompt = PromptTemplate(
    template = "Answer of the following \n {question} from the following - \n {text}",
    input_variables=['question' , 'text']
)

chain = prompt | model | parser

question  = """
1. What is the screen size and resolution of the Apple MacBook Air M4 listed on Flipkart?  
2. Which processor powers this MacBook Air model, and how many cores does it have?  
3. What is the battery backup duration mentioned for the device?  
4. What are the available offers and discounts for this product on Flipkart?  
5. What warranty coverage is provided with the Apple MacBook Air M4?  """

result = chain.invoke({"question" : question , "text" : docs[0].page_content})


print(result)