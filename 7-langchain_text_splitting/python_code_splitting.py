from langchain_text_splitters import RecursiveCharacterTextSplitter , Language


text = """
class Student:
    # Constructor method to initialize object attributes
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

    # Method to display student details
    def display_info(self):
        print(f"Name: {self.name}, Roll Number: {self.roll_number}")


# Creating an object of the class
student1 = Student("Mukesh", 101)

# Calling the method using the object
student1.display_info()
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    chunk_size = 370 , 
    chunk_overlap = 0 , 
    language= Language.PYTHON
)


chunks = splitter.split_text(text)


print(len(chunks))
for i, chunk in enumerate(chunks):
    print(f"Chunk {i}:\n{chunk}\n")