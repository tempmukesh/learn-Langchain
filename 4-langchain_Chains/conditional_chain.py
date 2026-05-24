from langchain_huggingface import HuggingFaceEndpoint , ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel  , RunnableBranch , RunnableLambda
from pydantic import BaseModel , Field
from langchain_core.output_parsers import StrOutputParser , PydanticOutputParser
from typing import Literal

load_dotenv()


llm = HuggingFaceEndpoint(
    model = "deepseek-ai/DeepSeek-V3.2",
    task = "text_generation"
)

model = ChatHuggingFace(llm = llm )

parser = StrOutputParser()

class Feedback(BaseModel):
    
    sentiment : Literal['positive' , "negative"] = Field(description="Give the sentiment of the following text into positive or negative")
    

parser2 = PydanticOutputParser(pydantic_object=Feedback)


prompt = PromptTemplate(
    template="Classify the sentiment of the following text into positive or negative \n {feedback} \n{format_instruction}",
    input_variables=['deepseek-ai/DeepSeek-V3.2'],
    partial_variables={"format_instruction" : parser2.get_format_instructions()}
)

classifier_chain = prompt | model | parser2

prompt2 = PromptTemplate(
    template= "Write an appropriate response to this positive feedback \n {feedback}",
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template= "Write an appropriate response to this negative feedback \n {feedback}",
    input_variables=['feedback']
)


branch = RunnableBranch(
    # (condition , chain)
    (lambda x: x.sentiment == "positive"  , prompt2 | model | parser),
    (lambda x :x.sentiment == "negative" , prompt2 | model |parser ),
    RunnableLambda(lambda x : "couldn't find sentiment")
)

chain = classifier_chain | branch

result = chain.invoke({"feedback"  : " The work exceeded expectations in both quality and timing."})

print(result)

chain.get_graph().print_ascii()
