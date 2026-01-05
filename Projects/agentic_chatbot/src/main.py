import streamlit as st

from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI

def load_langgraph_agenticai_app():
    """
    Docstring for load_langgraph_agenticai_app:

    Loads and runs the Langgraph agenticai application with streamlit ui.
    This function initializes the UI, handles user input, configures the LLM Model, 
    sets up the graph based on the selected use case, and displays the output while
    implementing exception handling for robustness.
    
    """