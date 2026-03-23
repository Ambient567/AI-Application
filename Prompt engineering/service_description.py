import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
 
if not api_key:
    raise ValueError("Open api key not found frin env file")


# Add the context to the model
def get_response(prompt):

    client = OpenAI(api_key=api_key)
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user", "content":prompt}],
        temperature = 0
        
    )
    return response.choices[0].message.content

service_description = """MyPersonalDelivery is a fast and reliable delivery service that helps customers
send and receive everyday items with ease. The service delivers groceries,
medicines, electronics, clothing, documents, and small household items.

MyPersonalDelivery offers same-day delivery for groceries and medicines in most
cities, affordable pricing, real-time order tracking, and friendly customer
support. The goal of the service is to make daily deliveries simple, safe, and
stress-free for customers."""

# Define the system prompt
system_prompt = f"""You are a customer service chatbot for MyPersonalDelivery whose service description is delimited by triple backticks. You should respond to user queries in a gentle way.
 ```{service_description}```
"""

user_prompt = "What benefits does MyPersonalDelivery offer?"

# Get the response to the user prompt
response = get_response(system_prompt, user_prompt)

print(response)