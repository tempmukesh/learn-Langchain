from typing import TypedDict
from langgraph.graph import StateGraph, START, END


# Shared State
class State(TypedDict):
    raw_data: str
    formatted_data: dict


# Node 1
def extract_data(state: State) -> State:
    
    # Raw input
    text = state["raw_data"]

    # Mock extraction process
    cleaned_text = text.replace("This is ", "")

    # Update state
    state["raw_data"] = cleaned_text

    return state


# Node 2
def format_data(state: State) -> State:

    # Processed text
    text = state["raw_data"]

    # Mock formatting
    state["formatted_data"] = {
        "source": "website",
        "content": text
    }

    return state


# Create Graph
graph = StateGraph(State)


# Add Nodes
graph.add_node("extract_data", extract_data)
graph.add_node("format_data", format_data)


# Add Edges
graph.add_edge(START, "extract_data")
graph.add_edge("extract_data", "format_data")
graph.add_edge("format_data", END)


# Compile Graph
app = graph.compile()


# Run Graph
result = app.invoke({
    "raw_data": "This is raw text from a website",
    "formatted_data": {}
})

print(result)