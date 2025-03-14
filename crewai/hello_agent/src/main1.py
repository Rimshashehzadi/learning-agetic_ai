from crewai.flow.flow import Flow,start,listen
from litellm import completion



class LitellmFlow(Flow):
    def start_function(self):
        output = completion(
            messages=[
                {
                    "role":"user",
                    "content":"Who is the president of the United States?"
                }
            ]
        )
       
       

    def