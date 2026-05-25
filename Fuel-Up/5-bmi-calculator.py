from langgraph.graph import StateGraph , START , END
from typing import TypedDict
from IPython.display import Image

# Step 1 define the state using typedict 
class BMIstate(TypedDict):

    height_m : float
    weight_kg : float

    bmi : float


def calculate_bmi(state : BMIstate ) -> BMIstate:
    weight = state['weight_kg']
    height = state['height_m']

    # calculate bmi
    bmi = weight / (height ** 2)

    state['bmi'] = bmi
    return state


# Step 2 : define the graph 
graph = StateGraph(BMIstate)

# Step 3 :  add nodes to your graph 
graph.add_node("calculate_bmi" , calculate_bmi)


# Step 4 :  add edge to your graph 
graph.add_edge(START , "calculate_bmi")
graph.add_edge("calculate_bmi" , END)

# Step 5 : Compile the graph 
workflow = graph.compile()

output = workflow.invoke({
    "height_m" : 1.60,
    "weight_kg" : 55,
    "bmi" : 0
})

print(output)