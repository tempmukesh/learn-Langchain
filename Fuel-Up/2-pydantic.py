from pydantic import BaseModel , Field
from typing import Optional , List
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    temperature = 0.0,
)


class ResumeData(BaseModel):
    name : str
    age : int = Field(gt = 18 , lt = 90 , description="age of the person")
    cgpa : float = Field(gt = 0 , le = 10 , default = 0.0 )
    past_companies : Optional[List[str]] = Field(default = ["fresher"] , description= "person where works in the past")


new_applicant_summary = """Johnathan "Jon" Miller, a 24-year-old recent graduate, secured his current position after demonstrating exceptional academic performance with a 3.85 CGPA in Computer Science from State University; before joining the team, he completed a rigorous six-month internship at TechNova Solutions, where he contributed to their cloud infrastructure projects."""

structured_model = model.with_structured_output(ResumeData)

result = structured_model.invoke(new_applicant_summary)

print("*" * 50 )
print(new_applicant_summary)
print("*" * 50 )
print(f"Name: {result.name}")
print(f"Age: {result.age}")
print(f"CGPA: {result.cgpa}")
print(f"Past Companies: {result.past_companies}")