from crewai.flow.flow import Flow, start, listen
from litellm import completion
from dotenv import load_dotenv


load_dotenv()


class TopicOutlineFlow(Flow):
    model = 'gemini/gemini-1.5-flash'

    @start()
    def generate_topic(self):
        # Prompt the LLM to generate the a blog topic
        response = completion(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": "Generate a most trending topic only  name in the world of AI in 2025."
                }
            ]
        )
        topic = response["choices"][0]["message"]["content"].strip()
        print(f"Generated Topic: {topic}")
        return topic

    @listen(generate_topic)
    def generate_outline(self, topic):
        # Now chain the output by using the topic in a follow-up prompt.
        response = completion(
            model=self.model,
            messages=[{
                "role": "user",
                "content": f"Based on the topic '{topic}', create a  five line on it."
            }]
        )
        outline = response["choices"][0]["message"]["content"].strip()
        print("Generated Outline:")
        print(outline)
        return outline


def kickoff():
    prompt_chaining_flow = TopicOutlineFlow()
    final_outline = prompt_chaining_flow.kickoff()
    print("Final Output:")
    print(final_outline)


def plot():
    prompt_chaining_flow = TopicOutlineFlow()
    prompt_chaining_flow.plot()


