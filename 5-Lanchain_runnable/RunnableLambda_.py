from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda , RunnableSequence , RunnablePassthrough , RunnableParallel

load_dotenv()


llm = HuggingFaceEndpoint(
    model = "google/gemma-2-2b-it",
    task = "text_generation"
)

model = ChatHuggingFace(llm = llm )

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template= "Write a joke about {topic}",
    input_variables=['topic']
)

def wcount(text):
    return len(text.split())


Runnable_first = RunnableSequence(prompt1 , model , parser)

# parallel chain 

parallel_chain = RunnableParallel({
    "joke" : RunnablePassthrough(),
    "count_word" : RunnableLambda(wcount)
})

final_chain = RunnableSequence(Runnable_first , parallel_chain)

result = final_chain.invoke({"topic" : "AI"})

decort = """{} \n word_count - {}""".format(result['joke'] , result['count_word'])

print(decort)

final_chain.get_graph().print_ascii()