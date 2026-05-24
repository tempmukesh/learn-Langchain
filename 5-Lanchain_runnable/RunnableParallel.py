from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence , RunnableParallel

load_dotenv()


llm = HuggingFaceEndpoint(
    model = "google/gemma-2-2b-it",
    task = "text_generation"
)

# I am taking at that time one model but If you can then select the best model individualy 
model = ChatHuggingFace(llm = llm )

prompt1 = PromptTemplate(
    template= "Generate a tweet about {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Generate a LinkedIn post about {topic}",
    input_variables=['topic']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "tweet"  : RunnableSequence(prompt1 , model , parser),
    "LinkedIN"  :RunnableSequence(prompt2 , model , parser) 
})


result = parallel_chain.invoke({"topic" : "AI"})

print(result)

parallel_chain.get_graph().print_ascii()