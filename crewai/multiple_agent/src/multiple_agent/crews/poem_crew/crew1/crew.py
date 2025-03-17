from crewai import Crew,Agent,Process,Task # type: ignore
from crewai.project import CrewBase,task,agent,crew # type: ignore

@CrewBase
class DevCrew:
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

#Agent :1
    @agent
    def junior_python_developer(self) -> Agent:
        return Agent(
            config= self.agents_config["junior_python_developer"],
        )
    
#Agent :2    
    @agent
    def senior_python_developer(self) -> Agent:
        return Agent(
            config= self.agents_config["senior_python_developer"],
        )
    
    @task
    def write_code(self) -> Task:
        return Task(
            config= self.tasks_config["write_code"],
        )
    @task
    def review_code(self) -> Task:
        return Task(
            config= self.tasks_config["review_code"],
        )
    @crew
    def crew1(self) -> Crew:

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequence(
                verbode=True,
        )
        )

