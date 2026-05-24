from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence , RunnableParallel  , RunnablePassthrough

load_dotenv()


llm = HuggingFaceEndpoint(
    model = "google/gemma-2-2b-it",
    task = "text_generation"
)

model = ChatHuggingFace(llm = llm )



prompt = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=['topic'] 
)

prompt2 = PromptTemplate(
    template= "Explain the joke and how make sense on {text}",
    input_variables= ['text']
)

parser = StrOutputParser()

joke_generator_chain = RunnableSequence(prompt , model , parser)

parallel_chain = RunnableParallel({
    "joke" : RunnablePassthrough(),
    "explanation" : RunnableSequence(prompt2 , model , parser)   
})

final_chain = RunnableSequence(joke_generator_chain , parallel_chain)

result = final_chain.invoke({"topic" : "AI"})

print(result)

final_chain.get_graph().print_ascii()
