import os
from dotenv import load_dotenv
import chainlit as cl
from agents import Agent, RunConfig, Runner, AsyncOpenAI, OpenAIChatCompletionsModel

# Load the environment variables from the .env file
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

# async def start():
    #Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
        api_key=gemini_api_key,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    )

model = OpenAIChatCompletionsModel(
        model="gemini-2.0-flash",
        openai_client=external_client
    )

config = RunConfig(
        model=model,
        model_provider=external_client,
        tracing_disabled=True
    )

agent = Agent(
        instructions="you are a helpful assistant that can answer questions about countries",
        name="Panaversty Support Agents",
    )

@cl.on_message
async def handle_message(message: cl.Message):
    result =await Runner.run(
        agent,
        input=message.content,
        run_config=config,
    )
    # Your custom logic goes here...

    # Send a response back to the user
    await cl.Message(
        content=result.final_output
    ).send()