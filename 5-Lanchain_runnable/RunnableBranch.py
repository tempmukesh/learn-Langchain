from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableSequence ,  RunnablePassthrough
 

load_dotenv()

llm = HuggingFaceEndpoint(
    model = "google/gemma-2-2b-it",
    task = "text_generation"
)

model = ChatHuggingFace(llm = llm )

parser  = StrOutputParser()

prompt = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Summarize the following text \n {text}",
    input_variables=['text']
)

chain_first = prompt | model | parser 

# """" -------syntax----------------------
# RunnableBranch(
#      (condition , runnable_case),
#      default    
# )
# -------syntax----------------------"""

branch_chain = RunnableBranch(
    (lambda x :  len(x.split())> 100 , RunnableSequence(prompt2 , model , parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(chain_first , branch_chain)

print(final_chain.invoke({"topic"  :  "Russia vs Ukraine"}))

final_chain.get_graph().print_ascii()