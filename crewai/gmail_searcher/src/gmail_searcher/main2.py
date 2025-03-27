from crewai.flow import Flow,start,listen
from gmail_searcher.crews.mail_searcher.searcher_crew import SearcherCrew


class EmailFlow(Flow):
    @start()
    def run_email_crew(self):
        output = SearcherCrew().crew().kickoff(
             inputs ={
                  "email_id": "email search analyze evaluate candidate and scheduel the meeting with candidate and then notify from this  email id rimshashehzadi79@gmail.com"
        }
        )
        return output.raw
    
def kickoff():
    email_flow = EmailFlow()
    result = email_flow.kickoff()
    print(result)