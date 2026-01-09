import streamlit as st
import os 

from src.langgraphagenticai.ui.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config=Config()
        self.user_controls={}

    def load_streamlit_ui(self):
        st.set_page_config(page_title="🤖 " + self.config.get_page_title(), layout="wide")
        st.header("🤖 "+ self.config.get_page_title())

        with st.sidebar:
            #get options from config
            llm_options= self.config.get_llm_options()
            usecase_options= self.config.get_usecase_options()

            #LLM Selection
            self.user_controls['selected_llm'] = st.selectbox("Selected LLM", llm_options)

            if self.user_controls['selected_llm'].lower() =="groq":
                #Model selection
                model_options= self.config.get_groq_model_options()
                self.user_controls['selected_groq_model'] = st.selectbox("Select Groq Model", model_options)
                self.user_controls['GROQ_API_KEY'] = st.session_state["GROQ_API_KEY"]=st.text_input("API KEY", type="password")

                if not self.user_controls['GROQ_API_KEY'] :
                    st.warning("⚠️ Please enter your groq api key to proceed..")

            #usecase selection
            self.user_controls['selected_usecase']=st.selectbox("Select Usecase", usecase_options)
            

            if self.user_controls['selected_usecase'].lower() in [ "chatbot with tools" , "ai news"]:
                
                os.environ['TAVILY_API_KEY']=self.user_controls['TAVILY_API_KEY']=st.session_state['TAVILY_API_KEY']=st.text_input("Enter you Tavily API Key", type="password")

                if not self.user_controls['TAVILY_API_KEY'] :
                    st.warning("⚠️ Please enter your tavily api key to proceed..")

            if self.user_controls['selected_usecase'].lower() == "ai news":

                st.subheader("📰🔎📬 AI News Fetch")

                self.user_controls['selected_time_range']=st.session_state['time_range']=st.selectbox("📅 Time Range", ['day', 'week', 'month', 'year'])

                st.button("🔎 Fetch News")
                
                     

        return self.user_controls            