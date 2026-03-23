import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
 
if not api_key:
    raise ValueError("Open api key not found frin env file")
 
def get_response(prompt):

    client = OpenAI(api_key=api_key)
     
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role":"user", "content":prompt}],
    temperature = 0
        
    )
    return response.choices[0].message.content


# Craft a chain-of-thought prompt that asks the model to explain what the function does
prompt = f""" Explain your chan-of-thought, describe the function step by step ```{function}``` """
 
response = get_response(prompt)
print(response)