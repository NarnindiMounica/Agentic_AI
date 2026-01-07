from langgraph.graph import StateGraph, START, END
from src.langgraphagenticai.states.state import State
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraphagenticai.tools.inbuilt_tools import InbuiltTools

class GraphBuilder:
    def __init__(self, model ):
        self.graph_builder = StateGraph(State)
        self.llm = model
        
    def basic_chatbot_build_graph(self):
        """
        Docstring for basic_chatbot_build_graph
        
        Builds a basic chatbot graph using Langgraph.
        This method initializes a chatbot node using the 'BasicChatbotNode' class
        and integrates it into the graph. The chatbot node is set as both the entry
        and exit point of the graph.

        """   
        self.basic_chatbot= BasicChatbotNode(self.llm)
        self.graph_builder.add_node("basic_chatbot_node", self.basic_chatbot.basic_chatbot_node ) 

        self.graph_builder.add_edge(START, "basic_chatbot_node")
        self.graph_builder.add_edge("basic_chatbot_node", END)
        return self.graph_builder
    
    def tools_chatbot_build_graph(self):
        """
        Docstring for tools_chatbot_build_graph
        
        Builds a chatbot graph which is bind with tools using Langgraph.
        This method defines a workflow of the graph for a chatbot which is bind with tools.

        """   
        self.basic_chatbot= BasicChatbotNode(self.llm)
        self.graph_builder.add_node("basic_chatbot_node", self.basic_chatbot.basic_chatbot_node ) 

        self.graph_builder.add_edge(START, "basic_chatbot_node")
        self.graph_builder.add_edge("basic_chatbot_node", END)
        return self.graph_builder

    def set_graph_builder(self, usecase):

        if usecase.lower()=="basic chatbot":
            graph_built = self.basic_chatbot_build_graph()
            graph = graph_built.compile()
            return graph
        
        if usecase.lower()=="chatbot with tools":
            graph_built = self.tools_chatbot_build_graph()
            graph = graph_built.compile()
            return graph

        
