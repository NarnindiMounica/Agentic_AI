import os
import streamlit as st

from src.langgraphagenticai.llms.groqllm import GroqLLM
from src.langgraphagenticai.states.state import State

class BasicChatbotNode:

    def __init__(self, model):
        self.llm =model

    def basic_chatbot_node(self, state:State)->dict:
        """
        Docstring for basic_chatbot_node
        
        Process the input state and generates a chatbot response
        """

        response = self.llm.invoke(state['messages']) 

        return {"messages": response}

    def tools_chatbot_node(self, state:State)->dict:
        """
        Docstring for tools_chatbot_node
        
        Process the input state and generates a chatbot response considering the tools bind to the model
        """

        response = self.llm.invoke(state['messages']) 

        return {"messages": "Tools Integration: " + response.content}  