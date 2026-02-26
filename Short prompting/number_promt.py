import os 
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("API key not found")

def get_respose(prompt):
    client = OpenAI(api_key=api_key)
    # Create a request to the Chat Completions endpoint
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    max_completion_tokens = 100
    )

    return response.choices[0].message.content

prompt = """Classify the sentiment of each review from 1 to 5.:
1. Unbelievably good!
2. Shoes fell apart on the second use.
3. The shoes look nice, but they aren't very comfortable. 
4. Can't wait to show them off!"""


response = get_respose(prompt)

print(response)


