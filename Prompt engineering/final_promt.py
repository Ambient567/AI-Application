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
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150,
        temperature=0,
    )
    return response.choices[0].message.content


# Dummy text to analyze
text = """
Artificial Intelligence is transforming the way people work and communicate. 
From healthcare to education, AI-powered tools are helping solve complex problems 
faster and more efficiently. Many companies are now investing heavily in AI research 
to build smarter applications for the future.
"""

# Create the instructions
instructions = instructions = (
    "Determine the language of the following text and generate a suitable title for it. "
    "Use the provided output format. The text will be delimited using triple backticks."
)

# Create the output format
output_format = (
    "Text:\n"
    "Language:\n"
    "Title:"
)



# Create the final prompt
prompt =f"""
{instructions}

Output format:
{output_format}

Text to analyze:
{text}
"""
response = get_response(prompt)
print(response)