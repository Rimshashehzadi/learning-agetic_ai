from openai import OpenAI
from dotenv import load_dotenv
# Load environment variables from .env file

import os
# Import necessary libraries

load_dotenv()
# Initialize OpenAI client for OpenRouter
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")  # Set your API key in environment variable
)

# Basic chat completion
response = client.chat.completions.create(
    model= os.getenv("MODEL"),  # Basic model
    messages=[
        {"role": "user", "content": "Write a one-sentence bedtime story about a unicorn."}
    ]
)

# Print the response
print(response.choices[0].message.content)