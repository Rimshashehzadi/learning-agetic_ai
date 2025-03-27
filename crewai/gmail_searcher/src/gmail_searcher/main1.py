from crewai.flow import Flow,start,listen
from gmail_searcher.crews.dev_crew.dev_crew import DevCrew


class DevFlow(Flow):
    @start()
    def run_dev_crew(self):
        output = DevCrew().crew().kickoff(
             inputs ={
                  "problem": "write python code for square two numbers"
        }
        )
        return output.raw
    
def kickoff():
    dev_flow = DevFlow()
    result = dev_flow.kickoff()
    print(result)
       
       
          