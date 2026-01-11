from tavily import TavilyClient
from langchain_core.prompts import ChatPromptTemplate

#https://docs.tavily.com/sdk/python/reference

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

        frequency = state['messages'][0].content.lower()
        self.state['frequency']= frequency
        time_range_map= {"day":"d", "week":"w", "month": "m", "year":"y"}
        days_map= {"day": 1, "week": 7, "month": 30, "year": 365}

        response = self.tavily.search(query="Get Latest News in the field of Artificial Intelligence from India and globally",
                                      topic="news",
                                      time_range=time_range_map[frequency],
                                      max_results=3,
                                      include_answer="advanced",
                                      days=days_map[frequency])
        
        state['news_data'] = response.get("results", [])
        self.state['news_data'] = state['news_data']  
        return state      


