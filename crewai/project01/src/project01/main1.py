from crewai.flow.flow import Flow, listen, start
from dotenv import load_dotenv
from litellm import completion


class ExampleFlow(Flow):
    model = "gemini/gemini-1.5-flash"

    @start()
    def generate_city(self):
        print("Starting flow")
        # Each flow state automatically gets a unique ID
        print(f"Flow State ID: {self.state['id']}")

        response = completion(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": "Return the name of a  city in the Pakistan.",
                },
            ],
        )

        city = response["choices"][0]["message"]["content"]
        # Store the city in our state
        self.state["city"] = city
        print(f"Random City: {city}")

        return city

    @listen(generate_city)
    def generate_fun_fact(self, city):
        response = completion(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": f"Tell me only two fun fact about {city}",
                },
            ],
        )

        fun_fact = response["choices"][0]["message"]["content"]
        # Store the fun fact in our state
        self.state["fun_fact"] = fun_fact
        return fun_fact


def kickoff():
 flow = ExampleFlow()
 result = flow.kickoff()

 print(f"Generated fun fact: {result}")