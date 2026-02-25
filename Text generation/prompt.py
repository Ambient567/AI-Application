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

prompt = """Give the eye catching slogan for a restaurant with Italian, Chinese food and fine-dining, fast-food etc """

response = get_respose(prompt)

print(response)


