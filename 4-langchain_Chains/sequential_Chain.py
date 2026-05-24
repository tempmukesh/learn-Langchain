from langchain_huggingface import HuggingFaceEndpoint , ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()


llm = HuggingFaceEndpoint(
    model = "google/gemma-2-2b-it",
    task = "text_generation"
)

model = ChatHuggingFace(llm = llm )


prompt1 = PromptTemplate(
    template="Generate a detailed report on this {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Generate a 5 pointer summurary from the following text \n {text}",
    input_variables=['text']
)

parser = StrOutputParser()

# chains formation 
chains = prompt1 | model | parser | prompt2 | model | parser

result = chains.invoke({"topic" : "Unemployement in india"})


print(result)

chains.get_graph().print_ascii()

