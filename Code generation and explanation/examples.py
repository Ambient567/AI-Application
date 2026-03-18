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


# Craft a prompt that asks the model for the function
prompt = f"""write a Python function that receives a list of 12 floats representing monthly sales data as input and, returns the month with the highest sales value as output."""

response = get_response(prompt)
print(response)