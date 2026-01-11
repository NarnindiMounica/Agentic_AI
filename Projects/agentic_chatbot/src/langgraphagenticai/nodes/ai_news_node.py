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

    def summarize_news(self, state:dict)->dict:
        """
        Docstring for summarize_news
        
        Summarize the fetched news using an LLM

        Args:
            state(dict): the state dictionary containing "news_data"

        Returns:
        dict: updated state with "summary" key containing the summarized news.    

        """ 

        news_items = self.state['news_data']

        prompt_template =ChatPromptTemplate.from_messages(
            [
                ("system", """Summarize AI News articles into markdown format. For each item include:
                 -Date in **YYYY-MM-DD** format in IST Timezone
                 -Concise sentences summary from latest news
                 -Sort news by date wise (latest first)
                 -Source URL as link
                 Use format:
                 ### [Date]
                 - [Summary](URL)"""),
                 ("user", "Articles:\n{articles}")
                    
            ]

        )

        articles_str = "\n\n".join([
            f"Content: {item.get("content", '')}\n URL: {item.get("url", '')}\n Date: {item.get("published_date", "")}"
            for item in news_items
        ])

        response = self.llm.invoke(prompt_template.format(articles=articles_str))
        state['summary'] = response.content
        self.state['summary'] = state['summary']
        return self.state
    
    def save_news(self, state:dict)->dict:
        "This function saves the summarized news in local file"
        frequency = self.state['frequency']
        summary = self.state['summary']
        filename=f"./AINews/{frequency}_summary.md"
        with open(filename, "w") as file:
            file.write(f" #{frequency.capitalize()} AI News Summary\n\n")
            file.write(summary)
        self.state['filename'] = filename
        return self.state    


