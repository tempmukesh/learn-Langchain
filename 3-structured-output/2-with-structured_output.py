from langchain_openai import ChatOpenAI
from typing import TypedDict , Annotated
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model = "...",
    temperature = 0.0
)

class Review(TypedDict):

    summary : Annotated[str ," a brief summary of the review"] 
    sentiment : Annotated[str , "return sentiment of the review either negative , positive or neutral"]


paragraph = """Structured output allows agents to return data in a specific, predictable format. Instead of parsing natural language responses, you get structured data in the form of JSON objects, Pydantic models, or dataclasses that your application can use directly."""

structured_model = model.with_structured_output(Review)

result = structured_model.invoke(paragraph)

print(result['summary'])

print(result['sentiment'])