import os
import streamlit as st

from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self, user_controls_input):
        self.user_controls_input= user_controls_input

    def get_llm_model(self):
        try:
            groq_api_key = self.user_controls_input['GROQ_API_KEY']
            selected_groq_model= self.user_controls_input['selected_groq_model']
            if groq_api_key == "" and os.environ["GROQ_API_KEY"] == "":
                st.error("Please enter the Groq API Key") 

            llm = ChatGroq(model=selected_groq_model, groq_api_key=groq_api_key)

        except Exception as e:
            raise ValueError(f"Error occurred with exception: {e}")  

        return llm  

    def get_tools_bind_llm(self, tools:list):

        base_llm = self.get_llm_model() 

        try:
            tools_llm = base_llm.bind_tools(tools) 

        except Exception as e:

            raise ValueError(f"Error occurred while binding tools: {e}") 
        
        return tools_llm

