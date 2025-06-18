
# def main():
#     print("Hello from basic-agent!")


# if __name__ == "__main__":
#     main()
import os
# os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
# import tensorflow as tf
import asyncio
from openai import AsyncOpenAI
from agents import Agent, Runner, function_tool, OpenAIChatCompletionsModel, set_tracing_disabled
from dotenv import load_dotenv

load_dotenv()
gemini_api_key = "AIzaSyAGfLGVNjMFg5cQFs1XFD-yIhg--TKHbHY"
client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
MODEL = "gemini-1.5-turbo"  # or "gemini-1.5-turbo-16k"

set_tracing_disabled(disabled=True)

@function_tool
def get_weather(city: str) -> str:
    print(f' [debug] getting weather for {city} ')
    return f"The weather in {city} is sunny with a high of 75°F."

def main(model: str, api_key: str):
    agent = Agent(
        name="Assistant",
        instructions="You only respond in haikus.",
        model=OpenAIChatCompletionsModel(model=model, openai_client=client),
    )
    result = Runner.run_sync(
        agent,
        "what is the weather of Lahore?",
    )
    print(result.final_output)

main(model=MODEL, api_key=gemini_api_key)