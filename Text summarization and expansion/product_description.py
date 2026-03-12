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

product_description = F"""The smartphone features a6.7-inch AMOLED display with a120Hz refresh rate, offering smooth visualsand vibrant colors. It is poweredby a high-performance processor that ensures fast multitaskingand gaming. The device includes a5000mAh battery that supports fast charging, allowing extendedusage throughout the day.

The smartphone comeswith a triple-camerasystem, including a64MP main camera, an ultra-wide lens,and a macro sensor, delivering high-quality photosand videos. Italso offers5G connectivity, enhancedsecurity features suchas anin-display fingerprint sensor,and runson the latestversionof the operatingsystem."""

prompt = f"""
Summarize the following smartphone product description in no more than five bullet points.
Highlight the key features that would help users quickly compare and evaluate the product.

Product Description:{product_description}
"""

response = get_response(prompt)

print("Original description: \n", product_description)
print("Summarized description: \n", response)