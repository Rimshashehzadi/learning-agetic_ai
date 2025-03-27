from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task



@CrewBase
class SearcherCrew:
    
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

#Agent NO.1
   
    @agent
    def gmail_searcher(self) -> Agent:
        return Agent(
            config=self.agents_config["gmail_searcher"],
        )
    
#Agent NO.2
   
    @agent
    def email_analyzer(self) -> Agent:
        return Agent(
            config=self.agents_config["email_analyzer"],
        )
    
#Agent NO.3
   
    @agent
    def candidate_evaluator(self) -> Agent:
        return Agent(
            config=self.agents_config["candidate_evaluator"],
             verbose=True,
             allow_delegation=True,
        )
    
    #Agent NO.4
   
    @agent
    def meeting_scheduler(self) -> Agent:
        return Agent(
            config=self.agents_config["meeting_scheduler"],
             verbose=True,
             allow_delegation=True,
        )
    
     #Agent NO.5
   
    @agent
    def notifier(self) -> Agent:
        return Agent(
            config=self.agents_config["notifier"],
            
        )
#Task NO.1
    
    @task
    def gmail_search_task(self) -> Task:
        return Task(
            config=self.tasks_config["gmail_search_task"],
        )
    
    #Task NO.2
    
    @task
    def email_extraction_task(self) -> Task:
        return Task(
            config=self.tasks_config["email_extraction_task"],
        )

#Task NO.3
    
    @task
    def candidate_evaluation_task(self) -> Task:
        return Task(
            config=self.tasks_config["candidate_evaluation_task"],
            
        )

#Task NO.4
    
    @task
    def meeting_scheduling_task(self) -> Task:
        return Task(
            config=self.tasks_config["meeting_scheduling_task"],
            
        )
    
#Task NO.5
    
    @task
    def notification_task(self) -> Task:
        return Task(
            config=self.tasks_config["notification_task"],
            
        )    

    @crew
    def crew(self) -> Crew:
        """Creates the Research Crew"""
        

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
