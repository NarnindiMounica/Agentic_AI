from typing_extensions import TypedDict
from typing import Annotated, List
from langgraph.graph.message import add_messages

class State(TypedDict):
    "represents the structure of the state used in the graph"
    messages: Annotated[List, add_messages]

