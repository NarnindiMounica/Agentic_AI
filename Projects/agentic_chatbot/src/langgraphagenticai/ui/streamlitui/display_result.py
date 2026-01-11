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

        elif usecase.lower()=="chatbot with tools":
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

        else:
             frequency = self.user_message
             with st.spinner("Fetching and summarizing news...⏳") :
                  result = graph.invoke({"messages": frequency})
                  try:
                       #read the markdown file
                       AI_News_Path = f"./AINews/{frequency.lower()}_summary.md"
                       with open(AI_News_Path, "r") as file:
                            markdown_content = file.read() 

                        #display the markdown content in streamlit
                       st.markdown(markdown_content, unsafe_allow_html=True)
                  except FileNotFoundError: 
                       st.error(f"News not generated or file not found: {AI_News_Path}")
                  except Exception as e:
                       st.error(f"an error occurred: {str(e)}")   
                         
                                                
                

             
              



              