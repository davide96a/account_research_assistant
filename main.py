# Contratto output:
# {
#   "sector": "string",
#   "sub-sector": "string",
#   "employees": "number"
#   "revenue": "string"
# }

from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_key)


def account_search(company):
    messages = [
        {"role": "system", "content": "You are an assistant that returns company information as JSON with exactly these 4 fields: sector (string), sub_sector (string), employees (number), revenue (string). Return only the JSON, with no additional text. If you don't know a value, use null."},
        {"role": "user", "content": f"Give me information about {company} "}
    ]
    try:
        response = client.chat.completions.create(
         model="gpt-4o-mini",
         messages=messages 
    )
    except:
        print("The LLM failed to respond")
        return None

    content = response.choices[0].message.content

    try:
        data_from_json = json.loads(content)
    except: 
        print("The LLM did not return a JSON")
        return None
    
    return data_from_json

print(account_search("Banca Intesa Sanpaolo"))