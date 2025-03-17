from crewai.flow import Flow,start,listen # type: ignore
from multiple_agent.crews.poem_crew.crew1.crew import DevCrew


class DevFlow(Flow):
    @start
    def run_dev_crew(self):
        output = DevCrew().crew1().kickoff(
            inputs={
                "problem":"write python code with addition two number",
            }
        )
        return output.raw
    
def kickoff():
    dev_fllow = DevFlow()
    result= dev_fllow.kickoff()
    print(result)   