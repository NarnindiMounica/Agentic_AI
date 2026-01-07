from langchain_tavily import TavilySearch
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

from langgraph.prebuilt import ToolNode


class InbuiltTools:

    def __init__(self):
        pass

    def get_inbuilt_tools(self):

        "this function returns a list of defined inbuilt tools"
        
        tavily_tool = TavilySearch(max_results=2)
        wikipedia_tool = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

        given_tools = [tavily_tool, wikipedia_tool]

        return given_tools
    
    def get_tool_node(self, tool:list):

        "This function creates a tool node with the list of given tools"

        return ToolNode(tool)




