from typing import Annotated

from typing_extensions import TypedDict
from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages

import os
from dotenv import load_dotenv

load_dotenv()
openaiAPIkey = os.getenv("OPENAI_API_KEY")

#First step 
class State(TypedDict):
    # Messages have the type "list". 
    # The `add_messages` function adds ne3 m4ssages to the list
    # (in this case, it appends messages to the list, rather than overwriting them)
    messages: Annotated[list, add_messages] 



"""
A StateGraph object defines the structure of our chatbot as a "state machine". We'll add nodes to represent the llm and
functions our chatbot can call and edges to specify how the bot should transition between these functions.
 - Passing on teh state class 
"""
graph_builder = StateGraph(State)

"""
Every node we define will receive the current State as input and return a value that updates that state.
Messages will be appended to the current list
"""

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=openaiAPIkey)

#Takes in teh current state as input and returns an updated messages list (updates state)
def chatbot(state: State):
    return {"messages": [llm.invoke(state["messages"])]}


# The first argument is the unique node name
# The second argument is the function or object that will be called whenever
# the node is used.
graph_builder.add_node("chatbot", chatbot)

#This tells our graph where to start its work each time we run it.
graph_builder.set_entry_point("chatbot")

#FINISH POINT
graph_builder.set_finish_point("chatbot")

#. To do so, call "compile()" on the graph builder. This creates a "CompiledGraph" we can use invoke on our state.
graph = graph_builder.compile()