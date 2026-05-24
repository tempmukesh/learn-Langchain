from langchain_huggingface import HuggingFaceEndpoint , ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

template = PromptTemplate(
    template="Write the most five interesting facts about {topic}",
    input_variables=['topic']
)

llm = HuggingFaceEndpoint(
    model = "google/gemma-2-2b-it",
    task = "text_generation"
)

model = ChatHuggingFace(llm = llm )

parser = StrOutputParser()

# template -> model -> parser -> output print 
chains = template | model | parser
 

result = chains.invoke({"topic" : "man"})

print(result)

chains.get_graph().print_ascii()