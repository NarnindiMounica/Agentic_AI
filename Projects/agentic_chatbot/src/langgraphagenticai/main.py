import streamlit as st
import os

from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.llms.groqllm import GroqLLM
from src.langgraphagenticai.graphs.graph_builder import GraphBuilder
from src.langgraphagenticai.tools.inbuilt_tools import InbuiltTools
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit

def load_langgraph_agenticai_app():
    """
    Docstring for load_langgraph_agenticai_app:

    Loads and runs the Langgraph agenticai application with streamlit ui.
    This function initializes the UI, handles user input, configures the LLM Model, 
    sets up the graph based on the selected use case, and displays the output while
    implementing exception handling for robustness.

    """

    #load UI
    ui=LoadStreamlitUI()
    user_input=ui.load_streamlit_ui()
    

    if not user_input:
        st.error("Error: Failed to load user input from the UI")
        return
    
    user_message = st.chat_input("Enter your message: ")

    if user_message:
        try:
            obj_groqllm = GroqLLM(user_controls_input=user_input)

            usecase = user_input['selected_usecase']
            
            if not usecase:
                st.error("Error: No usecase selected")
                return 
            
            if usecase.lower()=="basic chatbot":

                #configuring the LLM
                model = obj_groqllm.get_llm_model()

                if not model:
                    st.error("Error: LLM model could not be initialized")
                    return
            
            
                obj_graph_builder = GraphBuilder(model=model)

                try:

                    graph = obj_graph_builder.set_graph_builder(usecase=usecase)
                

                except Exception as e:
                    print(f"Error occurred while setting up graph: {e}")
                    return
                
            elif usecase.lower()=="chatbot with tools":
                obj_inbuilt_tools = InbuiltTools()
                user_tools = obj_inbuilt_tools.get_inbuilt_tools()

                #configuring the LLM
                model = obj_groqllm.get_tools_bind_llm(tools=user_tools)

                if not model:
                    st.error("Error: LLM model could not be initialized")
                    return
            
            
                obj_graph_builder = GraphBuilder(model=model)

                try:

                    graph = obj_graph_builder.set_graph_builder(usecase=usecase)
                

                except Exception as e:
                    print(f"Error occurred while setting up graph: {e}")
                    return


            
            try:
                DisplayResultStreamlit(usecase, graph, user_message).display_result_on_ui()

            except Exception as e:
                print(f"Error occurred while displaying results on UI: {e}")
                return 

            else:
                  



        except Exception as e:
            print(f"Error occurred: {e}") 
            return   



