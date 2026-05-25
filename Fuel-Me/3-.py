from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    temperature=0.0,

)

# STEP 1: Define your Pydantic Schema and create the Parser
class MovieInfo(BaseModel):
    title: str = Field(description="Name of the movie")
    year: int = Field(description="Release year of the movie")

parser = PydanticOutputParser(pydantic_object=MovieInfo)

# STEP 2: Create the PromptTemplate with partial_variables
template_string = """
Provide the details of a popular movie directed by {director}.

{format_instructions}
"""

prompt = PromptTemplate(
    template=template_string,
    input_variables=["director"], # Filled by the user dynamically at runtime
    partial_variables={"format_instructions": parser.get_format_instructions()} # Injected automatically!
)

# STEP 3: Construct the Pipeline using the pipe (|) syntax
chain = prompt | model | parser

# Execution: You only need to pass the 'director' now. 
# The pipeline handles the prompting, API call, and parsing automatically.
final_result = chain.invoke({"director": "Christopher Nolan"})

print(final_result.title) # Output: Inception
print(final_result.year)  # Output: 2010