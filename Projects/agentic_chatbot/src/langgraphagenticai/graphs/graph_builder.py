from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import tools_condition

from src.langgraphagenticai.states.state import State
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraphagenticai.tools.inbuilt_tools import InbuiltTools
from src.langgraphagenticai.nodes.ai_news_node import AINewsNode

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
        get_tools = InbuiltTools().get_inbuilt_tools()


        self.basic_chatbot= BasicChatbotNode(self.llm)
        self.graph_builder.add_node("tools_chatbot_node", self.basic_chatbot.tools_chatbot_node )
        self.graph_builder.add_node("tools", InbuiltTools().get_tool_node(tool=get_tools)) 

        self.graph_builder.add_edge(START, "tools_chatbot_node")
        self.graph_builder.add_conditional_edges("tools_chatbot_node", tools_condition)
        self.graph_builder.add_edge("tools", "tools_chatbot_node")
        self.graph_builder.add_edge("tools_chatbot_node", END)

        return self.graph_builder
    

    def ainews_bot_build_graph(self, llm):
        """
        Docstring for ainews_bot_build_graph
        
        Builds a graph which gets ainews from bind tools, summarize results and saves it locally using Langgraph.
        
        """ 
        ai_news_obj = AINewsNode(llm)
        self.graph_builder.add_node("fetch_news", ai_news_obj.fetch_news)
        self.graph_builder.add_node("summarize_news",ai_news_obj.summarize_news)
        self.graph_builder.add_node("saves_news",ai_news_obj.save_news)

        self.graph_builder.add_edge(START, "fetch_news")
        self.graph_builder.add_edge("fetch_news", "summarize_news")
        self.graph_builder.add_edge("summarize_news", "saves_news")
        self.graph_builder.add_edge("saves_news", END)
    
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
        
        if usecase.lower()=="ai news":
            graph_built = self.ainews_bot_build_graph()
            graph = graph_built.compile()
            return graph

        
