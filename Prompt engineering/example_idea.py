# Prompt Engineering 🎉
# Learning how to talk to AI properly so that we get better, clearer, and more useful answers.


import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
 
if not api_key:
    raise ValueError("Open api key not found frin env file")


client = OpenAI(api_key=api_key)

def get_response(prompt):
	
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role":"User", "content":prompt}],
    temperature = 0
    
    )
    
    return response.choices[0].message.content

response = get_response("What is prompt engineering?")
print(response)