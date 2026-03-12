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

report = "The market has seen rapid growthin the adoption of artificial intelligence across industries suchas finance, healthcare, and retail. Businesses are increasingly using AI to personalize customer experiences, automate customer support, and analyze large datasetsfor better decision-making. However,this rapid adoption has raised concerns among customers regardingdata privacy and security. Many consumers are becoming more cautious about how their personaldatais collected, stored, and usedby AI-driven systems. Regulatory frameworks anddata protection laws are influencing how companies design their AI solutions. As a result, companies that prioritize transparency and ethicaldata practices are gaining higher customer trust and loyalty."

prompt = f"""
Summarize the following market research report in a maximum of five sentences.
Focus specifically on how artificial intelligence and data privacy are shaping the market
and how they are affecting customer behavior.

Report:{report}
"""

response = get_response(prompt)

print("Summarized report: \n", response)