from pydantic import BaseModel , EmailStr , Field
from typing import Optional 

class Student(BaseModel):
    
    name : str = "nitish"
    age : Optional[int] = None
    email : EmailStr
    cgpa : float = Field(gt = 0 , lt = 10 , default = 5 , description="a decimal value representing the cgpa of the")

new_student = {"name" : "me" , "age" : 34 , "email" : "abc@gmail.com"}

student = Student(**new_student)

print(student)

# dict conversion 
student_dict = dict(student)

student_json = student.model_dump_json()

print(student_json)