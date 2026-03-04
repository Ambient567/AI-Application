import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
 
if not api_key:
    raise ValueError("Open api key not found frin env file")
 
def get_response():
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
   model="gpt-4o-mini",
   # Add in the extra examples and responses
   messages=[
       {"role": "system", "content": "You are a helpful Geography tutor that generates concise summaries for different countries."},
       {"role": "user", "content": "Give me a quick summary of Portugal."},
       {"role": "assistant", "content": "Portugal is a country in Europe that borders Spain. The capital city is Lisboa."},
    {"role": "user", "content": "Give me a quick summary of Japan."},
        {"role": "assistant", "content": "Japan is an island nation in East Asia known for its advanced technology, rich culture, and capital city Tokyo."},

        {"role": "user", "content": "Give me a quick summary of Brazil."},
        {"role": "assistant", "content": "Brazil is the largest country in South America, famous for the Amazon rainforest and its capital Brasília."},

        {"role": "user", "content": "Give me a quick summary of Kenya."},
        {"role": "assistant", "content": "Kenya is an East African nation known for its diverse wildlife, Great Rift Valley, and capital Nairobi."},

       {"role": "user", "content": "Give me a quick summary of Greece."}
        ]
    )

    # print(response)
    return response.choices[0].message.content
 
 
 
 
ans = get_response()
print(ans)