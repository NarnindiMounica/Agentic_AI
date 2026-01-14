from langgraph.graph import StateGraph, START, END

from src.states.state import BlogState
from src.nodes.blog_node import BlogNode

from src.llms.groq_llm import GroqLLM


class GraphBuilder:
    def __init__(self, llm):
        self.llm = llm
        self.graph = StateGraph(BlogState)
        self.blog_node_obj = BlogNode(self.llm)

    def build_topic_graph(self):
        "Build graph workflow based on topic"

        self.graph.add_node("title_creation",self.blog_node_obj.title_creation)
        self.graph.add_node("content_generation",self.blog_node_obj.content_generation)

        self.graph.add_edge(START, "title_creation")
        self.graph.add_edge("title_creation", "content_generation")
        self.graph.add_edge("content_generation", END)

        return self.graph
    
    def build_language_graph(self):
        "Build graph for blog generation with topic and language"

        self.graph.add_node("title_creation",self.blog_node_obj.title_creation)
        self.graph.add_node("content_generation",self.blog_node_obj.content_generation)
        self.graph.add_node("language_router", self.blog_node_obj.)
        self.graph.add_node("hindi_translation", self.blog_node_obj.)
        self.graph.add_node("telugu_translation", self.blog_node_obj.)


        self.graph.add_edge(START, "title_creation")
        self.graph.add_edge("title_creation", "content_generation")
        self.graph.add_edge("content_generation", "language_router")
        self.graph.add_conditional_edges("language_router", language_decider, 
                                         {"hindi": "hindi_translation", 
                                          "telugu": "telugu_translation"})


        return self.graph


    
    def setup_graph(self, usecase):
        if usecase=="topic":
            graph_builder = self.build_topic_graph()
            return graph_builder.compile()
        
        elif usecase=="language":
            graph_builder = self.build_language_graph()
            return graph_builder.compile()



#below code is for the langsmith langgraph studio
llm = GroqLLM().get_groq_llm()

#get the graph

graph_builder = GraphBuilder(llm)

graph=graph_builder.build_topic_graph().compile()