import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage

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
            response = graph.invoke({"messages": user_message})
            print(response)

            for message in response['messages']:
                if type(message)==HumanMessage:
                    with st.chat_message("user"):
                        st.write(message.content)
                elif type(message)==ToolMessage:        
                    with st.chat_message("tool"): 
                         st.write("Tool Call Starts")
                         st.write(message.content) 
                         st.write("Tool Call Ends") 
                else:         
                    with st.chat_message("assistant"):
                        st.success(message.content)         
                

             
              



              