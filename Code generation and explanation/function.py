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


function = """def calculate_area_rectangular_floor(width, length):
					return width*length"""

# Craft a multi-step prompt that asks the model to adjust the function
prompt = f"""
modify the function according to the specified requirements: test if the inputs to the functions are positive, and if not, display appropriate error messages, otherwise return the area and perimeter of the rectangle.

```{function}```
"""

response = get_response(prompt)
print(response)