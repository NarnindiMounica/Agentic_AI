from tavily import TavilyClient
from langchain_core.prompts import ChatPromptTemplate

class AINewsNode:

    def __init__(self, llm):
        self.llm = llm
        self.tavily = TavilyClient()
        #this is used to capture various steps in this file so that later can be used for steps show
        self.state={}

    def fetch_news(self, state:dict)->dict:
        """
        Docstring for fetch_news
        
        Fetch AI News based on the specified frequency

        Args:
        state(dict) : The state dictionary containing 'frequency'

        Returns:
        dict: updated state with 'news_data' key containing fetched news.

        """  
        


