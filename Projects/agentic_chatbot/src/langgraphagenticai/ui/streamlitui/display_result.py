import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

import json

class DisplayResultStreamlit:
    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display_result_on_ui(self):
        usecase = self.usecase
        graph = self.graph
        user_message = self.user_message
        if usecase.lower()=="basic chatbot":
            for event in graph.stream({"messages": user_message}, stream_mode="values"):
                print(event.values())
            with st.chat_message("user"):
                    st.write(user_message)
            with st.chat_message("assistant"):  
                    st.write(event['messages'][-1].content)  

        else:
             for event in graph.stream({"messages": user_message}, stream_mode="values"):
                print(event.values())
                st.write(event.values())

             
              



              