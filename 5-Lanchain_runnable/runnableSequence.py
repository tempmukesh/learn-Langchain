from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence


load_dotenv()



prompt = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=['topic'] 
)

prompt2 = PromptTemplate(
    template= "Explain the joke and how make sense on {text}",
    input_variables= ['text']
)

parser = StrOutputParser()

llm = HuggingFaceEndpoint(
    model = "deepseek-ai/DeepSeek-V3.2",
    task = "text_generation"
)

model = ChatHuggingFace(llm = llm )

chain = RunnableSequence(
    prompt  , model , parser 
)



result = chain.invoke({"topic"  : "AI"})

print(result)

chain.get_graph().print_ascii()
