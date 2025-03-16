from crewai.flow.flow import Flow,start,listen
from litellm import completion



class LitellmFlow(Flow):
    @start()
    def start_function(self):
        output = completion(
            model="gemini/gemini-2.0-flash",
            messages=[
                {
                    "role":"user",
                    "content":"Who is the President of United State?"
                }
            ]
        )
        final=output["choices"][0]["message"]["content"]
        print(final)
       
       

def run_flow():
    obj = LitellmFlow()
    obj.kickoff()
    