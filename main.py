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
    
    data_from_json["company"] = company
    return data_from_json



def sales_brief(data_from_json):
    return (f"{data_from_json['company']}'s sector is {data_from_json['sector']}, focused on {data_from_json['sub_sector']}. {data_from_json['company']}'s number of employees is {data_from_json['employees']}, with total revenue of {data_from_json['revenue']}.")


company = input("Hi, I'm DavAIde, your sales agent here to support you. Which company would you like to research today? ")
risultato = account_search(company)
testo = sales_brief (risultato)
print(testo)