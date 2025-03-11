from crewai.flow.flow import Flow,start,listen
import time

class SimpleFlow(Flow):

    @start()
    def start(self):
        print("Starting the flow")
        time.sleep(2)

    @listen(start)
    def step1(self):
        print("Step 1...")
        time.sleep(2)

    @listen(step1)
    def step2(self):
        print("Step 2....") 
        time.sleep(2)  

    @listen(step2)
    def step3(self):
        print("Step 3...")


def kickoff():
    output = SimpleFlow()
    output.kickoff()    