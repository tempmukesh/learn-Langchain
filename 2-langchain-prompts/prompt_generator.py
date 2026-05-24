from langchain_core.prompts import PromptTemplate


# template
template = PromptTemplate(
    template="""
Please summarize the research paper titled {paper_input} with the following specifications:

Explanation Style: {style_input}
Explanation Length: {length_input}

Include relevant mathematical equations if present in the paper. Explain the mathematical concepts using simple intuitive code snippets where applicable. Also add analogy that is relatable. If any piece of information is not available, instead of hallucinating, simply put "Insufficient information available".
Also, lastly ensure the summary is clear, accurate and aligned with the provided style and length.
""",
    input_variables=["paper_input", "style_input", "length_input"],
)


template.save("template.json")