from langchain_huggingface import HuggingFaceEndpoint , ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    model = "deepseek-ai/DeepSeek-V3.2",
    task = "text_generation" 
)

model = ChatHuggingFace(llm = llm )


template = PromptTemplate(
    template= "Suggest a catchy blog title about {topic}",
    input_variables= ['topic']
)

format_prompt = template.format(topic = "Ai engineer")

result = model.invoke(format_prompt)

print(result)