from crewai import Agent,Task,Crew, Process,Flow
from crewai.project import CrewBase, agent, crew, task
from langchain.tools import YoutubeChannelSearchTool, YoutubeVideoSearchTool
from litellm import completion
from dotenv import load_dotenv

load_dotenv()


class YouTubeSearchAgent(Flow):
    def search(self):
      output = completion(
          model="gemini/gemini-2.0-flash",
          messages=[
              {"role": "YouTube Search Specialist", "content": "Search for YouTube channels related to 'AI tutorials'. Provide a list of channel names and links."}
          ],
      )
      final_output = output.choices[0].message
      return final_output
    
    
youtube_search_agent = Agent(
    role='YouTube Search Specialist',
    goal='Search for YouTube channels and videos based on user queries.',
    backstory='You are an expert in navigating YouTube\'s vast library. You can efficiently find channels and videos based on keywords and topics.',
    verbose=True,
    allow_delegation=False,
    tools=[YoutubeChannelSearchTool(), YoutubeVideoSearchTool()],
)
# from crewai import Task

def create_youtube_channel_search_task(query):
    task = Task(
        description=f'Search for YouTube channels related to "{query}". Provide a list of channel names and links.',
        agent=youtube_search_agent,
    )
    return task

def create_youtube_video_search_task(query):
    task = Task(
        description=f'Search for YouTube videos related to "{query}". Provide a list of video titles and links.',
        agent=youtube_search_agent,
    )
    return task
# from crewai import Crew, Process

# Example queries
channel_query = "AI tutorials"
video_query = "LangChain explained"

# Create tasks
channel_search_task = create_youtube_channel_search_task(channel_query)
video_search_task = create_youtube_video_search_task(video_query)

# Create crew
youtube_crew = Crew(
    agents=[youtube_search_agent],
    tasks=[channel_search_task, video_search_task],
    verbose=2,
    process=Process.sequential,
)

# Run crew
def run_crew():
 result = youtube_search_agent()
 result.kickoff()
