from src.states.state import BlogState

class BlogNode:
    def __init__(self, llm):
        self.llm = llm

    def title_creation(self, state:BlogState):
        "create the title for the blog"

        if "topic" in state or state['topic']:

            prompt="""
                    You are an expert blog content writer. Use Markdown formatting.
                    Generate a blog title for the {topic}, This title should be creative and SEO friendly
                    
                    """
            
            system_message=prompt.format(topic=state['topic'])

            response = self.llm.invoke(system_message)

            return {"blog":{"title":response.content}}
        

    def content_generation(self, state:BlogState):
            """
            Docstring for content_generation
            
            this method is used to generate the content for the specified topic

            """
            if "topic" in state or state['topic']:
                prompt = """
                        You are an expert blog writer, Use markdown formatting
                        and generate a detailed blog content with detailed
                         breakdown for the topic {topic}"""
                system_prompt = prompt.format(topic=state['topic'])

                response = self.llm.invoke(system_prompt)
            return {"blog": {"title": state['blog']['title'], "content":response.content}}
    
    def language_translation(self, state:BlogState):
         """
            Docstring for language_translation
            
            this method is used to translate the generated content for the specified topic

            """
         if "topic" in state and "language" in state:
              prompt = """
                        You are an expert blog writer, Use markdown formatting
                        and generate a detailed blog content with detailed
                        breakdown for the topic {topic}in given language {language}"""
              system_prompt = prompt.format(language=state['language'], content=state['topic'])

              response = self.llm.invoke(system_prompt)
              return {"blog": {"content": response.content}}
              

            


