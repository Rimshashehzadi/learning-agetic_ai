# from litellm import completion
# import os

# ## set ENV variables
# os.environ["GEMINI_API_KEY"] = "AIzaSyDxTBBeGW8VTMD2TPwduIXySsiyHCHU5yg"

# def gemini_key():

#   response = completion(
#   model="gemini/gemini-1.5-flash",
#   messages=[{ "content": "Hello, how are you?","role": "user"}],
# #   stream=True,
# )
#   print(response)
from litellm import completion
import os

# Set environment variable for Gemini API key
os.environ["GEMINI_API_KEY"] = "AIzaSyDxTBBeGW8VTMD2TPwduIXySsiyHCHU5yg"

def gemini_key():
    response = completion(
        model="gemini/gemini-1.5-flash",
        messages=[{"role": "user", "content": "Hello, how are you?"}],
    )
    print(response)

if __name__ == '__main__':
    gemini_key()

