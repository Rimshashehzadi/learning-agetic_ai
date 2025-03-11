from litellm import completion
import os

## set ENV variables
os.environ["GEMINI_API_KEY"] = "AIzaSyDxTBBeGW8VTMD2TPwduIXySsiyHCHU5yg"

def gemini_key():
#  return os.environ["GEMINI_API_KEY"]
  response = completion(
  model="gemini/gemini-1.5-flash",
  messages=[{ "content": "Hello, how are you?","role": "user"}],
  stream=True,
)
  return "simple return"
  

def main():
    print('Hello from Litellm!')


# if __name__ == '__main__':
#     main()