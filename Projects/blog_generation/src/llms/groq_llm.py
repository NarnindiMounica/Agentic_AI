import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self):
        load_dotenv()

    def get_groq_llm(self):
        
        try:
            os.environ['GROQ_API_KEY']=groq_api_key=os.getenv("GROQ_API_KEY")  

            model = ChatGroq(api_key=groq_api_key, model="llama-3.1-8b-instant") 
             
        except Exception as e:
            print(f"Exception occurred while loading groq model: {e}") 
            return    

        return model