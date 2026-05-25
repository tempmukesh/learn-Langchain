from pydantic import BaseModel , Field
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.runnables import RunnablePassthrough


load_dotenv()

model = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    temperature = 0.0
)

prompt1 = PromptTemplate(
    input_variables=['city'],
    template="Tell me the most famous landmark in {city}. Only give the name."
)

chain1 = prompt1 | model

prompt2 = PromptTemplate(
    input_variables=['landmark'],
    template="Give me one interesting fun fact about {landmark}. Keep it short."

)
chain2 = prompt2 | model 


final_chain = (
    {"landmark" : chain1} |
    RunnablePassthrough.assign(fact = chain2)
)

result = final_chain.invoke({"city" : "mumbai"})

clean_result = {
    "landmrk" :  result['landmark'].content,
    "fact" : result['fact'].content
}

print(clean_result)