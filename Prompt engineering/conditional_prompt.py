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




# Create the instructions
instructions = (
    "Determine the language of the given text and count the number of sentences it contains. "
    "If the text has more than one sentence, generate a suitable title for it. "
    "If the text has only one sentence, write 'N/A' for the title. "
    "The text will be provided inside triple backticks.\n\n"
)

# Create the output format
output_format = (
    "Output format:\n"
    "Text:\n"
    "Language:\n"
    "Number of sentences:\n"
    "Title:\n\n"
)

prompt = instructions + output_format + f"```{text}```"
response = get_response(prompt)
print(response)